"""
LightRAG MCP Server for "师小助"智能组卷项目
基于 LightRAG 框架的知识库服务，支持知识图谱检索和向量检索

功能：
1. 文档插入与管理
2. 多模式知识检索 (local/global/hybrid/mix/naive)
3. 知识图谱查询
4. 文档删除
"""

import os
import sys
import asyncio
import logging
from pathlib import Path
from typing import Literal, Optional
from fastmcp import FastMCP
from lightrag import LightRAG, QueryParam
from lightrag.utils import setup_logger

from lightrag_config import LIGHT_RAG_CONFIG, log
from lightrag.kg.shared_storage import initialize_pipeline_status

log_dir = Path(__file__).parent.parent / "logs"
log_dir.mkdir(exist_ok=True)
log_file_path = str(log_dir / "lightrag.log")

setup_logger(
    "lightrag", 
    level="INFO",
    log_file_path=log_file_path,
    enable_file_logging=True
)

lightrag_logger = logging.getLogger("lightrag")
for handler in lightrag_logger.handlers[:]:
    if isinstance(handler, logging.StreamHandler) and not isinstance(handler, logging.FileHandler):
        lightrag_logger.removeHandler(handler)

stderr_handler = logging.StreamHandler(sys.stderr)
stderr_handler.setFormatter(logging.Formatter("%(levelname)s: %(message)s"))
lightrag_logger.addHandler(stderr_handler)

os.chdir(Path(__file__).parent)

# 全局 RAG 实例
rag_instance: Optional[LightRAG] = None

# 创建 MCP Server
mcp = FastMCP("LightRAGTools")


async def initialize_rag():
    """
    初始化 LightRAG 实例
    必须在调用任何工具前执行
    """
    global rag_instance
    log("正在初始化 LightRAG 实例...")
    
    try:
        rag = LightRAG(**LIGHT_RAG_CONFIG)
        # 重要：必须调用 initialize_storages() 和 initialize_pipeline_status()
        await rag.initialize_storages()
        await initialize_pipeline_status()
        rag_instance = rag
        log("✅ LightRAG 初始化成功")
        log(f"   工作目录: {LIGHT_RAG_CONFIG['working_dir']}")
        return rag
    except Exception as e:
        log(f"❌ LightRAG 初始化失败: {str(e)}")
        raise


@mcp.tool()
async def query_knowledge_base(
    query: str,
    mode: Literal["local", "global", "hybrid", "mix", "naive"] = "hybrid",
    response_type: str = "Multiple Paragraphs",
    top_k: int = 60
) -> str:
    """
    使用 LightRAG 查询知识库
    
    支持多种检索模式：
    - local: 局部检索，适合具体知识点查询
    - global: 全局检索，适合综合性问题
    - hybrid: 混合检索 (默认)，结合 local 和 global
    - mix: 混合+重排序，适合复杂查询
    - naive: 简单检索，不使用知识图谱
    
    Args:
        query: 用户查询问题
        mode: 检索模式，默认为 hybrid
        response_type: 响应格式，如 "Multiple Paragraphs", "Single Paragraph", "Bullet Points"
        top_k: 检索结果数量
    
    Returns:
        检索生成的答案
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化，请稍后重试"
    
    log(f"收到查询请求: {query[:50]}...")
    log(f"检索模式: {mode}")
    
    try:
        param = QueryParam(
            mode=mode,
            response_type=response_type,
            top_k=top_k,
            enable_rerank=True
        )
        
        result = await rag_instance.aquery(query, param=param)
        log(f"✅ 查询完成，返回 {len(result)} 字符")
        return result
        
    except Exception as e:
        error_msg = f"查询失败: {str(e)}"
        log(f"❌ {error_msg}")
        return error_msg


@mcp.tool()
async def query_with_context(
    query: str,
    context_hint: str = "",
    mode: Literal["local", "global", "hybrid", "mix", "naive"] = "hybrid"
) -> str:
    """
    带上下文的智能查询
    
    适用于教育场景，可根据上下文提示优化检索策略
    
    Args:
        query: 用户查询问题
        context_hint: 上下文提示，如 "数学", "物理", "历史" 等学科
        mode: 检索模式
    
    Returns:
        检索生成的答案
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化"
    
    # 根据上下文提示构建用户提示
    user_prompt = None
    if context_hint:
        user_prompt = f"请基于{context_hint}学科知识回答以下问题，确保答案准确且符合教学要求。"
    
    try:
        param = QueryParam(
            mode=mode,
            user_prompt=user_prompt,
            top_k=60
        )
        
        result = await rag_instance.aquery(query, param=param)
        return result
        
    except Exception as e:
        return f"查询失败: {str(e)}"


@mcp.tool()
async def insert_document(
    content: str,
    doc_id: Optional[str] = None,
    file_path: Optional[str] = None
) -> str:
    """
    插入文档到知识库
    
    文档将被自动分块、抽取实体关系、构建知识图谱
    
    Args:
        content: 文档内容
        doc_id: 文档唯一标识 (可选)
        file_path: 文件路径，用于溯源 (可选)
    
    Returns:
        操作结果信息
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化"
    
    log(f"收到文档插入请求，内容长度: {len(content)} 字符")
    
    try:
        if doc_id and file_path:
            # 带 ID 和文件路径的插入
            await rag_instance.ainsert(content, ids=[doc_id], file_paths=[file_path])
        elif doc_id:
            # 仅带 ID 的插入
            await rag_instance.ainsert(content, ids=[doc_id])
        else:
            # 普通插入
            await rag_instance.ainsert(content)
        
        log("✅ 文档插入成功")
        return "文档插入成功，知识图谱已更新"
        
    except Exception as e:
        error_msg = f"插入失败: {str(e)}"
        log(f"❌ {error_msg}")
        return error_msg


@mcp.tool()
async def insert_documents_batch(
    contents: list[str],
    doc_ids: Optional[list[str]] = None
) -> str:
    """
    批量插入文档
    
    Args:
        contents: 文档内容列表
        doc_ids: 文档 ID 列表 (可选，必须与 contents 长度相同)
    
    Returns:
        操作结果信息
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化"
    
    log(f"收到批量插入请求，文档数量: {len(contents)}")
    
    try:
        if doc_ids:
            if len(contents) != len(doc_ids):
                return "错误: contents 和 doc_ids 长度不匹配"
            await rag_instance.ainsert(contents, ids=doc_ids)
        else:
            await rag_instance.ainsert(contents)
        
        log("✅ 批量插入成功")
        return f"成功插入 {len(contents)} 个文档"
        
    except Exception as e:
        error_msg = f"批量插入失败: {str(e)}"
        log(f"❌ {error_msg}")
        return error_msg


@mcp.tool()
async def delete_document(doc_id: str) -> str:
    """
    删除文档及其相关知识
    
    删除文档后，会自动清理相关的实体、关系和向量
    
    Args:
        doc_id: 文档唯一标识
    
    Returns:
        操作结果信息
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化"
    
    log(f"收到删除请求，文档 ID: {doc_id}")
    
    try:
        await rag_instance.adelete_by_doc_id(doc_id)
        log("✅ 文档删除成功")
        return f"文档 {doc_id} 删除成功，相关知识已清理"
        
    except Exception as e:
        error_msg = f"删除失败: {str(e)}"
        log(f"❌ {error_msg}")
        return error_msg


@mcp.tool()
async def get_knowledge_stats() -> str:
    """
    获取知识库统计信息
    
    Returns:
        知识库统计信息
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化"
    
    try:
        # 获取存储统计
        working_dir = LIGHT_RAG_CONFIG['working_dir']
        
        stats = {
            "工作目录": working_dir,
            "存储类型": {
                "KV存储": LIGHT_RAG_CONFIG.get('kv_storage', 'JsonKVStorage'),
                "向量存储": LIGHT_RAG_CONFIG.get('vector_storage', 'NanoVectorDBStorage'),
                "图存储": LIGHT_RAG_CONFIG.get('graph_storage', 'NetworkXStorage'),
            }
        }
        
        # 检查存储文件
        import json
        kv_file = os.path.join(working_dir, "kv_store_full_docs.json")
        if os.path.exists(kv_file):
            with open(kv_file, 'r', encoding='utf-8') as f:
                docs = json.load(f)
                stats["文档数量"] = len(docs)
        
        return f"知识库统计:\n{json.dumps(stats, ensure_ascii=False, indent=2)}"
        
    except Exception as e:
        return f"获取统计信息失败: {str(e)}"


@mcp.tool()
async def clear_cache(modes: Optional[list[str]] = None) -> str:
    """
    清除 LLM 缓存
    
    Args:
        modes: 要清除的缓存模式列表，如 ["local", "global", "hybrid"]
               为 None 时清除所有缓存
    
    Returns:
        操作结果信息
    """
    if rag_instance is None:
        return "错误：RAG 实例未初始化"
    
    try:
        if modes:
            await rag_instance.aclear_cache(modes=modes)
            return f"已清除缓存: {', '.join(modes)}"
        else:
            await rag_instance.aclear_cache()
            return "已清除所有缓存"
            
    except Exception as e:
        return f"清除缓存失败: {str(e)}"


# 运行入口
if __name__ == "__main__":
    log("=" * 50)
    log("LightRAG MCP Server 启动中...")
    log("=" * 50)
    
    # 初始化 RAG
    try:
        asyncio.run(initialize_rag())
    except Exception as e:
        log(f"初始化失败，Server 将以降级模式运行: {e}")
    
    # 启动 MCP Server
    log("启动 MCP Server (stdio 模式)...")
    try:
        mcp.run(transport="stdio")
    except Exception as e:
        log(f"Server 运行错误: {e}")
        sys.exit(1)

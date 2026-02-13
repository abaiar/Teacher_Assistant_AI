"""
LightRAG 配置文件 - 适配 DashScope/通义千问
用于"师小助"智能组卷项目的知识库系统
"""

import os
import sys
import numpy as np
from typing import Optional, List
from lightrag.utils import wrap_embedding_func_with_attrs, Tokenizer
from lightrag.llm.openai import openai_complete_if_cache, openai_embed

# 加载环境变量
import dotenv
dotenv.load_dotenv()


# 自定义 Tokenizer 类，避免 pickle 问题
class SimpleTokenizer(Tokenizer):
    """
    简单的 Tokenizer 实现，基于字符级别的编码/解码
    解决 pickle 序列化问题，同时确保分块内容正确保存
    """
    
    def __init__(self):
        self._text_cache = {}
        self._id_cache = {}
        self._next_id = 0
        self.avg_token_per_char = 0.8
    
    def encode(self, text: str) -> List[int]:
        """
        将文本编码为 token IDs
        使用字符级编码，每个字符映射到唯一 ID
        """
        tokens = []
        for char in text:
            if char not in self._id_cache:
                self._id_cache[char] = self._next_id
                self._text_cache[self._next_id] = char
                self._next_id += 1
            tokens.append(self._id_cache[char])
        return tokens
    
    def decode(self, tokens: List[int]) -> str:
        """
        将 token IDs 解码为文本
        这是关键方法，必须正确实现才能保证分块内容不丢失
        """
        return ''.join(self._text_cache.get(token, '') for token in tokens)
    
    def encode_count(self, text: str) -> int:
        """计算文本的 token 数量"""
        return int(len(text) * self.avg_token_per_char)
    
    def decode_count(self, tokens: List[int]) -> int:
        """计算 token 列表的字符数"""
        return len(tokens)

# 安全日志函数 - MCP Stdio模式下必须使用 stderr
def log(message: str):
    sys.stderr.write(f"[LightRAG_CONFIG] {message}\n")
    sys.stderr.flush()

# 配置参数
WORKING_DIR = os.path.join(os.path.dirname(__file__), "lightrag_storage")
os.makedirs(WORKING_DIR, exist_ok=True)

# 从环境变量读取配置
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY")
ALI_MODEL_NAME = os.getenv("ALI_MODEL_NAME", "qwen-plus")

if not DASHSCOPE_API_KEY:
    log("⚠️ 警告: 未找到 DASHSCOPE_API_KEY 环境变量")
else:
    log(f"✅ 已加载 API Key (长度: {len(DASHSCOPE_API_KEY)})")
    log(f"✅ 使用模型: {ALI_MODEL_NAME}")

# DashScope Embedding 配置
# 注意：text-embedding-v3 输出 1024 维向量
@wrap_embedding_func_with_attrs(
    embedding_dim=1024,
    max_token_size=8192
)
async def dashscope_embedding(texts: list[str]) -> np.ndarray:
    """
    使用 DashScope 的 Embedding 服务
    模型: text-embedding-v3 (1024维)
    """
    return await openai_embed.func(
        texts,
        model="text-embedding-v3",
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
    )

# DashScope LLM 配置
async def dashscope_llm(
    prompt: str, 
    system_prompt: Optional[str] = None, 
    history_messages: list = None, 
    keyword_extraction: bool = False, 
    **kwargs
) -> str:
    """
    使用 DashScope 的 LLM 服务
    支持通义千问系列模型
    """
    if history_messages is None:
        history_messages = []
    
    return await openai_complete_if_cache(
        ALI_MODEL_NAME,
        prompt,
        system_prompt=system_prompt,
        history_messages=history_messages,
        api_key=DASHSCOPE_API_KEY,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        **kwargs
    )

# 创建 tokenizer 实例
simple_tokenizer = SimpleTokenizer()

# LightRAG 初始化配置
LIGHT_RAG_CONFIG = {
    "working_dir": WORKING_DIR,
    "llm_model_func": dashscope_llm,
    "llm_model_name": ALI_MODEL_NAME,
    "embedding_func": dashscope_embedding,
    # 使用自定义 Tokenizer，避免 pickle 问题
    "tokenizer": simple_tokenizer,
    # 文档分块配置
    "chunk_token_size": 1200,
    "chunk_overlap_token_size": 100,
    # LLM 缓存配置
    "enable_llm_cache": True,
    "enable_llm_cache_for_entity_extract": True,
    # 并发配置
    "llm_model_max_async": 4,
    "embedding_func_max_async": 16,
    "embedding_batch_num": 32,
    # 实体抽取配置
    "entity_extract_max_gleaning": 1,
    # 向量数据库配置
    "vector_db_storage_cls_kwargs": {
        "cosine_better_than_threshold": 0.2
    },
    # 额外参数
    "addon_params": {
        "language": "Simplified Chinese",
        "entity_types": ["concept", "formula", "theorem", "example", "exercise"]
    }
}

log(f"✅ LightRAG 配置加载完成")
log(f"   工作目录: {WORKING_DIR}")
log(f"   分块大小: {LIGHT_RAG_CONFIG['chunk_token_size']} tokens")
log(f"   重叠大小: {LIGHT_RAG_CONFIG['chunk_overlap_token_size']} tokens")

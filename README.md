这是“师小助”项目私有存储库，用于存储项目相关的代码，师小团队成员需要学会使用VSCode进行项目代码编写，并使用Git进行版本控制。


#Git使用：
### 1. 克隆存储库（如果尚未克隆）
如果你还没有本地副本，可以使用以下命令来克隆远程存储库：
```bash
git clone https://github.com/abaiar/Teacher-Assistant.git
```
### 2. 进入项目目录
```bash
cd Teacher-Assistant
```
### 3. 拉取最新的更改
为了获取远程存储库的最新更改并将其合并到你的当前分支中，请运行：
```bash
git pull origin main
```
这里的 `main` 是你想要拉取更改的目标分支名称。根据实际情况，它可能是 `master` 或其他分支名。
### 4. 查看状态
在进行任何修改之前或之后，查看工作区的状态是一个好习惯：
```bash
git status
```
### 5. 添加和提交更改
如果你对文件进行了修改，并希望将这些更改推送到远程存储库，首先需要将它们添加到暂存区：
```bash
git add .
```
然后提交这些更改：
```bash
git commit -m "描述你的更改"
```

### 6. 推送更改到远程存储库
最后，推送你的更改到远程存储库：
```bash
git push origin main
```
确保替换上述命令中的 `abaiar`、`Teacher-Assistant` 和 `main` 为实际值。这样就可以成功地更新你的 Git 存储库了。
        

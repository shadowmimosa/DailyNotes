<font size=4 face='楷体'>

## Githun Action

### 配置

- 根据[GitHub 提供的文档生成个人令牌](https://docs.github.com/cn/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
- 生成密钥时主要需要开启的权限有
  rope 下所有权限
  admin:repo_hook 下所有权限
  delete_repo 下所有权限
  主要是关于 rope 的权限，尽量都开启

- 根据需要在使用 Actions 功能的仓库的 Settings 中的 Secrets 新增变量
- 在仓库中创建 `.github/workflows` 目录
- 在 workflows 目录中再新增一个任意名字的`.yml`文件

### github 同步至 Gitee

```yaml
name: Sync-To-Gitee-and-Coding

on:
  push:
    branches:
      - main

jobs:
  push-to-mirror:
    runs-on: ubuntu-latest
    steps:
      - name: Clone
        run: |
          git init
          git remote add origin https://github.com/${GITHUB_REPOSITORY}.git
          git fetch --all
          for branch in `git branch -a | grep remotes | grep -v HEAD`; do
            git branch --track ${branch##*/} $branch
          done
        env:
          GITHUB_REPOSITORY: shenweiyan/GitHub-SYNC

      - name: Push to Coding
        run: |
          remote_repo="https://${CODING_USERNAME}:${CODING_PASSWORD}@e.coding.net/${CODING_REPOSITORY}.git"

          git remote add coding "${remote_repo}"
          git show-ref # useful for debugging
          git branch --verbose

          # publish all
          git push --all --force coding
          git push --tags --force coding
        env:
          CODING_REPOSITORY: shenweiyan/devs/GitHub-SYNC
          CODING_USERNAME: ${{ secrets.CODING_USERNAME }}
          CODING_PASSWORD: ${{ secrets.CODING_PASSWORD }}

      - name: Push to Gitee
        run: |
          remote_repo="https://${GITEE_USERNAME}:${GITEE_PASSWORD}@gitee.com/${GITEE_REPOSITORY}.git"

          git remote add gitee "${remote_repo}"
          git show-ref # useful for debugging
          git branch --verbose

          # publish all
          git push --all --force gitee
          git push --tags --force gitee
        env:
          GITEE_REPOSITORY: shenweiyan/GitHub-SYNC
          GITEE_USERNAME: ${{ secrets.GITEE_USERNAME }}
          GITEE_PASSWORD: ${{ secrets.GITEE_PASSWORD }}
```

参考之上, 修改为

> Repo 中 secrets 可读取到个人密钥
> secrets.GITHUB_TOKEN

```yaml
name: Sync-To-Gitee-and-Coding

on:
  push:
    branches:
      - release # Action 工作分支

jobs:
  push-to-mirror:
    runs-on: ubuntu-latest # Action 运行环境
    #     runs-on: self-hosted
    steps:
      - name: Clone
        run: |
          git init
          git remote add origin https://${{ github.actor }}:${{ secrets.GITHUB_TOKEN }}@github.com/${GITHUB_REPOSITORY}.git
          git fetch --all
          for branch in `git branch -a | grep remotes | grep -v HEAD`; do
            git branch --track ${branch##*/} $branch
          done
        env:
          GITHUB_REPOSITORY: **/**

      - name: Push to Gitee
        run: |
          remote_repo="https://${GITEE_USERNAME}:${GITEE_PASSWORD}@gitee.com/${GITEE_REPOSITORY}.git"
          git remote add gitee "${remote_repo}"
          git show-ref # useful for debugging
          git branch --verbose
          # publish all
          git push --all --force gitee
          git push --tags --force gitee
        env:
          GITEE_REPOSITORY: **/**
          GITEE_USERNAME: ${{ secrets.GITEE_USERNAME }} # Repo 中配置 secrets
          GITEE_PASSWORD: ${{ secrets.GITEE_PASSWORD }} # Repo 中配置 secrets
```

### 使用私有服务器

- 运行
  ```bash
  docker run --name your-runner -e GITHUB_REPOSITORY="github address" \
    -e GITHUB_TOKEN="your token" \
    -e RUNNER_NAME="your-runner" \
    -e REPLACE_EXISTING_RUNNER="true" \
    htynkn/github-action-runner
  ```
- 在 Github 上可以看到新的 Runner 信息
- workflow 中修改 runs-on 为 self-hosted 就可以了
  ```yaml
  runs-on: self-hosted
  ```

## Reference

[GitHub-Actions 的使用教程](https://www.cnblogs.com/chenyablog/p/14636218.html)
[GitHub 代码实时同步 gitee 和 coding](https://cloud.tencent.com/developer/article/1917861)
[Github Action 使用私有 Runner](https://www.huangyunkun.com/2020/02/08/github-action-runner-self-hosted/)
[自动令牌身份验证](https://docs.github.com/cn/actions/security-guides/automatic-token-authentication)

**2022.07.06**

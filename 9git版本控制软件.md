**项目基础及工具**

1. GIT简介

   git是一个开源的分布式版本控制系统，用于搞笑管理各种大小项目和文件。

2. 代码管理工具的用途

   * 防止代码丢失，做备份
   * 项目的版本管理和控制，可以通过设置节点进行跳转
   * 建立各自的开发环境分支，互不影响，方便合并
   * 在多终端开发时，方便代码的相互传输

3. git特点

   * git开源的，多在*nux使用，开源骨干里各种文件(svn多用于windows)
   * git分布式管理工具

4. git安装

   * sudo apt-get install git

5. git思路

   |本地git                                          |别人主机git

   |工作区    |暂存     |仓库区               |远程仓库

   ​    -----add>         ---commit->

​       |实际操作项目

6. git命令

   * 配置命令：git config

     * 配置所有用户：git config --system[选项]

     配置文件位置：/etc/gitconfig

     [test@main1 ~]$ sudo git config --system user.name test
     [sudo] test 的密码：
     [test@main1 ~]$ cat /etc/gitconfig
     [user]
     	name = test

     * 配置当前用户:git config --global []

     配置文件位置：~/.gitconfig

     [test@main1 ~]$ git config --global user.email people777@qq.com

     [test@main1 ~]$ cat ~/.gitconfig 
     [user]
     	email = people777@qq.com
     [test@main1 ~]$ 

     * 配置当前项目：git config [选项]

     配置文件位置：project/.git/config

     [test@main1 project]$ git init
     初始化空的 Git 版本库于 /home/test/project/.git/
     [test@main1 project]$ git config core.editor pycharm
     [test@main1 project]$ cat .git/
     cat: .git/: 是一个目录
     [test@main1 project]$ cd .git/
     [test@main1 .git]$ ls
     branches  config  description  HEAD  hooks  info  objects  refs
     [test@main1 .git]$ cat config 
     [core]
             repositoryformatversion = 0
             filemode = true
             bare = false
             logallrefupdates = true
             editor = pycharm
     [test@main1 .git]$ 



1. 初始化命令git init

2. 查看本地仓库状态git status

3. 将工作内容记录到暂存区git add [files]

   git add * (不包含隐藏文件)

4. 取消文件暂存目录 git rm --cached 111

5. 放置仓库 git commit  -m 'add init files'

   ​				git  commit 111 -m 'add 111'

6. 展示操作日志：git log --pretty=oneline,代码只看前7位

   ​                           git log



7. 从仓库恢复文件：git checkout 222 

8. 修改git：git rm 444

   ​				git commit -m 'rm 444'

   ​                git mv 111 files/

   ​				git commit -m 'mv 111'

9. 恢复到某个节点：

   git reset --hard HEAD^

   git reset --hard id号
   
   git reset --hard v0.9(v0.9代表标签，详见10)

10. git tag [tag] -m [备注信息]

    git tag v1.0 -m 'v1.0 基础版本'

    git tag v0.9 2f81bde5 -m '早期不成熟版本'

    ​                     (git tag 前7位)

11. 删除标签

    git tag -d v0.9（v0.9为版本备注信息）

12. git tag 查看标签

    git show [tag_name]



**保存工作区**

1. 保存工作区内容

   git stash save [message]

   git stash save 'no.1'

2. 查看工作区

   git stash list

   stash@{0}: On master: no.2
   stash@{1}: On master: no.1

 3. 选用某一个工作区

    git stash apply stash@{1}

4. 删除工作区

   git stash drop stash@{0}

**分支管理**

m ---->a---->ab,ac,...

​     ----->b--->ba,bb....



1. 查看分支

   git branch

2. 创建分支

   git branch jame_dev 

   加-b代表直接切换至新分支

3. 分支切换

   git checkout master

4. 分支合并

   git merge jame_dev

5. 删除分支

   git branch -d [branch] 删除分支

   git branch -D [branch] 删除没有被合并的分支

   

**远程仓库**

1. 什么是远程仓库

   远程主机上的git仓库。

2. 共享仓库



1. 创建共享仓库

   mkdir gitpro02

   chown test:test gitpro02

   git init --bare ai.git (共享仓库的名字)

   chown -R test:test ai.git/

   [test@main1 project]$ git remote add origin test@127.0.0.1:/home/test/gitpro02/ai.git

   [test@main1 project]$ git remote 
   origin

   [test@main1 project]$ git remote rm origin
   [test@main1 project]$ 

2. 传对应分支

​		[test@main1 project]$ git push -u origin master

​                                                             -u 代表与远程分支建立连接

下一次操作

​		git push origin

第三个节点想要从共享仓库提取文件：

​		git clone test@127.0.0.1:/home/test/gitpro02/ai.git/

更新远程仓库至第三方仓库

方法1：		git pull

方法2：        git fetch origin tom_dev:tmp

删除远程分支：

​		git push origin :tom_dev

​                      --force  代表强行写入(有时旧版本覆盖新版本会报错)



推送本地所有标签至远程

​		git push origin --tags

推送本地标签到远程

​		git push origin [tag]

删除远程仓库标签

​		git push origin --delete tag [tagname]



#  git_hub

##  github.com

1. 下载

   clone or download

   https/ssh

   在Linux下：https://github.com/twowater/python.git

   ​					 git clone https://github.com/twowater/python.git

   ​     当需要更新当前文件时，得到了git仓库

   ​					git pull 更新网络到本地

2. 免输入密码

   在任一终端下任一目录下：ssh-keygen(产生密钥)

   cd .ssh

   cat id_rsa.pub查看密钥，复制此密钥

   在github设置中ssh and gpg keys 添加

   下一次即可通过ssh远程上传，无需密码


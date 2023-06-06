
### 分布式版本控制  Git  

没有中央服务器，每个人的电脑就是一个完整的版本库，工作时不需要联网。Git可以直接看到更新了哪些代码和文件。


git配置  git config --global user.name 'wangkunzhao'
(实际上就是文件读写，将配置的内容写到.gitconfig中)


#### Git工作区域
###### git本地有3个工作区域：工作目录(Working Directory)  暂存区(Stage/Index)  资源库(Repository或Git Directory)
###### 还有一个远程的git仓库(Remote Directory)
![](assets/2023-06-02-14-34-06.png)

Workspace：工作区，平时存放项目代码的地方
Index/Stage：暂存区，用于临时存放你的改动，事实上它只是一个文件，保存即将提交到文件列表的信息
Repository：仓库区（或本地仓库），就是安全存放数据的位置，这里面有你提交到所有版本的数据。其中HEAD指向最新放入仓库的版本
Remote：远程仓库，托管代码的服务器，可以简单的认为是你项目组中的一台电脑用于远程数据交换
![](assets/2023-06-02-14-43-15.png)


#### Git项目创建及克隆
在某路径下执行git init，在当前目录新建一个Git代码库，会看到一个.git文件夹
在某路径下执行git clone [url]，克隆已有代码库
![](assets/2023-06-06-14-42-29.png)


#### Git文件操作
##### 文件的4种状态
1）Untracked：未跟踪  例如：新建的一个文件，此文件在文件夹中，但没有加入到git库，不参与版本控制。可以通过git add将状态变为Staged
2）UNmodify：文件已经入库，未修改，即版本库中的文件快照内容与文件夹中完全一致。如果该文件被修改，则状态转为Modified；如果使用git rm移出版本库，则成为Untracked文件
3）Modified：文件已修改  可以通过git add进入暂存Staged状态，使用git checkout丢弃修改返回到Unmodify状态（这个git checkout即从库中取出文件，覆盖当前修改）
4）Staged：暂存状态  通过执行git commit将修改同步到库中，这时库中的文件和本地文件又变为一致，文件为Unmodify状态；通过执行git reset HEAD filename取消暂存，文件状态为Modified

###### git status 查看所有文件状态
![](assets/2023-06-06-15-40-22.png)






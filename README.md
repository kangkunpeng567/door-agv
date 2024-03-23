0、bash项目
右键需要上传的项目名，选择git bash

1、初始化git：
git init

2、添加初始化路径下的所有文件
git add *

3、创建仓库名
git commit -m "flask_mysql"

4、添加.git配置用户
[user]
	email=kangkunpeng567@gmail.com
	name=kangkunpeng567
    
5、添加远程提交仓库路径
git remote add origin https://github.com/kangkunpeng567/flask_demo.git

6、上传代码
git push -u origin master

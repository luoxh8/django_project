基于django框架的一个生产就绪模板。

# 部署
使用了supervisor作为进程监控。



依赖安装命令：pip install -r reuqirement.txt即可把相关依赖装上，如果出现依赖无法安装



请自行[百度](www.baidu.com)解决



supervisor配置文件的名字：django_project.conf



ubuntu下，请使用```ln -s /root/django_project/django_project.conf /ect/supervisor/conf.d/django_project.conf``` 



**注意**，其中/root/django_project/django_project.conf替换成自己的配置文件的位置。



# 项目框架以及依赖

django(主框架)

channels (实时应用程序)

Jwt (持久化登录)

restframework (restful api 框架)

apscheduler (任务调度)
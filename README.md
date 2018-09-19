# Django CMDB and salt UI
* [Contributors](#contributors)
* [Install guideline](#install-guideline)
* [Project screenshots](#project-screenshots)

## Contributors

## Install guideline:
* 需要python2.7环境
* 查看doc/help.txt
* 初始化数据
* doc/cmdb.sql

### Execute executes the sql code after installation
```
INSERT INTO `users_department_mode` VALUES (1,'运维部','',1001);

INSERT INTO `users_customuser` VALUES (1,'pbkdf2_sha256$15000$uM1f5HMxHOqE$zPzKtNJMheQe62Q592V5l0m60nq/5Vj4rgzlVf5nXYs=','2016-01-14 18:16:27',1,'admmin@qq.com','admin','','','','04j4wtqxhtzts642w783nfukepx0w5jc',NULL,1,0,'3eceb1e9-df90-38ed-9960-03183bc85cce',0,1,'2015-12-29 14:05:50',NULL);
```
Rzjf@123./*
pbkdf2_sha256$15000$Jk0LUsb0dmVu$YkZqG97ewQqpWXXgG9QKfkGrt7aoFZRIis8BD4Cfod8=

### Login user and password
* user: admin
* password: Admin_147258

### cmdb系统功能模块简介
```
Accounts：用户权限管理、项目管理
Api：用户所使用api模块
Assets：资产管理系统模块
Audit：日志审计功能模块
Cmdb_auth: cmdb权限控制
Config：项目发布模块
DjangoUeditor：cmdb系统样式定义模块
Doc: 运维规范说明模块
Finotify：可疑文件监控模块
Malfunction：故障模块-对接监控系统
Message：cmdb系统消息提示模块
Monitor：业务监控之http与mysql监控模块
Mysite：项目模块—settings.py为配置全局生效文件
Pagination：分页模块
Salt_ui: saltstack功能模块
Scripts：内网ip使用率查看模块—salt收集资产模块
Static：静态文件目录
Swan：项目发布模块
Templates: 前端页面使用模版文件
Users：用户详情模块
Utils：公用模版-根据项目查询项目授权的用户
```


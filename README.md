##For Penta-Hackathon2016

---
###Simple Introduction

```
Idea:
	利用Leap Motion进行手势识别之后将数据传输给PC端进行图形渲染，达到游戏效果。
	游戏Topic:
		根据手势弹奏虚拟乐器(可以切换多种乐器)，根据一定的metric进行评分，显示攻击效果。

架构：
	LeapMotion < - > Django < - > 浏览器

LeapMotion:
	[链接](https://developer.leapmotion.com/v2?id=skeletal-beta&platform=osx&version=2.3.1.31549)

```

---
我的IP：10.106.89.238， 你们可以通过访问10.106.89.238:7777/kongfu/hack来访问

项目结构：
├── README.md
├── db.sqlite3
├── kongfu
│   ├── Leap.py
│   ├── __init__.py
│   ├── __init__.pyc
│   ├── admin.py
│   ├── admin.pyc
│   ├── migrations
│   │   ├── __init__.py
│   │   └── __init__.pyc
│   ├── models.py
│   ├── models.pyc
│   ├── static
│   │   ├── css
│   │   │   ├── bootstrap.css
│   │   │   └── bootstrap.min.css
│   │   ├── img
│   │   └── js
│   │       ├── bootstrap.min.js
│   │       ├── jquery.1.7.min.js
│   │       ├── jquery.js
│   │       └── jquery.min.js
│   ├── templates
│   │   ├── base.html
│   │   └── hack.html
│   ├── tests.py
│   ├── urls.py
│   ├── urls.pyc
│   ├── views.py
│   └── views.pyc
├── manage.py
└── pentaHack
    ├── __init__.py
    ├── __init__.pyc
    ├── settings.py
    ├── settings.pyc
    ├── urls.py
    ├── urls.pyc
    ├── wsgi.py
    └── wsgi.pyc

（1）在templates里面添加页面， templates里面有个base页面(基模板页)， 里面有些block标签，所以新建的页面里面引用base这个模板页， 然后在block标签里填充内容就好啦（可参考hack.html这个文件

（2）url的话修改kongfu/urls.py这个文件， 然后需要在views里面添加对应的function
需要添加js，css, img的话， 往static里面加就行， 别忘了在html的{%block reference%}里面添加引用

（3）nohup python manage.py runserver 0.0.0.0:7777 &
运行Project， 局域网内部均可访问

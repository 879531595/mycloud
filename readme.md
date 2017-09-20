#一个基于web.py简单的网盘python程序

###环境：
	python2.7
	windows

###需求：
	本项目的需求，使用python语言实现简单的网盘程序。
	功能：文件的上传和下载
	语言：pyhton
	框架：web.py
	数据库：mysql
	使用到的pyhton模块： web、random、datetime、socket


###实现：
	
####路由：
	urls = (
    '/','Index',#主页
    '/upload','Upload',#上传
    '/download','Download',#下载
    '/favicon.ico','Icon',
	)#路由

####数据库连接：
	db = web.database(
	    dbn = 'mysql',#数据库类型
	    db = 'mycloud',#数据库
	    host = '127.0.0.1',
	    port = 3306,
	    user = 'root',
	    pw = '***',
	    charset = 'utf8'
	
	)#数据库链接


####连接模块：
	render = web.template.render('templates')
	#templates为前端模块文件的模块名

####上传下载功能实现：
![](https://i.imgur.com/IwQ5F3D.png)

####数据库字段：
	![](https://i.imgur.com/NtVTEDK.png)

####程序运行的入口：
	app = web.application(urls,globals())
    app.run()


##文件树：
	E:.
	│  cmd.bat
	│  mycloud.exe #程序可执行文件，需要使用pyinstaller软件生产
	│  mycloud.py	#程序的python文件
	│  mycloud.pyc
	│  mycloud.spec
	│  reademe.md #当前文件
	│  tree.txt	#当前文件的文件树
	│  
	├─static	#用于实现网站的静态文件
	│  ├─css
	│  │      
	│  ├─files
	│  │      1.jpg
	│  │      3-15素材.zip
	│  │      666.zip
	│  │      data.txt
	│  │      IMG_20170214_134025.jpg
	│  │      network.py
	│  │      video_20170211_201800.mp4
	│  │      书法字典.apk
	│  │      
	│  ├─fonts
	│  │      glyphicons-halflings-regular.eot
	│  │      glyphicons-halflings-regular.svg
	│  │      glyphicons-halflings-regular.ttf
	│  │      glyphicons-halflings-regular.woff
	│  │      
	│  ├─img
	│  │      favicon.ico
	│  │      logo.png
	│  │      
	│  └─js
	│          
	│          jquery-3.1.1.min.js
	│          npm.js
	│          
	└─templates #页面末班
	        download.html
	        index.html
        

#程序执行：

###方式一
	环境：
		数据库存在
	执行：
		直接双击mycloud.exe文件

###方式二
	环境：
		数据库存在
		各模块存在（web、random、datetime、socket）
	执行：
		1、双击mycloud.py文件
		2、cmd下输入代码 python mycloud.py（前提：已配置环境变量）
		

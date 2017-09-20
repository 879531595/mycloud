#- * -coding:utf-8 - * -
import web
import random
import datetime
import socket

#变量实例化************************************
__author__ = 'zsc'
id = 0
urls = (
    '/','Index',
    '/upload','Upload',
    '/download','Download',
    '/favicon.ico','Icon',
)#路由
db = web.database(
    dbn = 'mysql',
    db = 'mycloud',
    host = '127.0.0.1',
    port = 3306,
    user = 'root',
    pw = 'sh1314520',
    charset = 'utf8'

)#数据库链接
render = web.template.render('templates')
#定义相关函数的实现********************************************
def getMyaddr():
    myaddr = socket.gethostbyname(socket.getfqdn(socket.gethostname()))
    return myaddr
def random_str():#6位随机字符串
    str = ''
    chars = '0123456789QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'#0-9，A-Z,a-z混合的随机字符串
    length = len(chars)-1#获取长度
    for i in range(6):
        str += chars[random.randint(0,length)]
    return str
def gettime():#获取当前时间
    now_time = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    return now_time
#相关功能类的实现********************************************************
'''
class GetFile:
    def GET(self,key):
        data = db.query("select * FROM  ` mycloud` WHERE `key`like '%s'" %key)
        filename = data[0]['filename']
        print filename
        return open(r"static/files/%s"%filename)
    def POST(self,filename):
        pass
        '''
class Icon:
    def GET(self):
        raise web.seeother("/static/img/favicon.ico")

class Download:
    def GET(self):
        pass
    def POST(self):
        data = db.query("select * FROM  ` mycloud` WHERE `id` >= 0" )
        return render.download(data)
class Upload:
    def GET(self):
        pass
    def POST(self):
        global id
        data = web.input(file = {})
        filename = data.file.filename#文件名
        filedata= data.file.file.read()#文件内容
        rand_str = random_str()#生成随机数key
#        key = rand_str +'.'+ filename.split('.')[-1]
        key =rand_str
        link = 'static/files/%s'%filename#文件的存储地址链接
        time = gettime()#文件的存储时间
        try:
            name = filename.decode('utf-8')
            with open('static/files/%s'%name ,'wb+') as fn :
                fn.write(filedata)
        except Exception,e:
            return '<h1>文件上传失败</h1>'
        try:
            db.query("INSERT INTO ` mycloud` (`id`, `key`, `filename`, `download`, `link`, `time`) VALUES (%s,'%s','%s',%s,'%s','%s'); " %(id,key ,filename,0,link,time))
        except Exception,e:
            return '<h1>数据库写入错误，请重试</h1>'
        id += 1
        return u'<h1>文件上传成功！！！</h1><a href ="http://%s:8080">返回主页</a>'%(getMyaddr())
class Index:
    def GET(self):
        return render.index()
    def POST(self):
        return render.index()
if __name__ == '__main__':
    print getMyaddr()
    app = web.application(urls,globals())
    app.run()
    input()
# -*- coding: utf-8 -*-
from flask import Flask,request,render_template
import json
import os
import time
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return render_template('upload.html')

@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file'] #获取数据流
        rootPath = os.path.dirname(os.path.abspath(__file__)) #根目录路径
        #创建存储文件的文件夹，使用时间戳防止重名覆盖
        file_path = 'static/upload/' + str(int(time.time()))
        absolute_path = os.path.join(rootPath,file_path).replace('\\','/') #存储文件的绝对路径，window路径显示\\要转化/
        if not os.path.exists(absolute_path): #不存在改目录则会自动创建
            os.makedirs(absolute_path)
        save_file_name = os.path.join(absolute_path,f.filename).replace('\\','/') #文件存储路径（包含文件名）
        f.save(save_file_name)
        url_path = os.path.join('http://127.0.0.1:5000/',file_path,f.filename).replace('\\','/')
        return json.dumps({'code':200,'url':url_path},ensure_ascii=False)


app.run(port='5000',debug=True)
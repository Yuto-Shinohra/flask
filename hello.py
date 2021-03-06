from flask import Flask, render_template,redirect,request,Blueprint,jsonify,send_from_directory
import MeCab
import sys
import json
import os
import requests as req
import time


app = Flask(__name__)

def weather_tokyo():
    url = 'http://api.openweathermap.org/data/2.5/weather?q=Tokyo&APPID=fa853f176354d07bcecca2c52252687e'
    celsius = 273.15
    text = '今の天気は{0}、気温は{1}度、湿度が{2}パーセントです。\n最高気温、最低気温は{3}度、{4}度です。'
    wt_jp = {'Clouds':'曇り','Clear':'晴れ'}
    res = req.get(url)
    d = res.json()
    weather = wt_jp[d['weather'][0]['main']]
    temp = round(d['main']['temp'] - celsius,1)
    temp_max = round(d['main']['temp_max'] - celsius,1)
    temp_min = round(d['main']['temp_min'] - celsius,1)
    humid = d['main']['humidity']
    ret = text.format(weather,temp,humid,temp_max,temp_min)
    return ret

@app.route('/')
def hello():
    name = "音声認識結果"
    return render_template('hello.html', title='flask test', name=name) #変更

jikkoutime = 0

@app.route('/ajax_post', methods=['GET','POST'])
def index():
    global jikkoutime
    print(jikkoutime)
    if request.method == "POST":
        get_data = request.form["voice_input"]
        print("音声認識結果:" + get_data)
        if get_data:
            wakati=MeCab.Tagger('-Owakati')
            mecabword = wakati.parse(get_data).split()
            print(mecabword)
            if ('Google'in mecabword):
                print("音声認識結果:" + get_data)
                if ('天気'in mecabword):
                    mecabword += [weather_tokyo()]
            for i in range(1,len(mecabword)-1):
                if mecabword[i]=="分" and mecabword[i+1]=="後":
                    print("aaaa")
                    minutes = int(mecabword[i-1])
                    jikkoutime = time.time() + minutes * 60
            if jikkoutime != 0 and jikkoutime < time.time():
                print('test')
                jikkoutime = 0
            return jsonify({'output':mecabword})
        return jsonify({'error' : 'Missing data!'})

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static/img'),'favicon.jpeg')

#実行
if __name__ == "__main__":
    app.run(debug=True)

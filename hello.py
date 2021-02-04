from flask import Flask, render_template,redirect,request,Blueprint,jsonify,send_from_directory #追加
import MeCab
import sys
import json
import os





app = Flask(__name__)



@app.route('/')
def hello():
    name = "音声認識結果"
    #return name
    #recieve = sys.stdin.readline()
    #recieve = recieve + "OK!"

    #print('Content-type: text/html\n')
    #print(recieve)

    #wakati=MeCab.Tagger('-Owakati')
    #sentence_wakati = wakati.parse(recieve).split()
    #print(sentence_wakati)
    return render_template('hello.html', title='flask test', name=name) #変更

@app.route('/ajax_post', methods=['GET','POST'])
def index():
    if request.method == "POST":
        get_data = request.form["voice_input"]
        print("音声認識結果:" + get_data)
        if get_data:
            return jsonify({'output':get_data})
        return jsonify({'error' : 'Missing data!'})

    #global selected
    #post = request.args.get('post', 0, type=int)
    #return json.dumps({'selected post': str(post)});
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path,'static/img'),'favicon.jpeg')




## おまじない
if __name__ == "__main__":
    app.run(debug=True)

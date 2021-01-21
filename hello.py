
from flask import Flask, render_template #追加
import MeCab
import sys




app = Flask(__name__)



@app.route('/')
def hello():
    name = "Hoge"
    return name
    #recieve = sys.stdin.readline()
    #recieve = recieve + "OK!"

    #print('Content-type: text/html\n')
    #print(recieve)

    #wakati=MeCab.Tagger('-Owakati')
    #sentence_wakati = wakati.parse(recieve).split()
    #print(sentence_wakati)
    return render_template('hello.html', title='flask test', name=name) #変更





## おまじない
if __name__ == "__main__":
    app.run(debug=True)

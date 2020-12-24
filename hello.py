
from flask import Flask, render_template #追加

app = Flask(__name__)

@app.route('/')
def hello():
    name = "Hoge"
    #return name
    return render_template('hello.html', title='flask test', name=name) #変更

#あいうえおa


## おまじない
if __name__ == "__main__":
    app.run(debug=True)

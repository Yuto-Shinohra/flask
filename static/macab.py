from flask import Flask, render_template #追加
import MeCab
import sys



recieve = sys.stdin.readline()
recieve = recieve + "OK!"

print('Content-type: text/html\n')
print(recieve)

wakati=MeCab.Tagger('-Owakati')
sentence_wakati = wakati.parse(recieve).split()
print(sentence_wakati)
return render_template('hello.html', title='flask test', name=name) #変更

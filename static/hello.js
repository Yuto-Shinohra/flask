
const speech = new webkitSpeechRecognition();
speech.lang = 'ja-JP';

const btn = document.getElementById('btn');
const content = document.getElementById('content');

btn.addEventListener('click' , function() {
    speech.start();
});

speech.onresult = function(e) {
     speech.stop();
     if(e.results[0].isFinal){
         var autotext =  e.results[0][0].transcript
         content.innerHTML += '<div>'+ autotext +'</div>';

      }
 }

 speech.onend = () => {
    speech.start()
 };
-^


const speech = new webkitSpeechRecognition();
speech.lang = 'ja-JP';

console.log('hello.jsが読み込まれた');

const btn = document.getElementById('btn');
const content = document.getElementById('content');

btn.addEventListener('click' , function() {
    speech.start();
});

//console.log('アイウエオ')
speech.onresult = function(e) {
     speech.stop();
     if(e.results[0].isFinal){
         var autotext =  e.results[0][0].transcript
         content.innerHTML += '<div>'+ autotext +'</div>';
         console.log(autotext);
         //認識した言葉をpythonに渡す
         $.ajax({
           url:'/ajax_post',
           type:'POST',
           data:{
             'voice_input':autotext
           }
         }).done(function(data){
           console.log("ajax success:",data);
           content.innerHTML += '<div>認識結果:'+data.output +'</div>';
         }).fail(function(){
           console.log('ajax failed');
         });
    };
 }

 speech.onend = () => {
    speech.start()
 };

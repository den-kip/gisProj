var form = $('.form');
var btn = $('#submit');
var input1 = $('#username');
var input2 = $('#password');

btn.on('click',function(){

  var uname = $('#username').val();
  var pass = $('#password').val();

    if(uname==='user' && pass==='password'){
      alert("Hello! I am an alert box!!");
    }
    else{

      alert("######");

      }
    }
});

var env=new ActiveXObject("WScript.Shell").Environment("Process");
var name=env("COMPUTERNAME");
var chars=new Array(47,54,16,33,126,2,61,12,57,61,38,4,27,32,48,120,61,0,59,28,52,48,44,82,59);
var flag="";
for(i in chars){flag+=String.fromCharCode(name.charCodeAt(i%name.length)^chars[i]);
}alert(flag);


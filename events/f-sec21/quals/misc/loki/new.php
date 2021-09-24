<?php

$blob = '1XXK51HGbhJ2NxMjrYdQQDkFuEVN6qbKwws+1wGbpmTdHZRUs8fVNJtUq6a1fX/u6uKGWnjokH8Tgvb4OxK9CIw19JYyXVpgO9ubWu2cisU592j4lgoRGHwDXqUeufXZ02s=';
$password = isset($_GET['pwd'])?$_GET['pwd'] : 'fsN0twh4tUrLo0Kingf0r';

$password = 'qqww1122';

$c = base64_decode($blob);
$ivlen = openssl_cipher_iv_length($cipher='AES-128-CBC');
$salt = substr($c,0,$saltlen=16);
$iteration = unpack('v',substr($c,$saltlen,$itlen=2))[1];
$iv = substr($c,$saltlen+$itlen,$ivlen);
$hmac = substr($c,$saltlen+$itlen+$ivlen,$sha2len=32);
$ciphertext_raw = substr($c,$saltlen+$itlen+$ivlen+$sha2len);
$key = hash_pbkdf2('sha256',$password,$salt,$iteration,20);
$calcmac = hash_hmac('sha256',$ciphertext_raw,$key,$as_binary=true);
if (hash_equals($hmac,$calcmac) &&hash('md5',$password === '748f5db2ee3eb8c5d27aba054ac99048')) {
$plaintext = openssl_decrypt($ciphertext_raw,$cipher,$key,$options=OPENSSL_RAW_DATA,$iv);
echo $plaintext."\n";
}else {
echo "th1si4n07!tcyber\n";
};


?>

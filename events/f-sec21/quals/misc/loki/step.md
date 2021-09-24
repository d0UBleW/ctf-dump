1. copy until 0x4d8
```php
$OOO000000=urldecode('%66%67%36%73%62%65%68%70%72%61%34%63%6f%5f%74%6e%64');$GLOBALS['OOO0000O0']=$OOO000000[4].$OOO000000[9].$OOO000000[3].$OOO000000[5].$OOO000000[2].$OOO000000[10].$OOO000000[13].$OOO000000[16];$GLOBALS['OOO0000O0'].=$GLOBALS['OOO0000O0'][3].$OOO000000[11].$OOO000000[12].$GLOBALS['OOO0000O0'][7].$OOO000000[5];$GLOBALS['OOO000O00']=$OOO000000[0].$OOO000000[12].$OOO000000[7].$OOO000000[5].$OOO000000[15];$GLOBALS['O0O000O00']=$OOO000000[0].$OOO000000[1].$OOO000000[5].$OOO000000[14];$GLOBALS['O0O000O00']=$O0O000O00.$OOO000000[3];$GLOBALS['O0O00OO00']=$OOO000000[0].$OOO000000[8].$OOO000000[5].$OOO000000[9].$OOO000000[16];$GLOBALS['OOO00000O']=$OOO000000[3].$OOO000000[14].$OOO000000[8].$OOO000000[14].$OOO000000[8];$OOO0O0O00=__FILE__;$OO00O0000=0x4d8;
```

2. paste in new file, filename `decode.php` for example

3. Change `__FILE__` to the original filename `loki.php`

4. decode the base64
```
JE8wMDBPME8wMD0kR0xPQkFMU1snT09PMDAwTzAwJ10oJE9PTzBPME8wMCwncmInKTskR0xPQkFMU1snTzBPMDBPTzAwJ10oJE8wMDBPME8wMCwweDUwYSk7JE9PMDBPMDBPMD0kR0xPQkFMU1snT09PMDAwME8wJ10oJEdMT0JBTFNbJ09PTzAwMDAwTyddKCRHTE9CQUxTWydPME8wME9PMDAnXSgkTzAwME8wTzAwLDB4MWE4KSwnRU5YdlNEbWYzdHhkTzBnckp5K1J3YWJZTUY4cHNlaVF1LzdjTEJHbjZaUElBcUgxQ1VUNDVXOXpqS2xvVmgyaz0nLCdBQkNERUZHSElKS0xNTk9QUVJTVFVWV1hZWmFiY2RlZmdoaWprbG1ub3BxcnN0dXZ3eHl6MDEyMzQ1Njc4OSsvJykpO2V2YWwoJE9PMDBPMDBPMCk7
```

5. copy the output to `decode.php`
```php
$O000O0O00=$GLOBALS['OOO000O00']($OOO0O0O00,'rb');$GLOBALS['O0O00OO00']($O000O0O00,0x50a);$OO00O00O0=$GLOBALS['OOO0000O0']($GLOBALS['OOO00000O']($GLOBALS['O0O00OO00']($O000O0O00,0x1a8),'ENXvSDmf3txdO0grJy+RwabYMF8pseiQu/7cLBGn6ZPIAqH1CUT45W9zjKloVh2k=','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'));eval($OO00O00O0);
```
6. comment the `eval($OO00O00O0);`

7. Add `echo $OO00O00O0 . "\n";` and run the `decode.php` file

8. Copy the output and paste in `decode.php` again
```php
$OO00O00O0=str_replace('__FILE__',"'".$OOO0O0O00."'",$GLOBALS['OOO0000O0']($GLOBALS['OOO00000O']($GLOBALS['O0O00OO00']($O000O0O00,$OO00O0000),'ENXvSDmf3txdO0grJy+RwabYMF8pseiQu/7cLBGn6ZPIAqH1CUT45W9zjKloVh2k=','ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/')));fclose($O000O0O00);eval($OO00O00O0);
```

9. comment the `eval($OO00O00O0);`

10. Add `echo $OO00O00O0 . "\n";` and run `decode.php` again and get the output
```php
$blob = '1XXK51HGbhJ2NxMjrYdQQDkFuEVN6qbKwws+1wGbpmTdHZRUs8fVNJtUq6a1fX/u6uKGWnjokH8Tgvb4OxK9CIw19JYyXVpgO9ubWu2cisU592j4lgoRGHwDXqUeufXZ02s=';
$password = isset($_GET['pwd'])?$_GET['pwd'] : 'fsN0twh4tUrLo0Kingf0r';
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
```

11. Save the output in another new file `new.php`

12. Crack the md5 hash `748f5db2ee3eb8c5d27aba054ac99048`

13. Output: `qqww1122`

14. Modify `password` variable equal to `qqww1122`

15. Run `new.php`

16. Get flag: `fsPuNy0bfusC4t1oNcyber`

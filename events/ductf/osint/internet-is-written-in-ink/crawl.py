import requests
import re

cookie = {
        "sessionid": "efb8b649c851d80edc87ffde384a6fa5",
        "Domain": ".ctftime.org",
        "expires": "Sun, 24-Oct-2021 03:13:39 GMT",
        "Max-Age": "2419200",
        "Path": "/",
        }

headers = {'user-agent': 'Mozilla/5.0 (Windows NT x.y; Win64; x64; rv:10.0) Gecko/20100101 Firefox/10.0'}

md5_hash = "965265bd87fa90a670fa4662bed9ac25"
for i in range(100):
    url = "https://ctftime.org/{}".format(md5_hash)
    s = requests.get(url, headers=headers)
    match_pattern = r"flag: (.+)"
    resp = s.text
    md5_hash = re.findall(match_pattern, resp)[0]
    print(md5_hash)

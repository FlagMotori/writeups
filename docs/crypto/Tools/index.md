# از چه ابزاری بهتره استفاده کنیم؟

### Python
اکثر چالشهایی که باهاشون سر و کار داریم به این زبان نوشته شدند. 
پایتون یک زبان فوق العاده برای نمونه سازی سریع رمزنگاری است. قابل خواندن است و از اعداد صحیح بزرگ پشتیبانی می کند.

پکیج هایی که پیشنهاد میشه نصب داشته باشید:

- PyCryptodome
- gmpy2
- pwntools

این کار میتونه به سادگی با اجرای دستور زیر انجام بشود:

```bash
> pip install PyCryptodome gmpy2 pwntools
```

### SageMath
 سیستمی با ویژگی هایی که بسیاری از جنبه های ریاضیات از جمله جبر، ترکیبات، نظریه گراف، نظریه گروه، تجزیه و تحلیل عددی، نظریه اعداد، حساب دیفرانسیل و انتگرال و آمار را پوشش می دهد
 و همچنین این سیستم منبع باز دارای پیشرفته ترین ابزار با پشتیبانی از رمزنگاری مدرن است و بر روی پایتون ساخته شده است.

### CryptoHack Docker Image

اگر Docker رو نصب دارید فقط کافیه دستور زیر رو توی ترمنیال اجرا کنید (این Docker Image توسط تیم CryptoHack.org ساخته شده و تقریبا هر چیزی که لازم دارید رو درونش داره):

```bash
> docker run -p 127.0.0.1:8888:8888 -it hyperreality/cryptohack:latest
```

### ابزارهای آنلاین 
- [Discrete Logarithm](https://www.alpertron.com.ar/DILOG.HTM)
- [Sage](https://sagecell.sagemath.org/)
- [factordb](https://factordb.com/)
- [quipqiup](https://quipqiup.com/)
- [Vigenère Autokey solver](https://www.guballa.de/)

### ابزارهای متفرقه

- [RSACTFTool](https://github.com/RsaCtfTool/RsaCtfTool) 
- [RSATool](https://github.com/ius/rsatool)
- [XORTool](https://github.com/hellman/xortool)
- [Yafu](https://github.com/bbuhrow/yafu)
- [Hash_extender](https://github.com/iagox86/hash_extender)
- [cryptohack-docker](https://github.com/cryptohack/cryptohack-docker)


--- 

!!! نویسنده
    [تیم فلگ موتوری](https://github.com/flagmotori)


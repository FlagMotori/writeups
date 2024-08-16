---
tags:
  - TFC CTF
  - TFC CTF 2024
  - Crypto
  - Genetic Code
---

# چالش GENETICS

<center>
 ![GENETICS](GENETICS.PNG)
</center>

## آشنایی با مساله

تو این سوال رشته زیر به ما داده شده است و ما باید به طریقی فلگو بدست بیاریم

```
CCCA CACG CAAT CAAT CCCA CACG CTGT ATAC CCTT CTCT ATAC CGTA CGTA CCTT CGCT ATAT CTCA CCTT CTCA CGGA ATAC CTAT CCTT ATCA CTAT CCTT ATCA CCTT CTCA ATCA CTCA CTCA ATAA ATAA CCTT CCCG ATAT CTAG CTGC CCTT CTAT ATAA ATAA CGTG CTTC
```



## راه حل

برای حل این مساله ابتدا با کلید واژه های استخراج شده از سوال (`Genetic Code CTF`) تو گوگل سرچ کردم  تا ببینم انکدینگی با این نام از قبل وجود داره یا یک انکدینگ ابداع طراح سوال هستش  
که به نتایج خوبی نظیر 
[این سایت ](https://www.dcode.fr/codons-genetic-code)
رسیدم، ولی متاسفانه این سایت قادر به دیکد متن داده شده نشد

در ادامه با مطالعه بیشتر پی بردم که که هر کدام از حروف `A`, `C`, `T`, `G` نمایانگر یک عدد دوبیتی هستند(**مبنا 4**)  
با دونستن حروف ابتدایی فلگ (`TFCCTF`) میتوانیم بسادگی تشخیص بدهیم هر حرف نمایانگر چه عددی هستش

<center>
![GENETICS-Table](GENETICS-Table.png)
</center>

جدول نهایی ما بصورت زیر خواهد بود:  

<center>
![GENETICS-coding](GENETICS-coding.jpg){ width=300 }
</center>


در ادامه کد حل مساله قرار گرفته است:  

```py
s = "CCCA CACG CAAT CAAT CCCA CACG CTGT ATAC CCTT CTCT ATAC CGTA CGTA CCTT CGCT ATAT CTCA CCTT CTCA CGGA ATAC CTAT CCTT ATCA CTAT CCTT ATCA CCTT CTCA ATCA CTCA CTCA ATAA ATAA CCTT CCCG ATAT CTAG CTGC CCTT CTAT ATAA ATAA CGTG CTTC"
s4 = s.replace("A", "0").replace("C", "1").replace("G", "2").replace("T", "3")
print( ''.join(chr(int(c, 4)) for c in s4.split()) )
```

---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`TFCCTF{1_w1ll_g3t_th1s_4s_4_t4tt00_V3ry_s00n}`</div>


!!! نویسنده
    [mheidari98](https://github.com/mheidari98)


---
tags:
  - Crypto
  - quadratic residue
  - legendre symbol
---

## باقی مانده درجه دوم

در نظریه اعداد عدد صحیح $q$ باقی مانده درجه دوم یا quadratic residue می گوییم اگر عدد صحیح مانند $x$ وجود داشته باشد به طوری که:

$$
x^{2}\equiv q \pmod{n}
$$

در غیر اینصورت آن را غیر باقی مانده درجه دوم یا quadratic non-residue میخوانیم.

## خواص

- **پیمانه اول: اگر** $p$ یک پیمانه فرد اول باشد آنگاه دقیقا $\frac{p+1}{2}$ باقی مانده درجه دوم به پیمانه $p$ وجود دارد.

- **نماد Legendre**:‌ نماد Legendre یا ($\frac{a}{p}$) برای مشخص کردن این که آیا عدد $a$ یک باقیمانده درجه دوم به پیمانه $p$ هست یا خیر به کار می رود. اگر $a$  یک باقیمانده درجه دوم به پیمانه $p$ باشد آنگاه $\frac{a}{p} = ‌1$  می باشد در غیر این صورت برابر $\frac{a}{p} = ‌-1$ می باشد و اگر $a\equiv 0 \pmod{p}$ بود آنگاه $\frac{a}{p} = ‌0$ می باشد.

- **خواصی دیگر:** 

```
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue
```

## مثال

در نظر بگیرید $n=7$. اعداد صحیح $0,1,2,3,4,5,6$ همگی تمامی باقیمانده ممکن برای تقسیم بر 7 هستند.
حالا بیاید و بررسی کنیم کدامین از اینها باقی مانده درجه دوم هستند:

$$0^{2} \equiv 0 \equiv 0 \pmod{7}$$ 

$$1^{2} \equiv 1 \equiv 1 \pmod{7}$$ 

$$2^{2} \equiv 4 \equiv 4 \pmod{7}$$ 

$$3^{2} \equiv 9 \equiv 2 \pmod{7}$$ 

$$4^{2} \equiv 16 \equiv 2 \pmod{7}$$ 

$$5^{2} \equiv 25 \equiv 4 \pmod{7}$$ 

$$6^{2} \equiv 36 \equiv 1 \pmod{7}$$ 

بنابراین باقی مانده درجه دوم به پیمانه 7 اعداد 0,1,2 و 4 هستند.

--- 

!!! نویسنده
    [MohamadAli](https://github.com/w0h4w4d4li)
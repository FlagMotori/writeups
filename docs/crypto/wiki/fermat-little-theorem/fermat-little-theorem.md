---
tags:
  - Crypto
  - Fermat's little Theorem
  - Modular arithmetic
---

## قضیه Fermat's little

???+ note "قضیه Fermat's little"

    در نظریه اعداد این قضیه نشان میدهد که اگر $p$ عددی اول باشد آنگاه برای هر عدد صحیح $a$ عدد $a^{p} - a$ یک عدد صحیح مضربی از $p$ هست. اگر بخواهیم به صورت حساب پیمانه ای نمایش بدهیم داریم:

    $$
    a^{p}\equiv a \pmod{p}
    $$

## مثال

برای مثال اگر $a=2$ و $p=7$ آنگاه 

$$2^{7} - 2\equiv 126 \equiv 7 \times 18 \equiv 0 \pmod{7}$$ 

???+ tip "نکته مهم"

    در حالتی که $p$ و $a$ نسبت به اول باشند این قضیه معادل است با :

    $$
    a^{p-1}\equiv 1 \pmod{p}
    $$

    برای مثال اگر $a=2$ و $p=7$ آنگاه 

    $$2^{6} \equiv 64 \equiv 7 \times 9 + 1 \equiv 1 \pmod{7}$$ 

--- 

!!! نویسنده
    [MohamadAli](https://github.com/w0h4w4d4li)
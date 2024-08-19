## باقی مانده درجه دوم

???+ info "تعریف finite field یا فیلد متناهی"

    در حالتی که $p$ و $a$ نسبت به اول باشند این قضیه معادل است با :

    $$2^{6} \equiv 64 \equiv 7 \times 9 + 1 \equiv 1 \pmod{7}$$ 

در نظریه اعداد عدد صحیح $q$ باقی مانده درجه دوم یا quadratic residue می گوییم اگر عدد صحیح مانند $x$ وجود داشته باشد به طوری که:

$$
x^{2}\equiv q \pmod{n}
$$

در غیر اینصورت آن راه غیر باقی مانده درجه دوم یا quadratic non-residue میخوانیم.

## خواص
```
Quadratic Residue * Quadratic Residue = Quadratic Residue
Quadratic Residue * Quadratic Non-residue = Quadratic Non-residue
Quadratic Non-residue * Quadratic Non-residue = Quadratic Residue
```

## مثال

برای مثال اگر $a=2$ و $p=7$ آنگاه 

$$2^{7} - 2\equiv 126 \equiv 7 \times 18 \equiv 0 \pmod{7}$$ 


--- 

!!! نویسنده
    [تیم فلگ موتوری](https://github.com/flagmotori)


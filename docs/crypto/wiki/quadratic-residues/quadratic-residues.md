## باقی مانده درجه دوم

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

در نظر بگیرید $n=7$. اعداد صحیح $0,1,2,3,4,5,6$ همگی تمامی باقیمانده ممکن برای تقسیم بر ۷ هستند.
حالا بیاید و بررسی کنیم کدامین از اینها باقی مانده درجه دوم هستند:

$$0^{2} \equiv 0 \equiv 0 \pmod{7}$$ 

$$1^{2} \equiv 1 \equiv 1 \pmod{7}$$ 

$$2^{2} \equiv 4 \equiv 4 \pmod{7}$$ 

$$3^{2} \equiv 9 \equiv 2 \pmod{7}$$ 

$$4^{2} \equiv 16 \equiv 2 \pmod{7}$$ 

$$5^{2} \equiv 25 \equiv 4 \pmod{7}$$ 

$$6^{2} \equiv 36 \equiv 1 \pmod{7}$$ 

بنابراین باقی مانده درجه دوم به پیمانه 7 اعداد 0,1,2 و 4 هستند

--- 

!!! نویسنده
    [تیم فلگ موتوری](https://github.com/flagmotori)


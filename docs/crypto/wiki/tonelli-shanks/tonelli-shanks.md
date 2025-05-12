---
tags:
  - Crypto
  - tonelli-shanks
  - Modular arithmetic
---

## الگوریتم tonelli-shanks

در محاسبات پیمانه ای مسئله یافتن یک ریشه دوم به پیمانه یک عدد اول مانند $p$ را می توان به صورت یافتن یک عدد صحیح $x$ به گونه ای توصیف کرد که:

$$
x^{2}\equiv a \pmod{p}
$$

که در آن $a$ یک عدد صحیح و $p$ یک عدد اول است. برای هر عدد $a$ یک راه حل برای این معادله در پیمانه $p$ وجود ندارد. با این حال، هنگامی که یک راه حل وجود دارد، الگوریتم Tonneli-Shanks یک روش کارآمد برای یافتن آن ارائه می دهد.

??? warning "توجه کنید"

    این الگوریتم برای پیمانه های مرکب (غیر  اول) کار نمی کند. یافتن ریشه دوم برای پیمانه های مرکب از نظر محاسباتی معادل فاکتورگیری اعداد صحیح است. یعنی مسئله سختی است.

## پیاده سازی

```py linenums="1" title="example.py"
def legendre(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli(n, p):
    assert legendre(n, p) == 1, "not a square (mod p)"
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    if s == 1:
        return pow(n, (p + 1) // 4, p)
    for z in range(2, p):
        if p - 1 == legendre(z, p):
            break
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s
    t2 = 0
    while (t - 1) % p != 0:
        t2 = (t * t) % p
        for i in range(1, m):
            if (t2 - 1) % p == 0:
                break
            t2 = (t2 * t2) % p
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i
    return r

# test
n=41660815127637347468140745042827704103445750172002
p=100000000000000000000000000000000000000000000000577
r = tonelli(n, p)
print("n=%d, p=%d" % (n, p))
print("roots : %d, %d" % (r, p - r))
```

--- 

!!! نویسنده
    [MohamadAli](https://github.com/w0h4w4d4li)
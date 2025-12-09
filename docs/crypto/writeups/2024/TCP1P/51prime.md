---
tags:
  - TCP1PCTF
  - TCP1PCTF 2024
  - Crypto  
  - math
  - LLL
---


# چالش 51prime

در چالش کد زیر به ما داده شده است:

```py
from hashlib import sha512
from pwn import xor
from Crypto.Util.number import isPrime

assert p == a**51 + 51*b**51 and isPrime(p) and a > 0 and b > 0
print(hex(p)[2:])
print(xor(flag,sha512((str(a)+str(b)).encode()).digest()).hex())

# 1cec7c3ff93ca538e71f334e83d905eabd894729a1b515b89dc2392036bc7e5d59fad2c35dbb0a8903c8bb2e9cd5e4779a92d3f361eb1ce9fa2530c47881a8719763f828360138373ffa2ce627f8ccad08e9b5ead178c614f7899adc6a14fa33aa2216c463a04041e78cffa2c68963c6ff422a076bedd32236282eb3bd1b7ba870a3b1c8f639cd536cba329b10a6cf7b4ef78bd11052ff8a0d432fb6d3b221742aa1da6914876e94aca5abdaeef30acdfc90cbc621245ad288a634e8bdf4152ea8ed0062c872ace7b4011dc5743fa9c424413f4e3e8fa5c5513fd4a711141f2ef68c01177f78945db623ac6cc762a6813f11cc278a143ea657bf309e281ef59048a29f279c9ad8b37f221ac06242f577bba985a2aaec051d95391a9681f905472f4e7d1322da492639ee4a5ac776a476cece55f9dfb782c1ef869deed2226691d3157fbb6b131968ebfb1fe5bc1e44a158f1e2321c001355cc9cb3344f6b09b78d965a807cd60d58a9efbab8c6d4f75c8e5ac7c9cf0e5409b55bb2133129272685913be02166c6bffe3747ccd186b6c26fc9f09
# 43edcf6275293ce97d716f49875c4bdba37f6ab30f15a53f09b72bf3816edf6b92618fb56d569d911b2f6fe7a36d4a854022dddf671dc89b4800bc1605822aab72d3
```

در آن مقدار`p`از طریق معادله زیر بدست آمده و برای بدست آوردن پرچم مسابقه نیاز به`a` و `b`داریم اما این یک معادله چندجمله‌ای است. با این حال، با یک حقه و استفاده از جذر و جابه‌جایی می‌توان آن را به یک معادله خطی پیمانه‌ای تبدیل کرد:

$$
p = a^{51}+51.b^{51}
$$

طرفین در پیمانه $p$ محاسبه می‌کنیم:

$$
a^{51}+51.b^{51}  \equiv  0 \ (mod \ p) 
$$

$$
a^{51}\equiv -51.b^{51} 
$$


طرفین جذر 51 می گیریم:

$$
a \equiv  \sqrt[51]{-51}.b  \ ( mod \ p) 
$$

$$
a + \sqrt[51]{-51}.b - k.p = 0 
$$

$$
\begin{bmatrix}  \sqrt[51]{-51} \\  1 \end{bmatrix}.b + k.\begin{bmatrix} p \\  0 \end{bmatrix} = \begin{bmatrix} a \\  b \end{bmatrix}
$$

پس ماتریس مشبکه آن را می‌سازیم و با استفاده از LLL آن را حل می‌کنیم:

$$
\begin{bmatrix}
    \sqrt[51]{-51} &  p  \\
    1   &   0     \\
\end{bmatrix} \ \underrightarrow{LLL} \ \begin{bmatrix} a \\  b \end{bmatrix}
$$

!!! توجه warning 
    در این معادله پیمانه‌ای چون باقیمانده برابر 0 است و ضریب $a$ یک است، ماتریس آن به این شکل در آمده است. 



```py
from sage.all import *
from gmpy2 import iroot
from pwn import xor
from hashlib import sha512
proof.all(False)

cipher=bytes.fromhex("43edcf6275293ce97d716f49875c4bdba37f6ab30f15a53f09b72bf3816edf6b92618fb56d569d911b2f6fe7a36d4a854022dddf671dc89b4800bc1605822aab72d3")
p = 0x1cec7c3ff93ca538e71f334e83d905eabd894729a1b515b89dc2392036bc7e5d59fad2c35dbb0a8903c8bb2e9cd5e4779a92d3f361eb1ce9fa2530c47881a8719763f828360138373ffa2ce627f8ccad08e9b5ead178c614f7899adc6a14fa33aa2216c463a04041e78cffa2c68963c6ff422a076bedd32236282eb3bd1b7ba870a3b1c8f639cd536cba329b10a6cf7b4ef78bd11052ff8a0d432fb6d3b221742aa1da6914876e94aca5abdaeef30acdfc90cbc621245ad288a634e8bdf4152ea8ed0062c872ace7b4011dc5743fa9c424413f4e3e8fa5c5513fd4a711141f2ef68c01177f78945db623ac6cc762a6813f11cc278a143ea657bf309e281ef59048a29f279c9ad8b37f221ac06242f577bba985a2aaec051d95391a9681f905472f4e7d1322da492639ee4a5ac776a476cece55f9dfb782c1ef869deed2226691d3157fbb6b131968ebfb1fe5bc1e44a158f1e2321c001355cc9cb3344f6b09b78d965a807cd60d58a9efbab8c6d4f75c8e5ac7c9cf0e5409b55bb2133129272685913be02166c6bffe3747ccd186b6c26fc9f09
x = int(GF(p)(-51).nth_root(51))  # x is 51-th root of 51

# a=x*b % p --> (a-x*b) % p=0 ---> a - x*b+ k.p = 0 

M=Matrix([
[x, p],
[1, 0],
]).T

M=M.LLL()
a, b = M[0]
assert p == a**51 + 51*b**51

flag = xor(cipher, sha512((str(a)+str(int(b))).encode()).digest())
print(flag)
```

??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`TCP1P{prime_prime_prime_prime_prime_prime_prime_prime_prime_prime}`</div>



!!! نویسنده
    [HIGHer](https://twitter.com/HIGH01012) 

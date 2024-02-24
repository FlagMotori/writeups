---
tags:
  - PingCTF
  - PingCTF-2023
  - Misc
  - Random
---

[آرشیو چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/pingCTF/2023/misc/you_spin_me_round)

اینم مثل قبلی، یه تعداد beep و boop دریافت میکنیم و میتونیم سید رو تشخیص بدیم
```python linenums="1"
from pwn import *

p = remote("57.128.196.218", 20000)

p.recvuntil(b"\n\n")
s = p.recvline().decode()
a, b = s.count("BEEP"), s.count("BOOP")
p.recvuntil(b"Task")
p.recvuntil(b": ")
s = p.recvline().decode().strip()
split = s.split(' ')
for i in range(1_000_000):
    random.seed(i)
    if random.randint(1, 100) == int(a):
        if random.randint(1, 100) == int(b):
            if random.randint(100, 10000) == int(split[0]):
                if int(split[0]) // random.randint(1, 100) == int(split[4]):
                    p.sendline(str(int(split[0]) // int(split[4])).encode())
                    break

def task1():
    random.randint(100, 10000)
    return str(random.randint(1, 100)).encode()

def task2():
    random.randint(100000, 1000000000)
    return str(random.randint(1, 100000) / 100).encode()

def task3():
    x = random.randint(100000, 1000000000) / 100
    y = random.randint(1, 100000) / 100
    p1, p2 = str(x % y).split('.')
    ans = f"{p1}{p2[0]}.{p2[1:]}e-1"
    return ans.encode()

task = 1
p.sendline(task2())
p.sendline(task3())
for i in range(996):
    print(i, end='\r')
    t = random.randint(1, 3)
    p.sendline(eval(f"task{t}()"))

print(p.clean(2))
```

!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$تاریخ نگارش ۱۴۰۲/۱۲/۴
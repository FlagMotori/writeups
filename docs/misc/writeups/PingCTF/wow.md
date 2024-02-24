---
tags:
  - PingCTF
  - PingCTF-2023
  - Misc
  - Random
---

[آرشیو چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/pingCTF/2023/misc/wow)

به محض وصل شدن به سرور یه تعداد رندوم به سمت ما ارسال میشه که میتونیم با اون رندوم ها سید رو تشخیص بدیم و ادامه ماجرا =))
```python linenums="1"
from pwn import *
import random

a = remote("57.128.196.218", 20001)

a.sendline(b'y')
a.recvuntil(b'user_balance=')
def get_randoms(n: int):
    randoms = []
    while len(randoms) < n:
        a.sendline(b'1')
        for line in a.recvuntil(b'user_balance=').decode().split('\n'):
            if 'rolls' in line:
                randoms.append(line.split('rolls ')[1])
        randoms.append('END')
    return randoms

first = 100
rands = get_randoms(30)
correct = 0
for i in range(10_000_001):
    random.seed(i)
    for j in rands:
        if j == 'END':
            first = 100
        elif int(j) == random.randint(1, first):
            correct += 1
            first = int(j)
        else:
            correct = 0
    if correct > 10:
        break

def i_will_win(number = 100, user = 'Safa'):
    if user == 'Safa':
        user = 'opponent'
    else:
        user = 'Safa'
    a = random.randint(1, number)
    if a == 1:
        return False if user == 'Safa' else True
    return i_will_win(a, user)

balance = int(a.recvline().decode())
while balance < 10_000_000:
    opponent_balance = 10_000_000 + 50 - balance
    if i_will_win():
        print(balance)
        a.sendline(str(min(balance, opponent_balance)).encode())
        balance *= 2
    else:
        a.sendline(b'1')
        balance -= 1
        
print(a.clean(2))
```

!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)$~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$تاریخ نگارش ۱۴۰۲/۱۲/۴
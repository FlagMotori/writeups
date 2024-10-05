---
tags:
  - BackdoorCTF
  - BackdoorCTF-2023
  - Begineer
  - C
  - Random
---

[آرشیو چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/BackdoorCTF/2023/misc/Fruit_Basket)

```c linenums="1"
#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string>
#include <unistd.h>

int main()
{
    unsigned int v3; // eax
    char *fruits[10] = {"Apple", "Orange", "Mango", "Banana", "Pineapple", "Watermelon", "Guava", "Kiwi", "Strawberry", "Peach"};

    int i; // [rsp+Ch] [rbp-24h]

    v3 = time(0);
    srand(v3);

    usleep(4000000);

    for (i = 0; i <= 49; ++i)
    {
        printf("%s\n", fruits[rand() % 10]);
    }
    printf("cat flag.txt\n");
    return 0;
}
```
این کد که از رو سورس چلنج دراومده رو کامپایل میکنیم و چون سید رندوم روی تایم ست شده، رندوم های سمت سرور و کلاینت برابر ان

با دستور زیر اجرا میکنیم و به nc پایپ میکنیم
```bash
./main|nc 34.70.212.151 8006
```
---
!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)


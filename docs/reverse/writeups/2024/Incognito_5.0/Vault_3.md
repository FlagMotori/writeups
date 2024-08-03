# چالش Vault 3

🔗 [دانلود چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/Incognito/2024/rev/Vault_3)

## نگاه اولیه به سوال

در این سوال فقط به ما یک فایل با نام `challenge2` داده شده بود.
در ابتدا برای اینکه بفهمیم با چه چیزی روبرو هستیم دستور file رو روش اجرا میکنیم


```bash
file challenge2
challenge2: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=a3ba1b21304762fc03ba2e52b68d776218252022, for GNU/Linux 3.2.0, not stripped
```

## تحلیل استاتیک


خب مشابه سوال قبلی بهمون یک فایل باینری 64بیتی داده شده، برا همین در ابتدا سراغ تحلیل استاتیک میریم و به کمک سایت دوست داشتنی [dogbolt](https://dogbolt.org) سعی میکنیم برنامه رو دیکامپایل کنیم و بفهمیم برنامه مدنظر چه کاری انجام میده

طبق تجربه معمولا Hex-Rays(IDA Pro) دیکامپایل های بهتری خروجی میده، در نتیجه ابتدا به دیکامپایل آیدا نگاهی میندازیم و اگر بخشی از کد نامفهوم بود، به خروجی سایر دیکاپایلر ها نیز نگاهی میندازیم.   
خب پس بیاید به خروجی آیدا نگاهی بندازیم:


```c
__int64 __fastcall rotateChar(char a1, int a2)
{
  if ( a1 > 96 && a1 <= 122 )
    return (unsigned int)((a1 - 97 + a2) % 26 + 97);
  if ( a1 <= 64 || a1 > 90 )
    return (unsigned __int8)a1;
  return (unsigned int)((a1 - 65 + a2) % 26 + 65);
}

__int64 __fastcall encrypt(__int64 a1)
{
  __int64 result;
  int i;
  for ( i = 0; ; ++i )
  {
    result = *(unsigned __int8 *)(i + a1);
    if ( !(_BYTE)result )
      break;
    *(_BYTE *)(i + a1) = rotateChar(*(_BYTE *)(i + a1) ^ (unsigned __int8)(i % 4), 3);
  }
  return result;
}

_BOOL8 __fastcall checkFlag(const char *a1)
{
  char dest[128];
  char s2[16];
  __int64 v4;

  qmemcpy(s2, "leyh{V2z4x#3q^x\"", sizeof(s2));
  v4 = 0x7F56305B5D6C77LL;
  strncpy(dest, a1, 0x80uLL);
  encrypt((__int64)dest);
  return strncmp(dest, s2, 0x18uLL) == 0;
}

int __fastcall main(int argc, const char **argv, const char **envp)
{
  char v4[128];
  puts("Enter the flag:");
  if ( (unsigned int)__isoc99_scanf("%127s", v4) )
  {
    if ( checkFlag(v4) )
      puts("Congratulations! You've solved the challenge.");
    else
      puts("Incorrect flag. Try again!");
  }
  return 0;
}
```


خب از سورس کد میتوان دید که برنامه یک رشته ورودی از ما میگیره و پاس میده به تابع `checkFlag`  
اونجا ورودی ما به تابع `encrypt` پاس داده میشه و خروجیش با یک رشته خاص مقایسه میشه.  
تو تابع `encrypt` میاد رو رشته ورودی یکسری `xor` انجام میده و سپس پاس داده میشه به تابع `rotateChar`  
تابع `rotateChar` میاد کد `ascii` کارکتر ورودی رو بررسی میکنه و اگه حروف کوچیک یا بزرگ انگلیسی بود به میزان a2 شیفت میدهد.(مشابه رمزنگاری سزار)

حال ما رشته مورد انتظار پس از عملیات‌های بالا رو داریم، درنتیجه کافیست تمام مراحل بالا رو معکوس پیش برویم تا به رشته ورودی ابتدای کار برسیم   
ولی پیش از آن، رشته مورد انتظار تو دیکامپایلر آیدا پرو اندکی مبهمه، درنتیجه به کمک دیکامپایلر BinaryNinja رشته دقیق نهایی رو بدست میاریم

```c
uint64_t checkFlag(char* arg1)
{
    int64_t var_28;
    __builtin_strcpy(&var_28, "leyh{V2z4x#3q^x\"wl][0V\x7f");
    void var_a8;
    strncpy(&var_a8, arg1, 0x80);
    encrypt(&var_a8);
    int32_t rax;
    rax = strncmp(&var_a8, &var_28, 0x18) == 0;
    return rax;
}
```


## حل چالش


```python
def revRotateChar(c, num):
    if 96<c and c<=122:
        return (c - 97 - num) % 26 + 97
    if 64<c and c<=90:
        return (c - 65 - num) % 26 + 65
    return c

s = b"leyh{V2z4x#3q^x\"wl][0V\x7f"
for i, c in enumerate(s):
    print(chr(revRotateChar(c, 3)^(i % 4)), end='')
```


---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`ictf{R0t4t!0n_w!th_X0R}`</div>


!!! نویسنده
    [mheidari98](https://github.com/mheidari98)


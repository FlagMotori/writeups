# چالش Vault 2

🔗 [دانلود چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/Incognito/2024/rev/Vault_2)

## نگاه اولیه به سوال

در این سوال فقط به ما یک فایل با نام `challenge1` داده شده بود.
در ابتدا برای اینکه بفهمیم با چه چیزی روبرو هستیم دستور file رو روش اجرا میکنیم

```bash
$ file challenge1
challenge1: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d15aa18d88517442ed4cf7a958d61093c455c645, for GNU/Linux 3.2.0, not stripped
```


## تحلیل استاتیک


خب بهمون یک فایل باینری 64بیتی داده شده، برا همین در ابتدا سراغ تحلیل استاتیک میریم و به کمک سایت دوست داشتنی [dogbolt](https://dogbolt.org) سعی میکنیم برنامه رو دیکامپایل کنیم و بفهمیم برنامه مدنظر چه کاری انجام میده

طبق تجربه معمولا Hex-Rays(IDA Pro) دیکامپایل های بهتری خروجی میده، در نتیجه ابتدا به دیکامپایل آیدا نگاهی میندازیم و اگر بخشی از کد نامفهوم بود، به خروجی سایر دیکاپایلر ها نیز نگاهی میندازیم.   
خب پس بیاید به خروجی آیدا نگاهی بندازیم:



```c
__int64 __fastcall mysteryFunction(__int64 a1)
{
  __int64 result;
  int i;

  for ( i = 0; ; ++i )
  {
    result = *(unsigned __int8 *)(i + a1);
    if ( !(_BYTE)result )
      break;
    *(_BYTE *)(i + a1) ^= (unsigned __int8)(i % 5) + 1;
  }
  return result;
}

_BOOL8 __fastcall checkFlag(const char *a1)
{
  char dest[128];
  char s2[32];
  qmemcpy(s2, "hawb~w6q5dcn0[n2", 16);
  *(_QWORD *)&s2[15] = 0x7F73357C5C7B32LL;
  strncpy(dest, a1, 0x80uLL);
  mysteryFunction((__int64)dest);
  return strncmp(dest, s2, 0x17uLL) == 0;
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
اونجا ورودی ما به تابع `mysteryFunction` پاس داده میشه و خروجیش با یک رشته خاص مقایسه میشه.  
تو تابع `mysteryFunction` میاد رو رشته ورودی یکسری xor انجام میده و خروجیش برگردونده میشه.  


متاسفانه تو خروجی IDA رشته‌ای که در انتها مقایسه میشه درست نمایش داده نشده و میتوان از خروجی BinaryNinja کمک گرفت.
```c
uint64_t checkFlag(char* arg1)
{
    int64_t var_28;
    __builtin_strcpy(&var_28, "hawb~w6q5dcn0[n2{\\|5s\x7f");
    void var_a8;
    strncpy(&var_a8, arg1, 0x80);
    mysteryFunction(&var_a8);
    int32_t rax;
    rax = strncmp(&var_a8, &var_28, 0x17) == 0;
    return rax;
}
```

## حل چالش


در انتها به سادگی با کد پایتونی زیر میتونیم فلگ رو بدست در بیاریم

```python
#s = b"hawb~w6q5dcn0[n" + bytes.fromhex('7F73357C5C7B32')[::-1]
s = b"hawb~w6q5dcn0[n2{\\|5s\x7f"
for i, c in enumerate(s):
    print(chr(c^(i%5+1) ), end='')
```



---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`ictf{v4r1abl3_k3y_x0r}`</div>


!!! نویسنده
    [mheidari98](https://github.com/mheidari98)


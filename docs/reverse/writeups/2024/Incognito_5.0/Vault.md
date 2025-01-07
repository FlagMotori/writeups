# چالش Vault 

🔗 [دانلود چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/Incognito/2024/rev/Vault)


## نگاه اولیه به سوال


در این سوال فقط به ما یک فایل با نام `challenge0` داده شده بود.
در ابتدا برای اینکه بفهمیم با چه چیزی روبرو هستیم دستور file رو روش اجرا میکنیم

```bash
$ file challenge0
challenge0: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=050a91a2a787ea9b21439b9cae80e47848c472f7, for GNU/Linux 3.2.0, not stripped
```

## تحلیل استاتیک


 خب بهمون یک فایل باینری 64بیتی داده شده، برا همین در ابتدا سراغ تحلیل استاتیک میریم و به کمک سایت دوست داشتنی [dogbolt](https://dogbolt.org) سعی میکنیم برنامه رو دیکامپایل کنیم و بفهمیم برنامه مدنظر چه کاری انجام میده.

??? info "دیکامپایلر چیست؟"

    یک دیکامپایلر برعکس یک کامپایلر عمل می کند! باینری ها را می گیرد و آنها را به کد منبع تبدیل می کند (با درجات مختلف موفقیت بسته به کامپایلر، تنظیمات کامپایلر، زبان، معماری، پیچیدگی و بسیاری عوامل دیگر).

معمولا طبق تجربه Hex-Rays دیکامپایل های بهتری میده، در نتیجه بیاید به خروجیش نگاهی بندازیم:

```c
_DWORD ascii_values_1[26] = {105, 99, 116, 102, 123, 119, 101, 108, 99, 48, 109, 101, 95, 116, 48, 95, 114, 101, 118, 51, 114, 115, 49, 110, 103, 125 };
_BYTE flagArray_0[32];

_BYTE *flag()
{
  int i;
  for ( i = 0; i < 26; ++i )
    flagArray_0[i] = ascii_values_1[i];
  flagArray_0[26] = 0;
  return flagArray_0;
}

int __fastcall main(int argc, const char **argv, const char **envp)
{
  const char *v3;
  const char *v4;
  char s1[112];
  printf("Enter the secret code: ");
  __isoc99_scanf("%99s", s1);
  v3 = flag();
  if ( !strcmp(s1, v3) )
  {
    puts("Access Granted!");
    v4 = flag();
    puts(v4);
  }
  else
  {
    puts("Access Denied!");
  }
  return 0;
}
```

## حل چالش



خب از سورس کد میتوان دید که برنامه از ما یک رشته ورودی میگیره و با خروجی تابع flag مقایسه میکنه.
در ادامه بسادگی با کد پایتونی زیر میتونیم فلگ رو در بیاریم

```python
a = [105, 99, 116, 102, 123, 119, 101, 108, 99, 48, 109, 101, 95, 116, 48, 
     95, 114, 101, 118, 51, 114, 115, 49, 110, 103, 125]
print(''.join(map(chr, a)))
```


---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`ictf{welc0me_t0_rev3rs1ng}`</div>


!!! نویسنده
    [mheidari98](https://github.com/mheidari98)


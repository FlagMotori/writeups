#  رایتاپ‌های تیم فلگ موتوری 

ما برای سایتمون از **MkDocs** تم **material** استفاده میکنیم.

برای بالا اوردن سایت روی سیستم خودتون از دستورات زیر استفاده کنید. 

```console
# 1. clone
git clone https://github.com/FlagMotori/writeups.git
# 2. requirements
pip install -r requirements.txt
# generate static file in site/
mkdocs build
# deploy at http://127.0.0.1:8000
mkdocs serve
```

> [!TIP]
> برای تست لوکال، وقتی فایل مارک داون تغییر کنه، خودکار سایت آپدیت میشه


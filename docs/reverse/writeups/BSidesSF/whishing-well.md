---
tags:
  - BSidesSF
  - BSidesSF-2024
  - Reverse
  - Android
---

اگه رایتاپ قبلی رو خوب خونده باشین، میدونید که اولین کار در مواجه با یه فایل apk، بازکردنش تو JadX هست

پس سر این فایل هم همین بلا رو میاریم =))

مجددا از روی AndroidManifest.xml پکیج‌نیم برنامه رو پیدا میکنیم و میریم تو کلاسش سرک بکشیم

MainActivity که کار خاصی انجام نمیده و صرفا تابع publishWish رو با یه ورودی که از کاربر گرفته اجرا میکنه

![wishing-well-1](wishing-well-1.png)

و اما کلاس PubSub

![wishing-well-2](wishing-well-2.png)

این کلاس همونطور که از اسمش هم پیداست، وظیفه publish-subscribe رو داره

خیلی خلاصه بخوام بگم، PubSub یه خدمتیه برای انتقال یه پیام بین دیوایس ها به واسته گوگل هست

بعضی از نوتیفیکیشن ها هم از همین طریق ارسال میشن و مباحثی مثل تاپیک بندی و ... هم توشون وجود داره

اگه میخواید درباره pub/sub بیشتر بخونید، رو [این لینک کلیک کنید](https://cloud.google.com/pubsub/docs/overview)

بریم سراغ ادامه چالش

گوگل برای api call زدن به سرویساش (ماشالله چقدر هم زیادن و خدا بیشترش کنه) یه ابزار cli ساخته به اسم gcloud که خیلی کار ما رو راحت میکنه

قبل از این که برم سراغش به اینم اشاره کنم که همونطور که تو عکس هم مشخصه، یه فایل key.json هم وجود داره که برا api call ها نیازش داریم و میریم از تو فولدر assets برش‌میداریم

```json
{
  "type": "service_account",
  "project_id": "bsides-sf-ctf-2023",
  "private_key_id": "ca50571bf6de0a614a66ede75f325969cc425308",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQDUjDLTA2b2iX1u\n5wYUJRv145yYtFNrwM0gCWuFXUNt99d/aZTU965U8W0OFQF1P82pCGHcOWiSDJCk\nyup+1bLG40n51jqBAk4UzUS2fQt9YvWK0QKjAJ3mOnDKs8BKcrUIAI1yEUgN3Ygj\ns92HZd15XegN+PtOfDVr+Fds+xsf0vnVUjJRJTLglyOLc4a0GepprdxEnjxugTJY\nHGCN0yB6I1Cc5tkNnwo4+DWxcsuNjm3zjmR9oa5+032CuV/uPED7KoeQ+4ZP6Ics\nRmmIeOH+aZ2niIG1I6e+lzK0WIpCHI/1SLwEa65OTMdubVmUIgDAQKahV2jx3P6h\nCuRbe9dzAgMBAAECggEAPVTjSY5+xH8yCbFySJfYtKBkTJAkTkCJMEhnlUkvLulI\nbsSppLZ/wJUV0e1vyUSK9M6tZl3Ode5YQqUm+0hw2QE3FHej1Bw1Kb19qWb1zM2k\natUa/Kwt5ARTDbrGrvTglhmKtzKTZyTYpuy87NgRC3d0gaup4KDozWoQ2CqxTgIN\nXCi/6TmLX4jLUQAf0eTiiKrAJCZXiOVLxJ1nrzZIX9GujD1ihcKvhVpoRQOK4dMG\n+TZirz7qqNXFrdV/Q31XdP2rSpOoKUUNSYYGDHicGSJxyt93igxawscIPSk3clBx\nVC2gLTmAKYD0mS9icLOhcTYp0R76/9wy19iHeA1jMQKBgQDubxAklGVUH7SOKggL\nsUXTDbZpC6HrcYuW+uPF/RJuocgnSd6bYIZUbbVRQfmltzVDvcGovZc4uKlCesMV\nOVPTo9RJjXg4RH8iuPQk1lJsfAfjrOrfbrXL/9kdJrqn0n3cxF2uwoKU0k8dEw9r\nBBiqOi/q1oxl5QRe5N/vzE5nCQKBgQDkNOnwlCi74X5iS1kxv3+8XnQdpHaus8RB\nVIOwota2LPZRkjlpLrKmcUEOb3LeNSLiRVJp4f9OiI1C0fy/aP9Kv9dvu223fGqd\n4W2JsBH0xmX27qU8dKVuRNETlnNGae+TTYXNlLwfw/dNOEP1kt1hjv3cyq/9gIuI\nwxERcIgNmwKBgGeTHWsWf5H0l+VtwsL5hgBxo3ysTfFOCLpUUF+wWLJwWtceUrIi\nUxgX9DzRMRZYqK29n4OioC9GoFg9pcLxfUWhlFVDPCcNMkEuIPhjlbiEhJTVh835\ndMWiZXkxWsIOQRiGwL9qxXjKhw11Oyxcwi4oSqpz+tdEjgp+1/x+PsypAoGAO1sf\n9fkzVxrhmoNqoavjd4VBwmwCipIrW6q1zf2sxxmOv8y+rgL9aJlQiIaoY++CMURC\nmVO06iJOS7D+gnK25CRdzqv7b5wmxwXZTdTD9tybrMyJod3dIX84ulWJiikHrVKe\nmMg03jZEXoth8b/PYQ6mLQVzHQaQRHQoPlb8rD0CgYBIVU23/bcYoS7kRo8utxDy\nWraoJvBXUQ6g9jGN4yX4IuRIsHcsvEQHI+cW0m1lNMLycKq5lQYra6ZuZL4KVbyn\nKcOOP6qownLnx0hPgbAHDTyD3kSSnvlaTWrnSAuoy/exrMrZ9LPVXVgTz/uwa/Zj\n3I3W/S3b2d8WQomqCbs6Sg==\n-----END PRIVATE KEY-----\n",
  "client_email": "wishing-well-pubsub@bsides-sf-ctf-2023.iam.gserviceaccount.com",
  "client_id": "118295537994451394759",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/wishing-well-pubsub%40bsides-sf-ctf-2023.iam.gserviceaccount.com",
  "universe_domain": "googleapis.com"
}
```

بعد از [نصب ابزار gcloud](https://cloud.google.com/sdk/docs/install)
میریم که فایل key.json رو بهش بدیم

```bash
gcloud auth activate-service-account --key-file=key.json
```

بعد نوبت به api call هامون میرسه

من خیلی دوست داشتم یه جایی میبود که میتونستم تمام scope هایی که این کردنشیال بهشون دسترسی داره رو پیدا کنم اما خو نشد و خود این که (بفهمی به کجا دسترسی داری) هم یه دسترسی خاص داشت که این دسترسی به اکانت داده نشده بود =))))

پس در قدم اول یه پیام پوش کردیم سمت PubSub که بفهمیم همه چی اوکیه

```bash
$ gcloud pubsub topics publish wishing-well --message=flag --project=bsides-sf-ctf-2023

messageIds:
- '11008165207535342'
```

همه چی درسته

حالا اما فلگ کجاست، از اینجا به بعد، چلنج خیلی guessy (حدسی) میشه و شما باید از غیب بفهمید که با همین کردنشیال، میتونید پیام ها رو بخونید و با این دستور، فلگ رو دریافت کنید

```bash
gcloud pubsub subscriptions pull wishing-well-sub --project=bsides-sf-ctf-2023
```

میدونم خیلی سوال دارید

منم خیلی سوال داشتم اما کسی نبود ازش بپرسم :joy:

به هر حال
بعد از زدن دستور، فلگ رو در چنین قالبی به ما نشون میده

```bash
┌────────────────────────────────────────────────────────┬───────────────────┬──────────────┬────────────┬──────────────────┬──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                          DATA                          │     MESSAGE_ID    │ ORDERING_KEY │ ATTRIBUTES │ DELIVERY_ATTEMPT │                                                                                                ACK_ID                                                                                                │
├────────────────────────────────────────────────────────┼───────────────────┼──────────────┼────────────┼──────────────────┼──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ {"data": {"message": "CTF{W1sh3s-publish3d-gr4nt3d}"}} │ 11104663640891080 │              │            │                  │ BhYsXUZIUTcZCGhRDk9eIz81IChFEgEIFAV8fXdbS3VdXn1oUQ0Zcn1gfTxeRQJTR1F6DVEfC2JcTkQHSf3MpvxXV0tbEgACQVV4XF0fDWBVXXUPUSWew4fWtuPUMBs-faOri9otLcz_opY1ZiI9XxJLLD5-KTBFQV5AEkwiBURJUytDCypYEU4EISE-MD5FU0RQ │
└────────────────────────────────────────────────────────┴───────────────────┴──────────────┴────────────┴──────────────────┴──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`CTF{W1sh3s-publish3d-gr4nt3d}`</div>


!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)


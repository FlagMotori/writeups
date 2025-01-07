---
tags:
  - PingCTF
  - PingCTF-2023
  - Misc
  - Game_Hacking
  - Random
---

[آرشیو چلنج](https://github.com/sajjadium/ctf-archives/tree/main/ctfs/pingCTF/2023/misc/ping_arcade)

با ریورس های فراوون میرسیم به یه نوع ساخت رندوم که خوشبختانه پروژه پایتون هم دارن
تو این لینک

https://github.com/mobaradev/UnifiedRandom

```python linenums="1"
import random
import requests
import UnifiedRandom

headers = {
    "User-Agent": "UnityPlayer/2022.3.12f1 (UnityWebRequest/1.0, libcurl/8.1.1-DEV)",
    "X-Unity-Version": "2022.3.12f1",
}
code = requests.get(
    "https://ping-arcade.knping.pl/start-game", headers=headers
).json()["accessCode"]
t = []
rand = UnifiedRandom(code)
randb = UnifiedRandom(code)
randc = UnifiedRandom(code)
for i in range(64):
    pulse = rand.get_number(0, 25) / 100.0
    rate = randb.get_number(8, 25) / 100.0
    block_index = randc.get_number(0, 5)
    t.append(rate * block_index + pulse)

times = "-".join(list(map(str, t)))
print(
    requests.post(
        "https://ping-arcade.knping.pl/verify-game",
        headers=headers,
        # proxies=proxies,
        data={
            "accessCode": code,
            "times": times,
            "controlNumber": randc.get_number(0, randc.get_number(0, 10000)) * 1.25 * 64,
        },
    ).json()
)
```

!!! نویسنده
    [SafaSafari](https://twitter.com/SafaSafari3)


---
tags:
  - BackdoorCTF
  - BackdoorCTF-2023
  - Reverse
  - Android
  - Frida
  - Hooking
---

با هوک کردن تابعی که تو آدرس `0x23820` وجود داره، میتونیم به تیکه های فلگ دست پیدا کنیم
```js linenums="1"
var awaitForCondition = function (callback) {
  var int = setInterval(function () {
    var addr = Module.findBaseAddress("libsl4ydroid.so");
    if (addr) {
      console.log("SO Address found:", addr);
      clearInterval(int);
      callback(addr);
      return;
    }
  }, 0);
};
awaitForCondition(function (baseAddr) {
  Interceptor.attach(baseAddr.add(0x23820), {
    onEnter: function(args) {
      console.log(args[0].readUtf8String())
  },

  });
  Interceptor.flush();
});
```
با ابزار فریدا میتونیم هوک رو انجام بدیم
```bash
frida -U -f com.backdoor.sl4ydroid -l Sl4ydroid.js
```
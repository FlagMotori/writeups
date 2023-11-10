---
icon: fontawesome/regular/flag 
---

# سخن آغازین
به صفحه رایتاپ‌های تیم **فلگ موتوری** خوش آمدید. 
در حال حاضر، این **نسخه آزمایشی** صفحه رایتاپ‌های اعضا تیم است. امیدواریم که این سایت گامی هرچند اندک در جهت ارتقاء دانش و آگاهی علاقه‌مندان به حوزه امنیت سایبر در این سرزمین باشد.

امروزه بسیاری از رایتاپ‌ها در حوزه امنیت اغلب به زبان انگلیسی نوشته و منتشر می‌شوند. از آنجایی که ممکن است مطالعه محتوای انگلیسی  برای بسیاری از افراد دشوار باشد، تصمیم گرفتیم رایتاپ‌ها را به زبان فارسی منتشر کنیم تا مخاطبین فارسی زبان فرایند حل چالش‌های مسابقات CTF را بهتر درک کنند. ما در تیم فلگ موتوری بر این باوریم که ارائه رایگان این رایتاپ‌ها و در دسترس قرار دادن آن ها برای همگان، می‌تواند کمبود منابع فارسی در زمینه امنیت سایبری را تا حدی جبران کند.
بنابراین، کوشیدیم تا بستری جذاب را برای خواندن رایتاپ فراهم کنیم. بدین منظور امکان سفارشی‌سازی رنگ‌ها در سایت تعبیه شده تا  تجربه متفاوتی از مطالعه رایتاپ بر اساس سلیقه شخصی خود شکل دهید.

##  انواع زمینه‌های رنگی  

برای ایجاد تنوع در نمایش سایت و لذت بیشتر از خواندن رایتاپ، می‌توان رنگ‌های سه بخش زمینه‌ای سایت را تغییر داد. که در ادامه به آن‌ها اشاره شده است.

### ۱_ روشن و تاریک بودن پس‌زمینه

با استفاده از این ویژگی می‌توانید براساس تنظیمات مرورگر و سیستم، به طور خودکار و یا به صورت دستی بین زمینه‌های روشن و تاریک  جابجا شوید.

<div class="tx-switch">
<button data-md-color-scheme="default"><code>Default</code></button>
<button data-md-color-scheme="slate"><code>Slate</code></button>
</div>
<script>
  var buttons = document.querySelectorAll("button[data-md-color-scheme]")
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorScheme = this.dataset.mdColorScheme;
      localStorage.setItem("data-md-color-scheme",this.dataset.mdColorScheme);
    })
  })
</script>

### ۲_ رنگ‌های قالب اصلی

برای تغییر رنگ اصلی قالب اصلی روی بلوک رنگ کلیک کنید.

<div class="tx-switch">
<button data-md-color-primary="red"><code>Red</code></button>
<button data-md-color-primary="pink"><code>Pink</code></button>
<button data-md-color-primary="purple"><code>Purple</code></button>
<button data-md-color-primary="deep-purple"><code>Deep Purple</code></button>
<button data-md-color-primary="indigo"><code>Indigo</code></button>
<button data-md-color-primary="blue"><code>Blue</code></button>
<button data-md-color-primary="light-blue"><code>Light Blue</code></button>
<button data-md-color-primary="cyan"><code>Cyan</code></button>
<button data-md-color-primary="teal"><code>Teal</code></button>
<button data-md-color-primary="green"><code>Green</code></button>
<button data-md-color-primary="light-green"><code>Light Green</code></button>
<button data-md-color-primary="lime"><code>Lime</code></button>
<button data-md-color-primary="yellow"><code>Yellow</code></button>
<button data-md-color-primary="amber"><code>Amber</code></button>
<button data-md-color-primary="orange"><code>Orange</code></button>
<button data-md-color-primary="deep-orange"><code>Deep Orange</code></button>
<button data-md-color-primary="brown"><code>Brown</code></button>
<button data-md-color-primary="grey"><code>Grey</code></button>
<button data-md-color-primary="blue-grey"><code>Blue Grey</code></button>
<button data-md-color-primary="white"><code>White</code></button>
</div>
<script>
  var buttons = document.querySelectorAll("button[data-md-color-primary]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorPrimary = this.dataset.mdColorPrimary;
      localStorage.setItem("data-md-color-primary",this.dataset.mdColorPrimary);
    })
  })
</script>

### ۳_  رنگ های مربوط تاکید
برای تغییر رنگ بخش‌های تاکیدی مانند عبور ماوس از روی لینکها و برچسب‌ها، روی بلوک رنگی دلخواه خود در این بخش کلیک کنید.

<div class="tx-switch">
<button data-md-color-accent="red"><code>Red</code></button>
<button data-md-color-accent="pink"><code>Pink</code></button>
<button data-md-color-accent="purple"><code>Purple</code></button>
<button data-md-color-accent="deep-purple"><code>Deep Purple</code></button>
<button data-md-color-accent="indigo"><code>Indigo</code></button>
<button data-md-color-accent="blue"><code>Blue</code></button>
<button data-md-color-accent="light-blue"><code>Light Blue</code></button>
<button data-md-color-accent="cyan"><code>Cyan</code></button>
<button data-md-color-accent="teal"><code>Teal</code></button>
<button data-md-color-accent="green"><code>Green</code></button>
<button data-md-color-accent="light-green"><code>Light Green</code></button>
<button data-md-color-accent="lime"><code>Lime</code></button>
<button data-md-color-accent="yellow"><code>Yellow</code></button>
<button data-md-color-accent="amber"><code>Amber</code></button>
<button data-md-color-accent="orange"><code>Orange</code></button>
<button data-md-color-accent="deep-orange"><code>Deep Orange</code></button>
</div>
<script>
  var buttons = document.querySelectorAll("button[data-md-color-accent]");
  Array.prototype.forEach.call(buttons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorAccent = this.dataset.mdColorAccent;
      localStorage.setItem("data-md-color-accent",this.dataset.mdColorAccent);
    })
  })
</script>

<style>
button[data-md-color-accent]> code {
    background-color: var(--md-code-bg-color);
    color: var(--md-accent-fg-color);
  }
button[data-md-color-primary] > code {
    background-color: var(--md-code-bg-color);
    color: var(--md-primary-fg-color);
  }
button[data-md-color-primary='white'] > code {
    background-color: var(--md-primary-bg-color);
    color: var(--md-primary-fg-color);
  }
button[data-md-color-accent],button[data-md-color-primary],button[data-md-color-scheme]{
    width: 8.4rem;
    margin-bottom: .4rem;
    padding: 2.4rem .4rem .4rem;
    transition: background-color .25s,opacity .25s;
    border-radius: .2rem;
    color: #fff;
    font-size: .8rem;
    text-align: left;
    cursor: pointer;
}
button[data-md-color-accent]{
  background-color: var(--md-accent-fg-color);
}
button[data-md-color-primary]{
  background-color: var(--md-primary-fg-color);
}
button[data-md-color-scheme='default']{
  background-color: hsla(0, 0%, 100%, 1);
}
button[data-md-color-scheme='slate']{
  background-color: var(--md-default-bg-color);
}
button[data-md-color-accent]:hover, button[data-md-color-primary]:hover {
    opacity: .75;
}
</style>
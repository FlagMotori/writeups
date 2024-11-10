# شخصی‌سازی

در این قسمت می‌توانید با استفاده از گزینه‌های تعبیه شده، برخی از قسمت‌های سایت را برای خود شخصی‌سازی کنید.
 
##  انواع زمینه‌های رنگی 

### ۱_ روشن و تاریک بودن پس‌زمینه

با استفاده از این ویژگی می‌توانید براساس تنظیمات مرورگر و سیستم، به طور خودکار یا به صورت دستی بین زمینه‌های روشن و تاریک جابجا شوید.

<div class="tx-switch">
  <button class="btn-default" data-md-color-scheme="default"><code>Light</code></button>
  <button class="btn-slate" data-md-color-scheme="slate"><code>Dark</code></button>
</div>
<script>
  var schemeButtons = document.querySelectorAll("button[data-md-color-scheme]");
  Array.prototype.forEach.call(schemeButtons, function(button) {
    button.addEventListener("click", function() {
      document.body.dataset.mdColorScheme = this.dataset.mdColorScheme;
      localStorage.setItem("data-md-color-scheme", this.dataset.mdColorScheme);
    });
  });
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

### ۳_  رنگ‌های تاکیدی 
برای تغییر رنگ بخش‌های تاکیدی مانند عبور ماوس از روی لینک‌ها و برچسب‌ها، روی بلوک رنگی دلخواه خود در این بخش کلیک کنید.

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



## تغییر خط نوشتاری
برای تغییر Font می‌توانید از هریک از گزینه‌های زیر استفاده کنید.


<div class="tx-switchs">
  <button data-md-font-family="Nazanin" style="text-align: right;"><code>نازنین</code></button>
  <button data-md-font-family="Gandom" style="text-align: right;"><code>گندم (پیش‌فرض)</code></button>
  <button data-md-font-family="Diplomat" style="text-align: right;"><code>دیپلمات</code></button>
  <button data-md-font-family="Irsans" style="text-align: right;"><code>ایران‌سنس</code></button>
  <button data-md-font-family="Yekan" style="text-align: right;"><code>یکان</code></button>
  <button data-md-font-family="Samim" style="text-align: right;"><code>صمیم</code></button>
  <button data-md-font-family="Dirooz" style="text-align: right;"><code>دیروز</code></button>
  <button data-md-font-family="Traffic" style="text-align: right;"><code>ترافیک</code></button>
</div>

<script>
  // Set initial fonts for each button and handle button click events
  document.addEventListener("DOMContentLoaded", function() {
    var buttons = document.querySelectorAll("button[data-md-font-family]");
    var savedFont = localStorage.getItem("data-md-font-family");

    buttons.forEach(button => {
      var fontFamily = button.dataset.mdFontFamily;
      button.style.fontFamily = fontFamily; // Set button's own font on load
      button.querySelector("code").style.fontFamily = fontFamily; // Set font for <code> within button

      // Highlight selected button on page load if it matches saved font
      if (fontFamily === savedFont) {
        button.classList.add("selected");
        document.body.style.fontFamily = savedFont + ", sans-serif"; // Apply saved font to body
      }

      // On click, change the font for the body and highlight the selected button
      button.addEventListener("click", function() {
        document.body.style.fontFamily = fontFamily + ", sans-serif";
        localStorage.setItem("data-md-font-family", fontFamily);

        // Remove 'selected' class from all buttons and add it to the clicked one
        buttons.forEach(btn => btn.classList.remove("selected"));
        button.classList.add("selected");
      });
    });
  });
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
button[data-md-color-accent],button[data-md-color-primary],button[data-md-color-scheme],button[data-md-font-family]{
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
button[data-md-scheme='default']{
  background-color: hsla(0, 0%, 100%, 1);
}
button[data-md-scheme='slate']{
  background-color: var(--md-default-bg-color);
}
button[data-md-color-accent]:hover, button[data-md-color-primary]:hover {
    opacity: .75;
}
</style>

window.MathJax = {
    tex2jax: {
      inlineMath: [ ["\\(","\\)"] ],
      displayMath: [ ["\\[","\\]"] ]
    },
    TeX: {
      TagSide: "right",
      TagIndent: ".8em",
      MultLineWidth: "85%",
      equationNumbers: {
        autoNumber: "AMS",
      },
      unicode: {
        fonts: "STIXGeneral,'Arial Unicode MS'"
      }
    },
    showProcessingMessages: false,
    messageStyle: "none"
  };
window.addEventListener('load', function() { 
    var p=localStorage.getItem("data-md-color-primary");
    if (p){
        document.body.setAttribute('data-md-color-primary',p);
    }
    var a=localStorage.getItem('data-md-color-accent');
    if (a){
        document.body.setAttribute('data-md-color-accent',a);
    }
    var s = localStorage.getItem('data-md-color-scheme');
    if (s) {
        document.body.setAttribute('data-md-color-scheme', s);
    }
}, false);


document.addEventListener("DOMContentLoaded", function () {
  // Check if a font choice is saved in localStorage and apply it
  var savedFont = localStorage.getItem("data-md-font-family");
  if (savedFont) {
    document.documentElement.style.setProperty('--md-text-font', savedFont);
  }
});


var fontButtons = document.querySelectorAll("button[data-md-font-family]");
Array.prototype.forEach.call(fontButtons, function(button) {
    button.addEventListener("click", function() {
        document.documentElement.style.setProperty('--md-text-font', this.dataset.mdFontFamily);
        localStorage.setItem("data-md-font-family", this.dataset.mdFontFamily);
    });
});


pangu.spacingPageBody();
---
tags:
  - Crypto
  - modular binomials
  - Modular arithmetic
---

## دو جمله ای پیمانه ای
 
دو جمله ای پیمانه ای یک مسئله ریاضی است که در آن یک عبارت دو جمله ای از شکل:

$$ x \equiv (a+b)^e \pmod{N} $$

که  $a$ و $b$ اعداد صحیح و عدد صحیح مثبت $e$ به عنوان نما و عدد صحیح مثبت $N$ به عنوان پیمانه میباشد.

  
## جستجو p و q

مسئله دو جمله ای پیمانه ای می تواند به شکل زیر باشد:

$$ c_1 \equiv (a_1 \cdot p + b_1 \cdot q )^{e_1} \pmod{N} $$

$$ c_2 \equiv (a_2 \cdot p + b_2 \cdot q )^{e_2} \pmod{N} $$
  
که   $c_1$ , $c_2$ , $a_1$, $a_2$, $b_1$, $b_2$, $e_1$, $e_2$, $N$ داده شده  و  $N=p \times q$ و  هدف یافتن $p$ و $q$ است.

در ابتدا میایم و $c_1$ رو به توان $e_2$ میرسونیم:

$$
{c_1‌}^{e_2} \equiv (a_1 \cdot p + b_1 \cdot q )^{e_1 \cdot e_2} \pmod{N} 
$$

از طرفی با توجه به قضیه دو جمله ای داریم:

$$
{c_1‌}^{e_2} \equiv (a_1 \cdot p)^{e_1 \cdot e_2} + (b_1 \cdot q )^{e_1 \cdot e_2} \pmod{N} 
$$

حالا میایم و دو طرف رو در ${a_1}^{-e_1 \cdot e_2}$ ضرب میکنیم پس داریم:

$$
{a_1}^{-e_1\cdot e_2} \cdot {c_1‌}^{e_2} \equiv {a_1}^{-e_1\cdot e_2} \cdot (a_1 \cdot p)^{e_1 \cdot e_2} + {a_1}^{-e_1\cdot e_2} \cdot (b_1 \cdot q )^{e_1 \cdot e_2} \pmod{N} 
$$

با اندکی ساده سازی:

\begin{equation}
{a_1}^{-e_1\cdot e_2} \cdot {c_1‌}^{e_2} \equiv  p^{e_1 \cdot e_2} + {a_1}^{-e_1\cdot e_2} \cdot (b_1 \cdot q )^{e_1 \cdot e_2} \pmod{N} 
\label{eq:1}
\end{equation}

و همه مراحل گفته شده را این بار برای $c_2$ تکرار میکنیم در نهایت:

\begin{equation}
{a_2}^{-e_1\cdot e_2} \cdot {c_2}^{e_1} \equiv  p^{e_1 \cdot e_2} + {a_2}^{-e_1\cdot e_2} \cdot (b_2 \cdot q )^{e_1 \cdot e_2} \pmod{N} 
\label{eq:2}
\end{equation}

سپس نتیجه بدست آمده در $\ref{eq:1}$ را از $\ref{eq:2}$ کم میکنیم:

\begin{equation}
{a_2}^{-e_1\cdot e_2} \cdot {c_2}^{e_1} - {a_1}^{-e_1\cdot e_2} \cdot {c_1‌}^{e_2}
\label{eq:3}
\end{equation}

$$
\equiv  p^{e_1 \cdot e_2} + {a_2}^{-e_1\cdot e_2} \cdot (b_2 \cdot q )^{e_1 \cdot e_2} - p^{e_1 \cdot e_2} + {a_1}^{-e_1\cdot e_2} \cdot (b_1 \cdot q )^{e_1 \cdot e_2} \pmod{N}
$$

$$
\equiv {a_2}^{-e_1\cdot e_2} \cdot (b_2 \cdot q )^{e_1 \cdot e_2} + {a_1}^{-e_1\cdot e_2} \cdot (b_1 \cdot q )^{e_1 \cdot e_2} \pmod{N}
$$

بنابراین $q$ برابر خواهد بود با:

$$
q = \text{GCD}({a_2}^{-e_1\cdot e_2} \cdot {c_2}^{e_1} - {a_1}^{-e_1\cdot e_2} \cdot {c_1‌}^{e_2}, N)
$$

و همین کار را برای بدست آوردن $p$ تکرار میکنیم که به عنوان تمرین به خواننده واگذار می شود.

## مثال 

!!! example ""

    برای تمرین بیشتر به شما پیشنهاد می شود رایتاپ مربوط به چالش RSA-GCD در مسابقه <a target="_blank" href="https://writeups.fmc.tf/crypto/writeups/2024/0xL4ughCTF/RSA-GCD/">0xL4ughCTF</a> را مطالعه کنید.

--- 

!!! نویسنده
    [MohamadAli](https://github.com/w0h4w4d4li)
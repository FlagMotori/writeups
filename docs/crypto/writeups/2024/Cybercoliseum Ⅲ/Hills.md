---
tags:
  - Cybercoliseum Ⅲ
  - Crypto  
  - Hill Cipher
---

# چالش Hills

در این سوال به ما فایل `task.txt` داده شده است.    


```python title="task.txt" linenums="1"
-------------------------
|76 |101|115|116|101|114|
-------------------------
|32 |83 |97 |110|100|101|
-------------------------
|114|115|32 |115|104|111|
-------------------------
|117|108|100|32 |104|101|
-------------------------
|108|112|32 |121|111|117|
-------------------------
|32 |58 |41 |41 |41 |42 |
-------------------------

KLZCOUKTVOUWUKDOBGZVJIIIRGVHXCRQUCNOX_IBBL
```


با اندکی جستجو تو گوگل در مورد اسم سوال، پی میبریم با **Hill Cipher** طرف هستیم.


??? info "آشنایی با Hill Cipher"

	یک رمزنگاری چند الفبایی (`polyalphabetic`) است که ورژن گسترش یافته رمزنگاری `Affine` هستش و با استفاده از جبر خطی (`linear algebra`) و هم‌نهشتی (`modular arithmetic`) از طریق یک ماتریس عددی که به عنوان کلید رمزگذاری و رمزگشایی عمل می کند، ایجاد شده است.

	#### نحوه رمزنگاری
	برای رمزنگاری از یک الفبا و یک ماتریکس مربعی به سایز `n` استفاده میکنیم که بهش `encryption matrix` میگیم.

	بیایید برای درک بهتر با مثالی پیش برویم
	میخواهیم رشته `FLAG_MOTORI` را با الفبا زیر


	```
	alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_"
	```


	و ماتریکس M (سایز 2) رمزنگاری کنیم

	$$
	M =  \begin{bmatrix}
	2 & 3 \\
	5 & 7 
	\end{bmatrix}
	$$


	1. ابتدا متن به تکه هایی به طول `n` نقسیم میکنیم و در صورتیکه تکه آخر طولش کمتر از `n` باشد، حروف رندوم بهش اضافه میکنیم تا طولش برابر `n` شود. در مثال ما اینگونه میشود

		- ```FL, AG, _M, OT, OR, IZ```

	2. سپس هر حرف را با ایندکسش در الفبا جایگزین میکنیم.

		```
		(5,11), (0,6), (26,12), (14,19), (14,17), (8,25)
		```

	3. سپس برای هر تکه، ضرب ماتریکسی زیر را انجام میدهیم که C  مقادیر رمز شده ما خواهد بود. ( عدد 27 طول الفبای ما هستش)

		$$
		M \cdot P \equiv C \mod 27
		$$

		که در مثال ما برای تکه اول اینگونه خواهد بود

		$$
		\begin{bmatrix}
		2 & 3 \\
		5 & 7 
		\end{bmatrix}  
		\cdot
		\begin{bmatrix}
		5 \\
		11 
		\end{bmatrix}
		\equiv
		\begin{bmatrix}
		16 \\
		21 
		\end{bmatrix} \mod 27
		$$

		در انتها مقادیر رمز شده را با حروف نظیرشان در الفبا جایگزین میکنیم و به متن رمز شده میرسیم.
		که در مثال رشته 
		`FLAG_MOTORI`
		به متن رمز شده زیر تبدیل میشود.


		```
		QVSPHZEOZAK_
		```


	#### نحوه رمزگشایی
	برای رمزگشایی به ماتریکس و الفبای مورد استفاده نیاز داریم.
	کافیست وارون ماتریس به پیمانه 27 را محاسبه کنیم و باقی مراحل مشابه رمزنگاری پیش برویم.

	$$
	\begin{bmatrix}
	2 & 3 \\
	5 & 7 
	\end{bmatrix} ^{-1}
	\equiv
	\begin{bmatrix}
	-7 & 3 \\
	5 & -2 
	\end{bmatrix}
	\equiv
	\begin{bmatrix}
	19 & 3 \\
	5 & 24 
	\end{bmatrix} \mod 27
	$$


	#### پیاده سازی در پایتون
	
	=== "python"
		```python
		import numpy as np
		from sympy import Matrix

		class HillCipher:
			def __init__(self, alphabet, matrix):
				self.n, m = matrix.shape
				assert self.n==m
				self.alphabet = alphabet
				self.mod = len(self.alphabet)
				self.mapper = dict(zip(self.alphabet, range(self.mod)))
				self.mapper |= dict((v, k) for k, v in self.mapper.items())
				self.M = matrix % self.mod
				self.invM = np.array(Matrix(self.M).inv_mod(self.mod))

			def process(self, msg, dec=False):
				key = self.invM if dec else self.M
				msg += 'Z'*(len(msg)%self.n)
				msgI = [*map(self.mapper.get, msg)]
				res = ''
				for i in range(len(msgI)//self.n):
					P = np.array(msgI[i*self.n:i*self.n+self.n])
					C = np.dot(key,P) % self.mod
					res += ''.join(map(self.mapper.get, C))
				return res

			def encrypt(self, plain):
				return self.process(plain.upper())

			def decrypt(self, cipher):
				return self.process(cipher.upper(), True)

		alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ_'
		arr = np.array([
			[2,3],
			[5,7]
		])

		HillCipher(alphabet, arr).encrypt('FLAG_MOTORI')
		``` 


کافیست با استفاده از سایت زیر رمزگشایی کنیم و فلگ را بدست بیاوردیم.


<p dir="ltr">
<a href="https://www.dcode.fr/hill-cipher">https://www.dcode.fr/hill-cipher</a> 
</p>

---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`CODEBY{BTW_EXISTS_AN_INTERESTING_FILM_ABOUT_HILLS}`</div>


!!! نویسنده
    [mheidari98](https://github.com/mheidari98)


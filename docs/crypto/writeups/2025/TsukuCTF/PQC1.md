---
tags:
  - TsukuCTF
  - TsukuCTF 2025
  - Crypto  
  - post-quantum cryptography
  - ML-KEM
  - Openssl
  - Pem file
---

# چالش  PQC1


<figure markdown="span">
  ![Cover](PQC1.png){ width="400" }
</figure>

## بررسی اولیه چالش
در ابتدا چالش کد زیر همراه را با  فایل خروجی [ouput](./output1.txt){:download}  به ما داده است: 

```py  title="prob.py" linenums="1"
# REQUIRED: OpenSSL 3.5.0

import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from flag import flag

# generate private key
os.system("openssl genpkey -algorithm ML-KEM-768 -out priv-ml-kem-768.pem")
# generate public key
os.system("openssl pkey -in priv-ml-kem-768.pem -pubout -out pub-ml-kem-768.pem")
# generate shared secret
os.system("openssl pkeyutl -encap -inkey pub-ml-kem-768.pem -secret shared.dat -out ciphertext.dat")

with open("priv-ml-kem-768.pem", "rb") as f:
    private_key = f.read()

print("==== private_key[:128] ====")
print(private_key[:128].decode())

with open("ciphertext.dat", "rb") as f:
    ciphertext = f.read()

print("==== ciphertext(hex) ====")
print(ciphertext.hex())

with open("shared.dat", "rb") as f:
    shared_secret = f.read()

encrypted_flag = AES.new(shared_secret, AES.MODE_ECB).encrypt(pad(flag, 16))

print("==== encrypted_flag(hex) ====")
print(encrypted_flag.hex())
```

این سوال  و کد پایتون آن مشابه سوال [pqc0](https://writeups.fmc.tf/crypto/writeups/2025/TsukuCTF/PQC0/) است که کلید خصوصی و ciphertext  را تولید کرده. با این تفاوت که بجای اینکه کل کلید خصوصی را بدهد تنها 128 بایت اول آن (مقدار زیر) را به ما داده. 

```
-----BEGIN PRIVATE KEY-----
MIIJvgIBADALBglghkgBZQMEBAIEggmqMIIJpgRAaa2HTyQm2vmmDmw5eheMJp6g
Jm3scrIloNZZF2eKncQZfPyppNNNOwAV3WY
```

پس مانند سوال قبلی (PQC0) نیاز داریم تا کلید خصوصی را بدست بیاوریم تا با استفاده از آن ciphertext را کپسوله‌زدایی کنیم.


## حل چالش

ابتدا برای اینکه با ساختار کلید در openssl آشنا شویم، یک کلید خصوصی معمولی را در cmd  (بعد از نصب openssl 3.5) با استفاده از دستورات زیر ابتدا تولید و نمایش می‌دهیم.

```shell
openssl genpkey -algorithm ML-KEM-768 -out priv-ml-kem-768.pem
openssl pkey -in priv-ml-kem-768.pem -text
```

که خروجی آن به شکل زیر است. 


<figure markdown="span">
  ![priv-key data](openssl key info.png){ width="450" }
</figure>

همان‌طور که مشخص است ساختار کلید ML-KEM در openssl به ترتیب دارای سه مقدار seed، کلید خصوصی (dk) و کلید عمومی (ek) است. 

پس در این سوال عملا جدای از 30 بایت اولیه که اطلاعات header است، تنها به ما بخشی از seed مربوطه را داده است. همان‌طور که در الگوریتم 16  مربوط به  [FIPS 203](https://csrc.nist.gov/pubs/fips/203/final) ( دستورالعمل استفاده از  ML-KEM توسط NIST) آمده می‌توان با استفاده از مقدار seed  که شامل دو مقدار 32 بایتی $d$ و $z$ می شود مقدار کلید عمومی و خصوصی را ساخت.


<figure markdown="span">
  ![KeyGen algorithm](kem-keyGen algorithm.png){ width="600" }
</figure>

با درنظر گرفتن 30 بایت اول از کلید خصوصی داده شده که مربوط به header و ID الگوریتم است عملا در این چالش مقدار  $z$ به ما کامل داده نشده و تنها $d$ را می توانیم از seed استخراج کنیم. خب بدون $z$ چطوری کلید خصوصی رو بدست بیاریم؟؟! من این چالش رو تا همین جا پیش رفتم بعد از تمام شدن متوجه شدم که در اینجا عملا  $z$ تاثیری در تولید کلید خصوصی ندارد  و مقدار $z$ را می‌توان هر مقداری در نظر گرفت!! :thinking:   

!!! سوال question 
    ۱- آیا openssl در تولید همه کلیدها مقدار seed را در داخل خود کلید خصوصی قرار می دهد؟

    ۲- چرا openssl باید مقادیر seed یعنی $d$ و $z$ را داخل کلید خصوصی قرار بدهد؟ خب در این صورت تنها با نشت این دو می توان کلید خصوصی را بدست آورد! :thinking: 


```py  title="solve.py" linenums="1"
from hashlib import sha3_512, sha3_256
from mlkem.ml_kem import ML_KEM
from pyasn1.type import univ, namedtype
from pyasn1.codec.der import encoder
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

c='73e322ebc019d4c299e4e270b66d27c96e3cef69834d7fde38c6d7d2f3c3cedeb94f3414b4023e65924b498dc5a314c46390270387001282774702af9482220b92560caa7e304fc499257acefafa860bdd0522239ce7df3b0ecf04fa4dca2697788e2f733576fa1015c7927d6f7a765970e97203fd48a17bf56ba86d23e234100f74092b3a2c8c1a88444a5454174b526121bc1dceeea1d8a1fb2e2b5f88ead8ea03af10d95fe34e6277678b6b907007f256bb12614699109139be3d72ce94b143a3f61cc35fee36b70893153e28b21002df4835af9aff43c36b873a430b049db97b75cea1628984e8dc912e511d9a358621e6d0f9762df7301b6e22d9237deedc1a72a0068ae84d9446827daf59e8e8728e0c46d149a2d4c4fdb67bfe8e39d7acbdc384f560f7f2ea253b350e80124098fc923e5bf9fc5d385858f4ecbb46130e55a2ff704b2d7b69e5d9b3f9fd3c0ef5bf9a7e17e095206de6d8254fae8f5cb5ac1f8fef51a23a65a33ca91d027e2977931f6716320a0f6ad6962a162c456ef9482ea6f59bff0ea264efc1072d9edfb6536b2a7aa67cb618512048fff844e6c82d02fc3e3bcd6896e1e35ab8e47e9abf4de6900850fad7732c4f56553698ce7cfdaa01aa1cae2fc88ca0043c94d22a5c42f1893816571e82d6a3b66b8f835f811a085381388cfe5c36428eaae7a4e664bb0c4c00e0387d9e74f5041c37b349c976e169c9703d4d3c6eea3d26cd43eb38e0661cbd8687056820cb320df5421d5268c2e9645f0492033c713256bdd5e79cebd3efab8c859426bb6989c70aa0639d583c370446a1271c32abd9079e0aa88ede2b158261db39ae5d2d189fced9406a9dc5329a8b959bdd4e245ea1f8be2d5516cbd5777b64e09bd69ba07997e1a72fdb03ba2620a1c90d7a654eff545c49a8196e0ab93218d6cfb36b1cd0125900e26dd6688aa400d3d7684182a6011217469795a381b5bb7fbc805b28acd097a149649cb601ed571d529a9a8d45d3ab4d41e3e3d8e136d3b7fb1d571c44b4848e5b56dee14b0f431a5c4f417af6790f3b6df281974c4f9340b90e3f1880ee9c719ea1b7bd12356045f9ce25cbd24769aa1acabfee8d7c8e57f0d876f45ebefa5871bc0c10e0e706a7703ed856f3da904edf3a6d472321844b681d5f0c98a4b0e178eb6096d36ce90334d6df6f4ed877852a6f45ade4eeadf72cccdcf342eccd8d1b2322b83047fd256e7a7152802efc4577e3a90c714a7b2af352efe9111c149c8fbaa71bca6d515ec4e9529b5a55d9309378e0698c7c33e85e3425bfda177ec1aa1d81e402ce54405700dc7df9d4688cfa98e53657f7e4c8db52bec306a7e07b73fc26ce4a48888e65c80a4af8ec8251abbbd5521f0b098e5a8f43112fe9d96feeb51bcbedc19dd38d0f4def5be292411a5668d329bb0b74cc6a8526291421b9490bf29dcdc8f0072c7391434cf30f29c007c38f3ef31ffe774f4d9460bd743e4ce65b0617aa52a30914e733257f4b6a80e1f6aff06c342f8dd30532621db7df'
ciphertext=bytes.fromhex(c)
enc_flag=bytes.fromhex('fd302c76946654e6e469a4656b90a8d60fb3492ed8c2238350e8e833a35b3587')


ml_kem = ML_KEM()


pem_priv_data="""-----BEGIN PRIVATE KEY-----
MIIJvgIBADALBglghkgBZQMEBAIEggmqMIIJpgRAaa2HTyQm2vmmDmw5eheMJp6g
Jm3scrIloNZZF2eKncQZfPyppNNNOwAV3WY"""


pem_lines = pem_priv_data.splitlines() # Remove PEM headers
b64_data = "".join(line for line in pem_lines if not line.startswith("-----"))
missing_padding = len(b64_data) % 4
if missing_padding:
    b64_data += "=" * (4 - missing_padding)
seed = base64.b64decode(b64_data)[30:] # first 30 bytes are identifier so skipped

d=seed[:32]
z=b'0'*32 # ??  guess

ek, dk = ml_kem._key_gen(d,z)
k_ = ml_kem.decaps(dk, ciphertext)  # shared secret key
flag = unpad(AES.new(k_, AES.MODE_ECB).decrypt(enc_flag),16)
print(flag)
```




---
??? success "FLAG :triangular_flag_on_post:"
    <div dir="ltr">`TsukuCTF25{seed_5eed_s33d}`</div>


!!! نویسنده
    [HIGHer](https://twitter.com/HIGH01012) 





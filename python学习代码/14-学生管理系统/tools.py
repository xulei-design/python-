import hashlib


# 对密码进行加密
def encrypt_password(password, x='safaeef'):
    h = hashlib.sha256()
    h.update(password.encode('utf8'))  # 123456  除了给的密码，在随意给一段，将他们拼接到一起进行加密
    h.update(x.encode('utf8'))
    return h.hexdigest()




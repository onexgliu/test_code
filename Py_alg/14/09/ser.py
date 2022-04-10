def encrypt(plaintext, i):
    ciphertext = ""         # 加密后的密文
    for ch in plaintext:
        if ch.isalpha():    # 判断每个字符是否是字母
            if ch.isupper():    # 判断是否是大写
                ciphertext += chr(65 + (ord(ch) - 65 + i) % 26)
            else:
                ciphertext += chr(97 + (ord(ch) - 97 + i) % 26)
        else:
            ciphertext += ch
    return ciphertext
def decrypt(ciphertext, i):
    plaintext = ""          # 解密后的明文
    for ch in ciphertext:
        if ch.isalpha():    # 判断每个字符是否是字母
            if ch.isupper():    # 判断是否是大写
                plaintext += chr(65 + (ord(ch) - 65 - i) % 26)
            else:
                plaintext += chr(97 + (ord(ch) - 97 - i) % 26)
        else:
            plaintext += ch
    return plaintext
def main():
    sel = input("加密输入1，解密输入2：")
    while sel != "1" and sel != "2":    # 如果输入的不是1也不是2就重新输入
        sel = input("请输入1或2：")
    key = input("请输入秘钥：")
    while not key.isdigit():            # 如果输入的不是由数字组成就重新输入
        key = input("请输入整数：")
    if sel == "1":                      # 加密操作
        plaintext = input("请输入明文：")
        ciphertext = encrypt(plaintext, int(key))   # 调用加密函数
        print("密文："+ciphertext)     # 输出加密后的密文
    else:                               # 解密操作
        ciphertext = input("请输入密文：")
        plaintext = decrypt(ciphertext, int(key))   # 调用解密函数
        print("明文："+plaintext)      # 输出解密后的明文
if __name__ == "__main__":
    main()

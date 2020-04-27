"""
python 在 Windows下使用AES时要安装的是pycryptodome模块   pip install pycryptodome
python 在 Linux下使用AES时要安装的是pycrypto模块   pip install pycrypto
"""
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex


class BsnAES:
    """
    ECB：是一种基础的加密方式, 现在不常用，现在常用CBC模式
    """
    def __init__(self, secret, iv=None):
        self.secret = secret.encode('utf-8')
        if not iv:
            self.iv = b'0000000000000000'

    # 如果text不足16位的倍数就用空格补足为16位
    def add_to_16(self, text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')

    # 加密函数
    def encrypt(self, text):
        mode = AES.MODE_CBC  # 定义模式
        iv = b'0000000000000000'  # 偏移量--必须16字节
        text = self.add_to_16(text)
        cryptos = AES.new(self.secret, mode, self.iv)
        cipher_text = cryptos.encrypt(text)
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        return b2a_hex(cipher_text)

    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self, text):
        iv = b'0000000000000000'
        mode = AES.MODE_CBC
        cryptos = AES.new(self.secret, mode, self.iv)
        plain_text = cryptos.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip('\0')


if __name__ == '__main__':
    secret = '9999999999999999'
    bsn = BsnAES(secret)
    e = bsn.encrypt("hello world")  # 加密
    d = bsn.decrypt(e)  # 解密
    print("加密:", e)
    print("解密:", d)
    assert "hello world" == d
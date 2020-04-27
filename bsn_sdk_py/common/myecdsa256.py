import os
import base64
import hashlib
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import load_pem_private_key, Encoding, PrivateFormat
from cryptography.x509 import load_pem_x509_certificate, NameOID
# 引入官方包中的签名类 Ecies，默认实例化(CURVE_P_256_Size, SHA2)，CURVE_P_256_Size椭圆曲率和sha256算法
from hfc.util.crypto.crypto import Ecies, ecies, CURVE_P_256_Size, SHA2
from cryptography import x509
from cryptography.hazmat.primitives import serialization


# ecdsa256签名方法
def ecdsa_sign(message, key_data):
    """
	:param message: 待签名字符串
	:param pri_key_file_name: 用户私钥路径
	:return: 返回base64编码格式的签名值
	"""
    # Read the pri_key_file
    # path = os.path.abspath('.')
    # file = os.path.join(path, pri_key_file_name)
    # print('私钥目录路径: ', file)
    # pri_key_file = open(file, "rb")
    # key_data = pri_key_file.read()
    # pri_key_file.close()

    # 加载私钥
    skey = load_pem_private_key(key_data, password=None, backend=default_backend())

    # 使用官方库中的方法签名
    signature = Ecies(CURVE_P_256_Size, SHA2).sign(private_key=skey, message=message)

    # print("signature:", signature)
    # 返回base64编码格式的签名值 base64.b64encode(signature)
    return signature


# ecdsa256 验签方法
def ecdsa_verify(message, signature, key_data):
    """
	:param message: 待签名字符串
	:param signature: 返回报文中的 mac值
	:param pub_key_file: 网关公钥路径
	:return: 返回 True or False
	"""
    # 读取公钥内容
    # path = os.path.abspath('.')
    # file = os.path.join(path, pub_key_file)
    # print('网关公钥目录路径: ', file)
    # pub_key_file = open(file, "rb")
    # key_data = pub_key_file.read()
    # pub_key_file.close()

    # 加载X509证书 公钥证书
    cert = load_pem_x509_certificate(key_data, default_backend())
    # print("公钥证书cert:", cert)

    # 取出公钥秘钥内容
    public_key = cert.public_key()
    # print("公钥秘钥内容public_key:", public_key)

    # 读取签名后的数据
    mac = signature

    # 验签
    verify_results = Ecies().verify(public_key=public_key, message=message.encode('utf-8'),
                                    signature=base64.b64decode(mac))
    # print("verify_results:", verify_results)

    # 返回值为 T or F
    return verify_results


def certificate_request(name, save_path):
    ecies256 = ecies()
    private_key = ecies256.generate_private_key()
    csr = ecies256.generate_csr(private_key, x509.Name(
        [x509.NameAttribute(NameOID.COMMON_NAME, name)]))  # test02@app0001202004161020152918451
    csr_pem = csr.public_bytes(Encoding.PEM)
    sk_pem = private_key.private_bytes(Encoding.PEM, PrivateFormat.PKCS8, serialization.NoEncryption())
    with open(save_path, mode='wb') as f:
        f.write(sk_pem)

    # with open('pub.csr', mode='wb') as f:
    #     f.write(csr_pem)
    return csr_pem, save_path


def hash256_sign(o_str):
    sha256 = hashlib.sha256()
    sha256.update(o_str.encode('utf-8'))
    return sha256.hexdigest()  # .upper()


if __name__ == '__main__':
    o_str = 'USER0001202004151958010871292app00012020041610201529184510364a7ce7c1f7c3fb7afb3ea2b9c678ed3dfd5e7c61ae72c4541822646fd24a19'
    print((hash256_sign(o_str)))

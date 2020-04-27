# SDK调用参考


## python语言SDK

### 1. 调用前准备

#### 应用参数
> 应用参数是用户在参与应用成功之后在应用详情页面获取，或者由本地设置的一些参数，具体包含以下参数
 * __节点网关接口地址：__ 参与的城市节点的节点网关的调用地址
 * __用户编号：__ 用户的编号
 * __应用编号：__ 参与的应用的编号
 * __应用公钥：__ 用户参与成功之后下载的节点网关的应用公钥
 * __应用私钥：__ 托管类型应用再参与成功之后由BSN生成的应用公钥，非托管应用为在参与应用时上传的公钥所对应的私钥
 * __Https证书：__ 调用https网关接口时使用的https证书

 #### 本地参数
 * __证书存储目录：__ 用来存储非托管应用在调用用户证书登记时生成的用户私钥和证书的目录

### 2. 准备调用

#### 导入sdk包
需要引入下面的包
```
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.fabric_client import FabricClient
```
#### 初始化config
可以初始化一个存储所有配置的对象，这些具体的配置信息应当由调用者根据各自的项目配置或者读取之后，在调用时传入，  
在config的`Init`方法中实现了获取一个App基础信息的操作，该操作请不要频繁的调用，该接口将占用您的TPS和流量，可以在项目使用一个静态对象存储`config`在需要时使用。  
值得注意的是，在配置证书的时候，应用的证书（即用来签名和验签的证书）是直接传证书路径，而Https的证书是证书对于项目根  
目录的文件路径（这与之前的示例代码一致）。
```
	nodeApi = "" //节点网关地址
	user_code:="" //用户编号
	app_code :="" //应用编号
	app_public_cert_path :="" //应用公钥路径
	user_private_cert_path :="" //应用私钥路径
	mspDir:="" //证书存数目录
	httpcert :="" //https证书
	c = Config(user_code, app_code, nodeApi, mspDir, httpcert,
                 app_public_cert_path, user_private_cert_path)
```
#### 初始化Client
使用已经生成的配置对象，调用以下代码可以创建一个Client对象，用来调用节点网关
```
    client = FabricClient()
    client.set_config(c)
```

####   调用接口
每一个网关接口已经封装了请求和响应的参数对象，只需要赋值就可直接调用，方法内已经实现了签名和验签的操作。  
以下为注册子用户的调用操作，其他类似。
```
    client.register_user('hll4', '123456')
```

####   日志
若想获取更详细的运行过程，配置一个looger就可以了
```
        import logging
        FORMAT = "%(asctime)s %(thread)d %(message)s"
        logging.basicConfig(filename='bsn_test.log', filemode='w',level=logging.INFO, format=FORMAT, datefmt="[%Y-%m-%d %H:%M:%S]")

```

### 3.一些其他说明

#### 非托管应用的用户身份证书的说明
由于非托管的应用在调用网关进行交易的时候所需要的用户证书需要用户自己生成，其流程是：注册用户->登记用户证书 。在登记用户证书的操作中，会由本地生成一对秘钥，然后通过秘钥导出证书的CSR文件（证书申请文件），调用用户证书
登记接口获取一个有效的证书，使用该证书才能在通过托管应用交易处理接口中正常的发起交易。
需要注意的是在CSR文件中设置CN时，并不直接是注册的Name，而是由Name和AppCode拼接的名称，格式为`Name@AppCode` 。
该操作是在 `bsn_sdk_py.client.entity.enroll_user.EnrollUser`的`GetCertificateRequest`方法中实现的。

__证书的存储__ 目前只存储本地文件形式的证书，

命名规则为: 

          __证书的存储__+ '\keystore\' + Name@AppCode + '_private.pem' 
          __证书的存储__+ '\keystore\' + Name@AppCode + '_cert.pem'

#### 关于加密
为方便在进行数据交易的上链操作中对数据进行加密解密，SDK中实现了一种对称加密`AES`和一种非对称加密`SM2`算法  
其中对称加密为`AES`具体调用如下
```
	secret = '9999999999999999'
	t = "hello world"
    bsn = BsnAES(secret)
    e = bsn.encrypt(t)  # 加密
    d = bsn.decrypt(e)  # 解密
    assert t == d
```
非对称加密`SM2`，具体如下,在该方法中同时实现了SM2的签名和验签
>非对称加密中由公钥加密，私钥进行解密
```
    from gmssl import sm2, func
	private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
    public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
    sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)

    #数据和加密后数据为bytes类型
    data = b"111"
    enc_data = sm2_crypt.encrypt(data)
    dec_data =sm2_crypt.decrypt(enc_data)
    assert dec_data == data
```

#### 关于秘钥生成
在BSN中，`fabric`框架的密钥格式为`ECDSA`的`secp256r1`曲线，而`fisco-bcos`框架的密钥格式为`SM2`
在用户参与非托管应用时需要生成对应格式的密钥并上传。  
下面介绍这两种密钥的生成，秘钥的生成是使用`openssl`生成的，其中`SM2`秘钥的生成需要`openssl`的`1.1.1`及以上版本
> 注：以下命令是在linux环境下执行的
##### 1. ECDSA(secp256r1)的密钥生成
- 生成私钥
```
openssl ecparam -name prime256v1 -genkey -out key.pem
```
- 导出公钥
```
openssl ec -in key.pem -pubout -out pub.pem
```
- 导出pkcs8格式私钥
> 由于部分语言中使用pkcs8格式的密钥比较方便，可以使用下面的命令导出pkcs8格式私钥  
> 在本sdk中使用的私钥即为pkcs8格式
```
openssl pkcs8 -topk8 -inform PEM -in key.pem -outform PEM -nocrypt -out key_pkcs8.pem
```
通过以上命令可以生成三个文件  
__`key.pem`__ :私钥  
__`pub.pem`__ :公钥  
__`key_pkcs8.pem`__ :pkcs8格式私钥

##### 2.`SM2`格式秘钥生成  
首先需要检查`openssl`的版本是否支持`SM2`格式秘钥生成，可以使用下面的命令
```
openssl ecparam -list_curves | grep SM2
```
如果输出以下内容，则表示支持，
```
SM2       : SM2 curve over a 256 bit prime field
```
否则需要去官网下载`1.1.1`或者以上版本，
这是使用的为`1.1.1d`版本，  
官网下载地址：[https://www.openssl.org/source/openssl-1.1.1d.tar.gz](https://www.openssl.org/source/openssl-1.1.1d.tar.gz])  

- 生成私钥
```
openssl ecparam -genkey -name SM2 -out sm2PriKey.pem
```
- 导出公钥
```
openssl ec -in sm2PriKey.pem -pubout -out sm2PubKey.pem
```
- 导出pkcs8格式私钥
> 由于部分语言中使用pkcs8格式的密钥比较方便，可以使用下面的命令导出pkcs8格式私钥  
> 在本sdk中使用的私钥即为pkcs8格式
```
openssl pkcs8 -topk8 -inform PEM -in sm2PriKey.pem -outform pem -nocrypt -out sm2PriKeyPkcs8.pem
```
通过以上命令可以生成三个文件  
__`sm2PriKey.pem`__ :私钥  
__`sm2PubKey.pem`__ :公钥  
__`sm2PriKeyPkcs8.pem`__ :pkcs8格式私钥
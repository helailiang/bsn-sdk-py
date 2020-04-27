from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort, obj_sort
from bsn_sdk_py.trans.not_trust_trans_request import NotTrustTransRequest


class NoTrustTrans(BsnBase):
    """
    非托管模式交易
    """

    def __init__(self, chainCode, funcName, userName, args=None, transientData: dict=None):
        super().__init__()
        self.name = userName
        self.chainCode = chainCode
        self.funcName = funcName
        self.args = args
        self.transientData = transientData

    def req_body(self):
        transRequest = NotTrustTransRequest(self.chainCode, self.funcName, self.name, self.args, self.transientData)
        transRequest.set_config(self.config)
        transRequest_data = transRequest.notrust_trans_data()
        req_body = {
            "transData": transRequest_data,
        }
        return req_body

    def sign(self, body):
        # 拼接待签名的字符串
        sign_str = self.config.user_code + self.config.app_code + body['body']["transData"]
        # 对字符串 使用用户私钥证书进行 SHA256WITHECDSA 签名，调用ecdsa_sign方法生成base64格式mac值
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     obj_sort(res_data['body']["blockInfo"]) + obj_sort(res_data['body']["ccRes"])

        signature = res_data['mac']
        # 调用ecdsa_verify方法，进行验签
        return self.config.encrypt_sign.verify(verify_str, signature)

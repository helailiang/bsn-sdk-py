from bsn_sdk_py.common import myecdsa256
from bsn_sdk_py.client.config import Config
from bsn_sdk_py.client.entity.bsn_base import BsnBase
from bsn_sdk_py.until.tools import nonce_str, array_sort, map_sort


class GetBlockInfo(BsnBase):
    """
    获取块信息
    """
    def __init__(self, blockNumber=0, blockHash='', txId=''):
        self.blockNumber = blockNumber
        self.blockHash = blockHash
        self.txId = txId

    def req_body(self):
        req_body = {
            "blockNumber": self.blockNumber,
            "blockHash": self.blockHash,
            "txId": self.txId,
        }
        return req_body


    def sign(self, body):
        # 拼接待签名的字符串
        sign_str = self.config.user_code + self.config.app_code + str(body['body']["blockNumber"]) + \
                   body['body']["blockHash"] + body['body']["txId"]
        # 对字符串 使用用户私钥证书进行 SHA256WITHECDSA 签名，调用ecdsa_sign方法生成base64格式mac值
        mac = self.config.encrypt_sign.sign(sign_str).decode()
        return mac

    def verify(self, res_data):
        verify_str = str(res_data["header"]["code"]) + res_data["header"]["msg"] + \
                     str(res_data['body']["blockHash"]) + str(res_data['body']["blockNumber"]) + \
                     res_data['body']["preBlockHash"] + str(res_data['body']["blockSize"]) + \
                     str(res_data['body']["blockTxCount"]) + array_sort(res_data['body']["transactions"])

        signature = res_data['mac']
        # 调用ecdsa_verify方法，进行验签
        return self.config.encrypt_sign.verify(verify_str, signature)

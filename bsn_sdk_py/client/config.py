import json
from cryptography.hazmat.primitives.serialization import load_pem_private_key
from cryptography.hazmat.backends import default_backend
from bsn_sdk_py.common.api_requestor import APIRequestor
from bsn_sdk_py.client.bsn_enum import AppAlgorithmType
from bsn_sdk_py.common.bsn_encrypt import ECDSA, SM2
from bsn_sdk_py.client.exceptions import BsnException

class Config(object):
    """
    定义一个通用的配置
    """

    def __init__(self, user_code, app_code, nodeApi, mspDir,
                 app_public_cert_path, user_private_cert_path, http_client_cert=None, debug=False):
        self.user_code = user_code
        self.app_code = app_code
        self.nodeApi = nodeApi  # 节点网关
        self.mspDir = mspDir  # 证书保存目录
        self.http_client_cert = http_client_cert  # https 证书
        self.user_private_cert_path = user_private_cert_path

        # with open(self.user_private_cert_path, "rb") as fp:
        #     self.user_private_key = fp.read()

        self.app_public_cert_path = app_public_cert_path
        # with open(self.app_public_cert_path, "rb") as fp:
        #     self.app_public_key = fp.read()

        self.app_info = None
        self.app_info = self.getAppInfo()
        self.setAlgorithm()
        # print(self.app_info)

    def setAlgorithm(self):
        if self.app_info['algorithmType'] == AppAlgorithmType.AppAlgorithmType_R1.value:
            self.encrypt_sign = ECDSA(self.user_private_cert_path, self.app_public_cert_path)
        elif self.app_info['algorithmType'] == AppAlgorithmType.AppAlgorithmType_SM2.value:
            self.encrypt_sign = SM2(self.user_private_cert_path, self.app_public_cert_path)
        else:
            raise BsnException('-1', "无效的证书类型")
    def getAppInfo(self):
        """
        统一获取应用信息：
        {'appName': 'sdk测试-密钥非托管', 'appType': 'fabric', 'caType': 2, 'algorithmType': 2,
        'mspId': 'OrgbNodeMSP', 'channelId': 'app0001202004161020152918451'}
        :return:
        """
        req_url = self.nodeApi + "/api/app/getAppInfo"
        req_data = self.build_body()
        res = APIRequestor(self.http_client_cert).request_post(req_url, req_data)
        return res["body"]


    def build_body(self):
        data = {
            "header": {
                "userCode": self.user_code,
                "appCode": self.app_code,
            },
            "body": None,
            "mac": "",
        }
        return data



def read_private(pri_key_file_path):
    pri_key_file = open(pri_key_file_path, "rb")
    key_data = pri_key_file.read()
    pri_key_file.close()

    # 加载私钥
    skey = load_pem_private_key(key_data, password=None, backend=default_backend())
import requests
from bsn_sdk_py.client.exceptions import BsnException
from bsn_sdk_py.client.bsn_enum import ResCode
from bsn_sdk_py.until.bsn_logger import log_debug,log_info


class APIRequestor(object):
    def __init__(self, http_client_cert):
        self.http_client_cert = http_client_cert

    def request_post(self, req_url, data):
        log_info(("请求地址：", req_url))
        log_info(("请求数据：", data))
        headers = {'content-type': 'application/json'}
        if any((self.http_client_cert,)):
            res = requests.post(req_url, headers=headers, json=data,
                                verify=self.http_client_cert)
        else:
            res = requests.post(req_url, headers=headers, json=data, verify=False)

        resCode = res.status_code
        resHeaders = res.headers
        log_info(('接受到的响应headers：', resHeaders))
        if resCode != 200:
            raise Exception('请求失败,http code为{}'.format(resCode, ))
        resBody = res.json()
        log_info(('接受到的响应：', resBody))
        if resBody['header']["code"] != ResCode.ResCode_Suc.value:  # 返回成功，则需要进行解密
            raise BsnException(resBody['header']["code"],resBody['header']["msg"])
        return resBody

    def request_get(self):
        pass
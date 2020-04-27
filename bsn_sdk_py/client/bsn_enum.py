from enum import IntEnum


class AppAlgorithmType(IntEnum):
    """
    应用秘钥类型
    """
    AppAlgorithmType_Not = 0
    AppAlgorithmType_SM2 = 1  # SM2
    AppAlgorithmType_R1 = 2  # ECDSA(secp256r1)
    AppAlgorithmType_K1 = 3


class AppCaType(IntEnum):
    """
    应用秘钥托管类型
    """
    AppCaType_Not = 0
    AppCaType_Trust = 1  # 托管
    AppCaType_NoTrust = 2  # 非托管

class ResCode(IntEnum):
    """
       应用秘钥托管类型
       """
    ResCode_Suc = 0  # 校验成功
    ResCode_Fail = -1  # 校验失败

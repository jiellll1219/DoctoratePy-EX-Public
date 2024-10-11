from flask import request
from virtualtime import time
from utils import read_json, write_json
from admin.GiveItem import GiveItem
import json

from constants import ALLPRODUCTLIST_PATH, CASHGOODLIST_PATH, SYNC_DATA_TEMPLATE_PATH, GPGOODLIST_PATH

def GetUnconfirmedOrderIdList():

    data = request.data
    data = {
        "orderIdList": [],
        "playerDataDelta": {
            "deleted": {},
            "modified": {}
        }
    }

    return data

def getAllProductList():

    data = request.data
    data = read_json(ALLPRODUCTLIST_PATH,encoding='utf-8')

    return data

def getcreateOrder():

    goodid = json.loads(request.data)

    data = {
    "playerDataDelta": {
        "modified": {},
        "deleted": {}
    },
    "result": 0,
    "orderId": goodid["goodId"],
    "orderIdList": []
    }

    print(data)

    return data

def queryshowappproduct():

    json_body = json.loads(request.data)
    print(json_body)

    result = {
        "data": {
            "amount": 114514,
            "productName": "开采源石"
        },
        "isBox": True,
        "msg": "OK",
        "type": "A",
        "status": 0
    }

    return result

def querypaymentconfig():

    result = {
        "data": {
            "payment": [
                {
                    "key": "alipay",
                    "recommend": True,
                    "discount": False
                },
                {
                    "key": "wechat",
                    "recommend": False,
                    "discount": False
                },
                {
                    "key": "pcredit",
                    "recommend": False,
                    "discount": False
                }
            ]
        },
        "msg": "OK",
        "status": 0,
        "type": "A"
    }

    return result

def alipay():

    result = {
        "data": {
            "orderId": "114514",
            "extension": {
                "qs": "app_id=2018091261385264&......&version=1.0"
            }
        },
        "msg": "OK",
        "status": 0,
        "type": "A"
    }

def wechat():

    result = {
        "data": {
            "orderId": "114514",
            "extension": {
                "appid": "wx0ae7fb63d830f7c1",
                "noncestr": "5d7b4b7f6f6f6f6f6f6f6f6f6f6f6f",
                "package": "Sign=WXPay",
                "partnerid": "wx2018091261385264",
                "prepayid": "wx2018091261385264",
                "sign": "doctorate",
                "timestamp": time
            }
        },
        "msg": "OK",
        "status": 0,
        "type": "A"
    }

    return result

def state():

    result = {
        "data": {
            "pc": 1,
            "createtime": time,
            "productName": "开采源石",
            "amount": 114514,
            "productType": 2,
            "appCode": "7318def77669979d"
        },
        "msg": "已支付",
        "status": 116,
        "type": "A"
    }

    return result

def check():

    result = {
        "msg": "OK",
        "status": 0,
        "type": "A"
    }

    return result
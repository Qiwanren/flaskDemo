'''
    使用类实现产品订购功能


    flask获取：
        post中数据：request.form.get("comment")
        get中数据：request.args.get("comment")
        如果传递的是json格式数据：request.json.get("comment")


    备注：解析json串
        # json为字符串类型，非 bytes
        req = json.loads(str(request.body, encoding="utf-8"))
        reqStr = json.dumps(req)
'''

# coding: utf-8

from app.action.product import product
import json
from app.service.productService import productService
product_data = [
    {
        'id': 1,
        'name': '产品一'
    },
    {
        'id': 2,
        'name': '产品二'
    }
]

@product.route('/products', methods=['GET', ])
def products():
    data = {
        'status': 'success',
        'products': product_data
    }
    return json.dumps(data, ensure_ascii=False, indent=1)

@product.route('/orderProduct', methods=['GET', ])
def orderProduct():
    proService = productService()
    proService.sendProductToCB()
    return "message has send to cb!!!"







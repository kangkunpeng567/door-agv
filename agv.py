# 网页的数据请求是以json格式传输
from flask import Flask, request, jsonify
app = Flask(__name__)
# 3、访问到服务端路由函数
@app.route('/receive_data', methods=['POST'])
def receive_data():
    # 3、服务器和终端之间网页的数据请求是以json格式传输。
    # 服务端接收HTTP请求，从app1发送的json数据将会保存到request对象里，
    # 通get_json()方法请求对象把转化成字典对象
    data = request.get_json()

    # 字典类型：class 'dict'
    # 字典详情：{'command': 'STACKER_STACKER1_IN', 'isLoading': 'true', 'robotCode': 'CARRIER_001'}
    requestId = data["requestId"]

    aaa = {"requestId":requestId,"success":True}

    # 4、将字典对象内容aaa，通过jsonify转换成Response请求对象返回给客户端
    bbb = jsonify(aaa)
    print(data)
    return bbb
if __name__ == '__main__':
    app.run(debug=True, port=9002)
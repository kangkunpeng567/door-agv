import json
# 客户端请求访问服务端时, 会将需要传输的数据转换成json数据对象，存放response请求对象里，并通过http协议传输给服务端。
from flask import Flask,request
import requests
app = Flask(__name__)
# 1、客户端页面路由请求
@app.route('/send_data', methods=['GET','POST'])
def send_data():

    url = 'http://127.0.0.1:9002/receive_data'
    # data = {"command": "STACKER_STACKER1_IN",
    #         "isLoading": "true",
    #         "requestId": "625999e4-93f6-11ee-b963-661e06825e43",
    #         "robotCode": "CARRIER_001"
    # }
    data = request.get_json()

    # 2、进入客户端路由函数后，进行跳转请求到服务器端'/receive_data'，
    #  会将需要传输的数据转换成json数据，存放response请求对象里，并通过http协议传输给服务端。
    response = requests.post(url,json=data)

    # 5、客户端每发送的一个请求requist，同时也会得到服务端的一个respons对象，调用json()将请求对象转换成字典，
    print(response.json())

    # 6、每一个请求都会得到一个反馈，根据服务端路由调用完成函数后，反馈给客户端页面。
    return {'message': 'Data sent to app2', 'response_from_app2':response.json()}

if __name__ == '__main__':
    app.run(debug=True, port=9000)
#  从 flask 库中导入 Flask 类和 jsonify 函数
from flask import Flask, jsonify
#  从 flask_cors 库中导入 CORS 类，用于解决跨域问题
from flask_cors import CORS

#  创建 Flask 应用实例，__name__ 是当前模块的名称，Flask 用它来定位资源
app = Flask(__name__)
#  初始化 CORS，允许所有来源跨域访问本应用（解决前后端分离时的跨域报错）
CORS(app)  # 解决跨域

#  装饰器：将 URL 路径 /api/test 绑定到下面的 test 函数
@app.route('/api/test')
def test():
    #  定义处理 /api/test 请求的函数
    #  返回 JSON 格式响应，jsonify 会自动设置正确的 Content-Type 头
    return jsonify({
        "message": "前后端连接成功！"
    })

#  判断是否是直接运行此脚本（而不是被其他模块导入）
if __name__ == '__main__':
    #  启动 Flask 开发服务器，debug=True 开启调试模式（代码修改后自动重启，显示详细错误信息）
    app.run(debug=True)
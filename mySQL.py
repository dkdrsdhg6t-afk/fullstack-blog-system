# 导入模块
from flask import Flask  # Flask Web框架核心
from flask_cors import CORS  # 处理跨域请求（前端访问后端必需）
from flask_mysqldb import MySQL  # 连接MySQL数据库的工具

# 初始化应用
app = Flask(__name__)  # 创建Flask应用实例
CORS(app)  # 启用跨域支持（允许前端访问后端）

#  数据库配置
app.config['MYSQL_HOST'] = 'localhost'  # 数据库地址
app.config['MYSQL_USER'] = 'root'  # 数据库用户名
app.config['MYSQL_PASSWORD'] = 'Daisy110119'  # 数据库密码
app.config['MYSQL_DB'] = 'fullstack-blog-system'  # 要连接的数据库名

mysql = MySQL(app)  # 将配置绑定到MySQL工具，创建数据库连接实例


# 定义路由（接口）

#  测试接口
@app.route('/api/test')  # 定义URL路由 /api/test
def test():  # 对应的处理函数
    return "数据库连接正常！"  # 返回响应字符串（测试连通性）


#  获取文章列表接口
@app.route('/api/articles')  # 定义URL路由 /api/articles
def get_articles():  # 对应的处理函数
    try:  # 异常捕获（防止程序崩溃）
        # 执行SQL查询：从articles表查询所有数据
        cursor = mysql.connection.cursor()  # 创建数据库游标（用于执行SQL）
        cursor.execute("SELECT * FROM articles")  # 执行SQL查询语句
        articles = cursor.fetchall()  # 获取查询结果（所有行）
        cursor.close()  # 关闭游标（释放资源）

        # 返回JSON格式数据（前端易于解析）
        return {"code": 200, "data": articles}

    except Exception as e:  # 如果发生异常
        return {"code": 500, "msg": f"Error: {str(e)}"}  # 返回错误信息


# 启动应用
if __name__ == '__main__':  # 判断是否为主程序入口（避免被导入时运行）
    app.run(debug=True)  # 启动Flask开发服务器（debug模式：修改代码自动重启）
from flask import Flask # 导入Flask模块
app = Flask(__name__) # 创建应用实例
from  flask import  render_template
import pymysql

def select_student():
    # 连接database
    conn = pymysql.connect(host="127.0.0.1",
                           user="root",
                           password="123456",
                           db="gdit_student",
                           # db="cov",
                           charset="utf8")

    # 获取一个光标
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典数据类型

    # 定义将要执行的sql语句
    # sql = 'select user,pwd from student;'
    # sql = 'select user from student;'
    sql = 'select * from student;'
    # 拼接并执行sql语句
    cursor.execute(sql)

    # 取到查询结果
    # ret1 = cursor.fetchone()  # 取一条
    ret1 = cursor.fetchmany(3)  # 取三条
    cursor.close()
    conn.close()
    return ret1

@app.route('/',methods=["GET", "POST"])
def  index():
    ret_info = select_student()
    print(ret_info)
    data1 = ret_info[0]
    data2 = ret_info[1]
    data3 = ret_info[2]
    data_set = {
        "user": "gdit",
        "pwd": 100
    }
    return render_template('show_table2.html', data1 = data1, data2 = data2, data3 = data3)
if __name__ == '__main__':
	app.run(debug=True)
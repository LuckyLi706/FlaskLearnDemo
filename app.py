import json
import os

from flask import Flask
from flask import request

# 获取当前目录
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


# 参数可以携带请求发送
@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'


# GET和POST普通请求
@app.route('/login', methods=['GET', 'POST'])
def get_post_request():
    if request.method == 'GET':
        # 通过这种方式获取GET请求的值，
        # 如果当前请求不存在这个键，会引发一个 KeyError
        user_name_get = request.args.get('user', '')
        pass_word_get = request.args.get('pass', '')
        # 格式化字符串
        return "user：%s，pass：%s" % (user_name_get, pass_word_get)
    else:
        if request.method == 'POST':
            # 通过这种方式获取POST提交的表单
            if len(request.form) != 0:
                user_name_get = request.form['user']
                pass_word_get = request.form['pass']
                return "user：%s，pass：%s" % (user_name_get, pass_word_get)
            else:
                # 通过这种方式获取POST提交的json数据
                json_data = request.get_data()
                # 将拿到的数据转为json
                json_data_value = json.loads(json_data)
                return "user：%s，pass：%s" % (json_data_value['user'], json_data_value['pass'])
        else:
            return 'NOT SUPPORT METHOD'


# 上传单个文件
@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == "POST":
        f = request.files['file']
        save_file(f)
        return 'upload_file_success'


# 上传多个文件和json混合上传
@app.route('/upload_files', methods=['POST'])
def upload_files():
    if request.method == "POST":
        data = request.form.get('data')
        print(data)
        file_list = request.files.getlist('file')
        for file in file_list:
            save_file(file)
        return 'upload_files_success'


# 保存文件到本地
def save_file(file):
    # 生成随机数
    # random_num = random.randint(0, 100)
    # f.filename.rsplit('.', 1)[1] 获取文件的后缀
    # filename = datetime.now().strftime("%Y%m%d%H%M%S") + "_" + str(random_num) + "." + file.filename.rsplit('.', 1)[1]
    file_path = basedir + '/' + file.filename  # basedir 代表获取当前位置的绝对路径
    file.save(file_path)  # 把图片保存到static 中的file 文件名


if __name__ == '__main__':
    app.run()

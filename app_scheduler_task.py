from flask import Flask
from flask_apscheduler import APScheduler

# 需要下载Flask_APScheduler库
app = Flask(__name__)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()


# 黑名单功能，一小时的定时任务
@scheduler.task('interval', id='1', seconds=1 * 60 * 60, misfire_grace_time=900)
def print_hello():
    print('Hello,World')


if __name__ == '__main__':
    app.run()

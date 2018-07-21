import json

from flask import Flask
from Database import Database

app = Flask(__name__)

@app.route('/')
def index():
    return """
    <html>
    <head>
        <title>巨硬校园智能监控系统</title>
    </head>
    <body>
        <h1>巨硬API列表</h1>
        <ui>
            <li>
                <a href="/monitors">monitors</a>
            </li>
            <li>
                <a href="/students">students</a>
            </li>
        </ui>
    </body>
    </html>
    """


@app.route('/monitors')
def monitors():
    return json.dumps([e.to_list() for e in Database().monitor_read_all()])


@app.route('/students')
def students():
    return json.dumps([e.to_list() for e in Database().student_read_all()])


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)

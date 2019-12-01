import numpy as np
from flask import Flask, request, jsonify, render_template, send_from_directory
from mySpider import get_data
from idcard_s import SearchId

app = Flask(__name__)


def show_data(link):
    data_list = get_data(link, 1)
    return data_list


def Search_Id(user_id):
    need_list = SearchId(user_id)
    return need_list


@app.route('/favicon.ico')
def get_fav():
    return send_from_directory((app.root_path, 'static'),
                               'favicon.ico', mimetype='images/favicon.ico')


@app.route('/', methods=['GET', 'POST'])
def home():
    link = 'https://www.taptap.com/ajax/top/download'
    app_data = show_data(link)
    title = 'Android 热门手机游戏排行榜'
    # print(link)
    return render_template('index.html', app_data=app_data, title=title)


@app.route('/new/')
def new():
    link = 'https://www.taptap.com/ajax/top/new'
    app_data = show_data(link)
    return render_template('content.html', app_data=app_data)


@app.route('/idsearch/', methods=['GET', 'POST'])
def IdSearch():
    userid = 632826199408290011
    result = Search_Id(userid)
    return render_template('idsearch.html', result=result)


if __name__ == "__main__":
    app.run(debug=True)

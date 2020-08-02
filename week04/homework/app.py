from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient  # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)

app = Flask(__name__)

client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.dbsparta  # 'dbsparta'라는 이름의 db를 만듭니다.


## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')


## API 역할을 하는 부분
@app.route('/order', methods=['POST'])
def orderAlert():
    size_receive = request.form['size_give']
    address_receive = request.form['address_give']
    name_receive = request.form['name_give']

    doc = {
        'size': size_receive,
        'address': address_receive,
        'name': name_receive,
    }

    db.jordanShop.insert_one(doc)
    return jsonify({'result': 'success', 'msg': 'DONE'})


@app.route('/order', methods=['GET'])
def read_orders():
    orders = list(db.jordanShop.find({},{'_id':False}))
    return jsonify({'result': 'success', 'all_orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

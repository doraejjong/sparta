from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/review', methods=['POST'])
def write_review():
    title_receive = request.form['title_give']
    author_receive = request.form['author_give']
    review_receive = request.form['review_give']

    review = {
        'title': title_receive,
        'author': author_receive,
        'review': review_receive
    }
    db.reviews.insert_one(review)


    return jsonify({'result': 'success', 'msg': '리뷰작성이 완료 되었습니다!'})


@app.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.reviews.find({},{'_id': False }))
    return jsonify({'result': 'success', 'reviews': reviews})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)

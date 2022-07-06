from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.innovationcamp


## HTML 화면 보여주기
@app.route('/')
def task():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/mars', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    address_receive = request.form['address_give']
    size_receive = request.form['size_give']
    price_receive = int(size_receive)*500

    doc = {
        'name': name_receive,
        'address': address_receive,
        'size': size_receive,
        'price': price_receive,
    }

    db.onlineshop.insert_one(doc)

    return jsonify({'msg': '주문 완료!'})


# 주문 목록보기(Read) API
@app.route('/mars', methods=['GET'])
def view_orders():
    
    orders = list(db.onlineshop.find({}, {'_id': False}))

    return jsonify({'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
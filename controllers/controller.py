from flask import render_template
from app import app
from models.order_list import order_list

@app.route('/')
def index():
    return render_template('index.html', orders=order_list)

@app.route('/orders/<index>')
def order(index):
    return render_template('order.html', order=order_list[int(index)], order_number=str(int(index)+1))
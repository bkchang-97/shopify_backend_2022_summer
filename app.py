from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.secret_key = 'Secret Key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shopify_2022.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    stock = db.Column(db.Integer)
    category = db.Column(db.String(100))
    description = db.Column(db.String(100))

    def __init__(self, name, stock, category, description):
        self.name = name
        self.stock = stock
        self.category = category
        self.description = description

@app.route('/')
def index():
    all_data = Data.query.all()
    return render_template("index.html", inventory=all_data)

@app.route('/insert', methods=['POST'])
def insert():
    print("la di da")
    if request.method == 'POST':
        name = request.form['name']
        stock = request.form['stock']
        category = request.form['category']
        description = request.form['description']

        my_data = Data(name, stock, category, description)
        db.session.add(my_data)
        db.session.commit()

        flash("Item Inserted Successfully")

        return redirect(url_for('index'))

@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        data = Data.query.get(request.form.get('id'))

        data.name = request.form['name']
        data.stock = request.form['stock']
        data.category = request.form['category']
        data.description = request.form['description']

        db.session.commit()
        flash("Item Updated Successfully")

        return redirect(url_for('index'))

@app.route('/delete/<id>/', methods=['GET', 'POST'])
def delete(id):
    my_data = Data.query.get(id)
    db.session.delete(my_data)
    db.session.commit()
    flash("Item Deleted Successfully")

    return redirect(url_for('index'))

@app.route('/export')
def export():
    all_data = Data.query.all()
    names = [data.name for data in all_data]
    stocks = [data.stock for data in all_data]
    categories = [data.category for data in all_data]
    descriptions = [data.description for data in all_data]

    df = pd.DataFrame(list(zip(names, stocks, categories, descriptions)),
                      columns = ['Name', 'Stock', 'Category', 'Description'])

    df.to_csv('data.csv')

    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
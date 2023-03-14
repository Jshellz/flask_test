from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from api.models import ToDo

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/home/')
def home():
    todo_list = ToDo.query.all()
    return render_template('home.html', todo_list=todo_list)


if __name__ == '__main__':
    app.debug = True
    db.create_all()
    app.run(host='0.0.0.0')

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from users.register import RegisterForm
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://localhost/public'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
    app.run(debug=True)


class User(db.Model):
    __tablename__ = 'usertable'
    id = db.Column(db.Serial, primary_key=True)
    email = db.Column(db.VARCHAR(15), unique=True)
    password = db.Column(db.VARCHAR(15), unique=True)

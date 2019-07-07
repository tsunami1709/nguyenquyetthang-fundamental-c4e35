from flask import Flask
app = Flask(__name__)

#function binding
@app.route('/')
def home():
    return "Home page"

@app.route('/hello')
def hello():
    return "Hello Everyone"

@app.route('/hello/<name>')
def hello_khanh(name):
    age = 20
    return "Hello {0}, he is {1} year old!".format(name,age)
    
@app.route('/hello/<name>/<age>')
def hello_name_age(name,age):
    return "Hello {0}, he/she is {1} years old".format(name,age)

@app.route('/add/<int:_1_number>/<int:_2_number>')
def add(_1_number,_2_number):
    return str(_1_number + _2_number)

if __name__ == "__main__":
    app.run(debug=True)
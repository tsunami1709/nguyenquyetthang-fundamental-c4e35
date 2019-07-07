from flask import Flask,render_template
app = Flask(__name__)

user = {
    'thang':{
        "name":'Thang',
        "age":'23',
        'gender':"male"
        },
    'khanh':{
        "name":'Khanh',
        "age":'20',
        'gender':"male"
        },
    'hoa':{
        "name":'Hoa',
        "age":'30',
        'gender':"male"
        }
}

@app.route('/user/<username>')
def user_name(username):
    if username in user.keys():
        return render_template('info.html',user=user,username=username)
    else:
        return "User not found"

if __name__ == "__main__":
    app.run(debug=True)
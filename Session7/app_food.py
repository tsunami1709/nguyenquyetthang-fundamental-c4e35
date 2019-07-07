from flask import Flask,render_template,redirect
app = Flask(__name__)

all_foods = [
{
    "title":"Bánh bao",
    "description":"Rất ngon",
    "food_type":"food",
    "link":"https://www.huongnghiepaau.com/wp-content/uploads/2019/04/banh-bao-chay-ngon.jpg"
},
{
    "title":"Sủi cảo",
    "description":"Rất ngon",
    "food_type":"food",
    "link":"https://www.huongnghiepaau.com/wp-content/uploads/2017/11/42ef3937b979091cf46e2f58109b31fa.jpg"
},
{
    "title":"Rượu nữ nhi hồng",
    "description":"Rất thơm",
    "food_type":"drink",
    "link":"https://ssangyongvietnam.com.vn/wp-content/uploads/2018/12/ruou-nu-nhi-hong.jpg"
}    
]

@app.route('/foods')
def all_food():
    return render_template("all_foods.html", FOOD=all_foods)

@app.route('/foods/detail/<int:index>')
def food_detail(index):
    food_detail = all_foods[index]
    return render_template('foods_detail.html', FOOD_DETAIL=food_detail)

@app.route('/foods/delete/<int:index>')
def delete_food(index):
    del all_foods[index]
    return redirect('/foods')
if __name__ == "__main__":
    app.run(debug=True)
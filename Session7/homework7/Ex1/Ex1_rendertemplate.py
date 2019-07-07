from flask import Flask,render_template
app = Flask(__name__)

@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    w = float(weight)
    h = float(height)/100
    b = w/(h*h)
    SS = [b < 16, 16 <= b < 18.5, 18.5 <= b < 25, 25 <= b < 30, b>=30]
    b = round(b,2)
    LS = ['Severely underweight', 'Underweight', 'Normal', 'Overweight', 'Obese']
    return render_template('bmi.html',ss=SS,ls=LS, b=b)

if __name__ == "__main__":
    app.run(debug=True)
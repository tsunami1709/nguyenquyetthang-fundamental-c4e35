from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<weight>/<height>')
def bmi(weight,height):
    w = float(weight)
    h = float(height)/100
    b = w/(h*h)
    ls = ['Severely underweight', 'Underweight', 'Normal', 'Overweight', 'Obese']
    if b < 16:
        return "BMI = {0} and You: {1}".format(round(b,2),ls[0])
    elif b < 18.5:
        return "BMI = {0} and You: {1}".format(round(b,2),ls[1])
    elif b < 25:
        return "BMI = {0} and You: {1}".format(round(b,2),ls[2])
    elif b < 30:
        return "BMI = {0} and You: {1}".format(round(b,2),ls[3])
    elif b>=30:
        return "BMI = {0} and You: {1}".format(round(b,2),ls[4])
if __name__ == "__main__":
    app.run(debug=True)
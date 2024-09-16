from types import MethodType
from flask import Flask,jsonify



app = Flask(__name__)

@app.route('/')  # base API
def welcome():
    return'Hi I am Mayur'


@app.route('/addition')
def addition():
    print("We are testing addition API")
    a = 100 
    b = 200
    add = a + b
    print(f"Addition of {a} and {b} is {add}")

    return jsonify({"Message": f"Addition is {add}"})
    
@app.route('/name')   
def get_name():
    print("We are testing Name API")
    return jsonify({'Message': "Name API Successful"})
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002,debug=False)
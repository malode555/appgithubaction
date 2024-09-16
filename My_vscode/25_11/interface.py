from flask import Flask,jsonify,render_template,request
import project_db
import utils
app = Flask(__name__)

@app.route('/')  # base API
def welcome():
    print("We are learning Flask")
    return jsonify({'Message': "Welcome API Successful"})

############################################################################

@app.route('/name')   
def get_name():
    print("We are testing Name API")
    return jsonify({'Message': "Name API Successful"})

#############################################################################

@app.route('/name/<name>')   # name >> string
def Name(name):
    print("We are testing Name API")
    return jsonify({'Message': f"Name is {name}"})

@app.route('/marks/<int:mark>')   # name >> string
def get_marks(mark):
    print("We are testing marks API",type(mark))
    return jsonify({'Message': f"Student marks is {mark}"})


@app.route('/cgpa_score/<float:cgpa>')   # name >> string
def get_cgpa(cgpa):
    print("We are testing marks API",type(cgpa))
    print('Hello')
    print("Testing Debugger")
    return jsonify({'Message': f"CGPA is {cgpa}"})

########################################################################
########################## Addition API ################################
########################################################################

@app.route('/addition')
def addition():
    print("We are testing addition API")
    a = 100 
    b = 200
    add = a + b
    print(f"Addition of {a} and {b} is {add}")

    return jsonify({"Message": f"Addition is {add}"})

########################################################################
########################## Multiplication API ################################
########################################################################

@app.route('/multiplication')
def multiplication():
    print("We are testing addition API")

    data = request.form
    print('User data is :',data)
    a = int(data['a'])
    b = int(data['b'])
    mul = a * b
    print(f"Addition of {a} and {b} is {mul}")

    return jsonify({"Message": f"multiplication is {mul}"})

########################################################################
########################## Addition API ################################
########################################################################

@app.route('/test_addition')
def test_addition():
    print("We are testing addition API")
    data = request.get_json()
    print("user Data is ",data)
    a = int(data['a'])
    b = int(data['b'])
    add = utils.get_addition(a,b)

    print(f"Addition of {a} and {b} is {add}")

    return jsonify({"Message": f"Addition is {add}"})


#######################################################################
####################### Login API #####################################
#######################################################################

@app.route('/login',methods = ['POST'])
def login():
    print("Testing Login API")
    data = request.form
    if request.method == 'POST':
        print('Input data is ',data)
        user_id = data['user_id']
        password = data['password']

        msg = project_db.get_login_details(user_id,password)

        return jsonify({"Message":msg})
    
    else:
        return jsonify({"Message":'Unsuccessful'})



#######################################################################
####################### Test ML Model##################################
#######################################################################

@app.route('/predict',methods = ['POST'])
def prediction():
    print("Testing prediction API")
    data = request.form
    if request.method == 'POST':
        print('Input data is ',data)
        x1 = float(data['SepalLengthCm'])
        x2 = float(data['SepalWidthCm'])
        x3 = float(data['PetalLengthCm'])
        x4 = float(data['PetalWidthCm'])

        prediction = utils.predict_class(x1,x2,x3,x4)        
        return jsonify({"Message": f'predicted class is :{prediction}'})
    
    else:
        return jsonify({"Message":'Unsuccessful'})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002,debug=False)


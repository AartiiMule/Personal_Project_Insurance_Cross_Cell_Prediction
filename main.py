from flask import Flask, jsonify, render_template, request

from project_app.utils import  VehicleInsurance

# Creating instance here
app = Flask(__name__)


@app.route("/") 
def hello_flask():
    print("Welcome to Insurance cross cell Prediction System")   
    return render_template("index.html")


@app.route("/Predict_Response", methods = ["POST", "GET"])
def get_predicted_response():
    if request.method == "GET":
        print("We are in a GET Method")

        Gender = (request.args.get("Gender"))
        Age = eval(request.args.get("Age"))
        Driving_License = eval(request.args.get("Driving_License"))
        Region_Code = eval(request.args.get("Region_Code"))
        Previously_Insured = eval(request.args.get("Previously_Insured"))
        Vehicle_Age = request.args.get("Vehicle_Age") 
        Vehicle_Damage = request.args.get("Vehicle_Damage")
        Annual_Premium = eval(request.args.get("Annual_Premium"))
        Policy_Sales_Channel = eval(request.args.get("Policy_Sales_Channel"))
        Vintage = eval(request.args.get("Vintage"))




        print("*********************** Gender,Age,Driving_License,Region_Code,Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage **********************\n",Gender,Age,Driving_License,Region_Code,Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage)

    

        vehicle_ins = VehicleInsurance(Gender,Age,Driving_License,Region_Code,Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage)
        Response = vehicle_ins.get_predicted_response()
        
        return render_template("index.html", prediction = Response)
        print("__name__ -->", __name__)

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port= 5005, debug = False)  # By default Prameters
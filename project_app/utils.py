import pickle
import json
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import config


class VehicleInsurance():
    def __init__(self,Gender,Age,Driving_License,Region_Code,Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage):

        self.Gender = Gender
        self.Age	= Age
        self.Driving_License = Driving_License
        self.Region_Code	= Region_Code
        self.Previously_Insured	= Previously_Insured
        self.Vehicle_Age	= Vehicle_Age
        self.Vehicle_Damage	= Vehicle_Damage
        self.Annual_Premium	= Annual_Premium
        self.Policy_Sales_Channel	= Policy_Sales_Channel
        self.Vintage= Vintage
       
       

    def load_models(self):
        with open(config.MODEL_FILE_PATH,"rb") as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)

    def get_predicted_response(self):

        self.load_models()   # Creating instance of model and json_data

        
        array = np.zeros(len(self.json_data['columns']))


        array[0] = self.json_data["Gender"][self.Gender]
        array[1] = self.Age
        array[2] = self.Driving_License
        array[3] = self.Region_Code


        array[4] = self.Previously_Insured
        array[5] = self.json_data["Vehicle_Age"][self.Vehicle_Age]
        array[6] = self.json_data["Vehicle_Damage"][self.Vehicle_Damage]
        array[7] = self.Annual_Premium
        array[8] = self.Policy_Sales_Channel
        array[9] = self.Vintage


        Response = round(self.model.predict([array])[0],2)

        return Response


if __name__ == "__main__":
    Gender = "Male"
    Age = 44.0
    Driving_License = 1.0
    Region_Code = 28.0
    Previously_Insured = 0.0
    Vehicle_Age = "> 2 Years"
    Vehicle_Damage = "Yes"
    Annual_Premium = 40454.0
    Policy_Sales_Channel = 26.0
    Vintage = 217.0
    Response = 1.0

    vehicle_ins = VehicleInsurance(Gender,Age,Driving_License,Region_Code,Previously_Insured,Vehicle_Age,Vehicle_Damage,Annual_Premium,Policy_Sales_Channel,Vintage)
    Response = vehicle_ins.get_predicted_response()
    print("Predict Response:", Response)
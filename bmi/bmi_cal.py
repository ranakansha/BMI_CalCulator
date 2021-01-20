import json
import pandas as pd

Table2 = pd.DataFrame({
    "BMI Category": [],
    "BMI Range": [],
    "Health risk": []
    })
       

json_data = pd.read_json('bmi.json')

def bmi_calculator(height, weight):                         
    """                                                     
    This function will take input as ::                     
        :: height                                           
        :: weight                                           
    and return output as bmi range                          
    """          
                                    
    bmi = weight/(height**2)      
                                                      
    return bmi

bmi_data = bmi_calculator(json_data['HeightCm']*0.01, json_data['WeightCm'])

for bmi in bmi_data.iteritems(): 
    if (bmi < 18.4):                                        
        Table2['BMI Category'] = "Underweight"              
        Table2['BMI Range (kg/m2)'] = "18.4 and below"      
        Table2['Health risk'] = "Malnutrition risk"         
    elif ( bmi >= 18.5 and bmi < 24.9):                     
        Table2['BMI Category'] = "Normal weight"            
        Table2['BMI Range (kg/m2)'] = "18.5-24.9"           
        Table2['Health risk'] = "Low risk"                  
    elif ( bmi >= 25 and bmi < 30):                         
        Table2['BMI Category'] = "Overweight"               
        Table2['BMI Range (kg/m2)'] = "25-29.9"             
        Table2['Health risk'] = "Enhanced risk"             
        print("overweight")                                 
    elif ( bmi >=30 and bmi < 35):                           
        Table2['BMI Category'] = "Moderately obese"         
        Table2['BMI Range (kg/m2)'] = "30-34.9"             
        Table2['Health risk'] = "Medium risk"               
        print("Suffering from Obesity")                     
    elif (bmi >=35 and bmi < 40):                          
        Table2['BMI Category'] = "Severely obese"            
        Table2['BMI Range (kg/m2)'] = "35-39.9"              
        Table2['Health risk'] = "High risk"                  
        print("Suffering from Obesity")                      
    elif bmi >40:                                            
        Table2['BMI Category'] = "Very severly obese"  
        Table2['BMI Range (kg/m2)'] = "40 and above"  
        Table2['Health risk'] = "Very high risk"


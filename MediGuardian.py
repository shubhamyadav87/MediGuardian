import numpy as np
import pickle
import streamlit as st

# Load saved models
loaded_model1 = pickle.load(open(r"C:\Users\shubh\Desktop\Final\Project 4\Diabetes_trained_model.sav", 'rb'))
loaded_model2 = pickle.load(open(r"C:\Users\shubh\Desktop\Final\Project 4\Heart_disease_prediction.sav", 'rb'))
loaded_model3 = pickle.load(open(r"C:\Users\shubh\Desktop\Final\Project 4\Thyroid.sav", 'rb'))

# Prediction functions
def Diabetes_prediction(input_data):
  input_data_as_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_array.reshape(1, -1)
  prediction = loaded_model1.predict(input_data_reshaped)
  if prediction[0] == 0:
    return "The person is not diabetic"
  else:
    return "The person is diabetic"

def Heart_disease_prediction(input_data):
  input_data_as_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_array.reshape(1, -1)
  prediction = loaded_model2.predict(input_data_reshaped)
  if prediction[0] == 0:
    return "The person does not have heart disease"
  else:
    return "The person has heart disease"

def Thyroid_prediction(input_data):
  input_data_as_array = np.asarray(input_data)
  input_data_reshaped = input_data_as_array.reshape(1, -1)
  prediction = loaded_model3.predict(input_data_reshaped)
  if prediction[0] == 0:
    return "The person does not have thyroid issues"
  else:
    return "The person has thyroid issues"

def main():
  # Title
  st.title("MediGuardian")

  # Sidebar for selecting the type of prediction
  option = st.sidebar.selectbox(
    "Choose a prediction model",
    ("Diabetes Prediction", "Heart Disease Prediction", "Thyroid Prediction")
  )

  # Input fields based on the selected option
  if option == "Diabetes Prediction":
    Pregnancies = st.text_input("Enter No. of pregnancies")
    Glucose = st.text_input("Enter Glucose level")
    BloodPressure = st.text_input("Enter your Blood pressure(BP)")
    BMI = st.text_input("Enter your BMI (Body-mass-index)")
    Age = st.text_input("Enter your Age")
    input_data = [Pregnancies, Glucose, BloodPressure, BMI, Age]

    if st.button("Results"):
      Diagnosis = Diabetes_prediction(input_data)
      st.success(Diagnosis)
    
  elif option == "Heart Disease Prediction":
    Age = st.text_input("Enter your Age")
    Sex = st.text_input("Enter your Sex (1 = male; 0 = female)")
    CP = st.text_input("Enter Chest pain type (0-3)")
    Trestbps = st.text_input("Enter Resting blood pressure")
    Chol = st.text_input("Enter Serum cholesterol in mg/dl")
    FBS = st.text_input("Enter Fasting blood sugar (> 120 mg/dl, 1 = true; 0 = false)")
    Restecg = st.text_input("Enter Resting electrocardiographic results (0-2)")
    Thalach = st.text_input("Enter Maximum heart rate achieved")
    Exang = st.text_input("Enter Exercise induced angina (1 = yes; 0 = no)")
    Oldpeak = st.text_input("Enter ST depression induced by exercise relative to rest")
    Slope = st.text_input("Enter the slope of the peak exercise ST segment (0-2)")
    Ca = st.text_input("Enter number of major vessels (0-3) colored by flourosopy")
    Thal = st.text_input("Enter Thalassemia (1 = normal; 2 = fixed defect; 3 = reversible defect)")
    input_data = [Age, Sex, CP, Trestbps, Chol, FBS, Restecg, Thalach, Exang, Oldpeak, Slope, Ca, Thal]



    if st.button("Results"):
      Diagnosis = Heart_disease_prediction(input_data)
      st.success(Diagnosis)
    
  elif option == "Thyroid Prediction":
        Age = st.text_input("Enter your Age")
        Sex = st.text_input("Enter your Sex (1 = male; 0 = female)")
        On_thyroxine = st.text_input("On thyroxine (1 = yes; 0 = no)")
        Query_on_thyroxine = st.text_input("Query on thyroxine (1 = yes; 0 = no)")
        On_antithyroid_meds = st.text_input("On antithyroid medication (1 = yes; 0 = no)")
        Sick = st.text_input("Sick (1 = yes; 0 = no)")
        Pregnant = st.text_input("Pregnant (1 = yes; 0 = no)")
        Thyroid_surgery = st.text_input("Thyroid surgery (1 = yes; 0 = no)")
        I131_treatment = st.text_input("I131 treatment (1 = yes; 0 = no)")
        Query_hypothyroid = st.text_input("Query hypothyroid (1 = yes; 0 = no)")
        Query_hyperthyroid = st.text_input("Query hyperthyroid (1 = yes; 0 = no)")
        Lithium = st.text_input("Lithium (1 = yes; 0 = no)")
        Goitre = st.text_input("Goitre (1 = yes; 0 = no)")
        Tumor = st.text_input("Tumor (1 = yes; 0 = no)")
        Hypopituitary = st.text_input("Hypopituitary (1 = yes; 0 = no)")
        Psych = st.text_input("Psych (1 = yes; 0 = no)")
        TSH_measured = st.text_input("TSH measured (1 = yes; 0 = no)")
        TSH = st.text_input("TSH (mcU/mL)")
        T3_measured = st.text_input("T3 measured (1 = yes; 0 = no)")
        T3 = st.text_input("T3 (ng/dL)")
        TT4_measured = st.text_input("TT4 measured (1 = yes; 0 = no)")
        TT4 = st.text_input("TT4 (mcg/dL)")
        T4U_measured = st.text_input("T4U measured (1 = yes; 0 = no)")
        T4U = st.text_input("T4U (ratio)")
        FTI_measured = st.text_input("FTI measured (1 = yes; 0 = no)")
        FTI = st.text_input("FTI (index)")
        TBG_measured = st.text_input("TBG measured (1 = yes; 0 = no)")
        TBG = st.text_input("TBG (mcg/dL)")
        Referral_source = st.text_input("Referral source")
        input_data = [Age, Sex, On_thyroxine, Query_on_thyroxine, On_antithyroid_meds, Sick, Pregnant, Thyroid_surgery, I131_treatment, Query_hypothyroid, Query_hyperthyroid, Lithium, Goitre, Tumor, Hypopituitary, Psych, TSH_measured, TSH, T3_measured, T3, TT4_measured, TT4, T4U_measured, T4U, FTI_measured, FTI, TBG_measured, TBG, Referral_source]

        if st.button("Results"):
            Diagnosis = Thyroid_prediction(input_data)
            st.success(Diagnosis)


if __name__ == '__main__':
    main()

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from get_diabetes_recommendation import SehatAIDiabetesReport
from get_heart_disease_rec import SehatAIHeartDiseaseReport
from get_parkinsons_rec import SehatAIParkinsonsReport
# Set page configuration
st.set_page_config(page_title="Sehat AI: An AI-Powered Multiple Disease Predictor",
                   layout="wide",
                   page_icon="images/SehatAI_logo.jpg")

    
# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models

diabetes_model = pickle.load(open(f'{working_dir}/saved_models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open(f'{working_dir}/saved_models/heart_disease_model.sav', 'rb'))

parkinsons_model = pickle.load(open(f'{working_dir}/saved_models/parkinsons_model.sav', 'rb'))

# sidebar for navigation
with st.sidebar:

    # Center the image
    st.image("images/SehatAI_logo.jpg", use_container_width=True)  # Adjust width

    # Add the option menu
    selected = option_menu(
        'Sehat AI: An AI-Powered Multiple Disease Predictor',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinsons Prediction'],
        icons=['activity', 'heart', 'person'],
        menu_icon="hospital-fill",  
        default_index=0
    )


# Diabetes Prediction Page
if selected == 'Diabetes Prediction':

    # page title
    st.title('Diabetes Prediction using ML')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        patientName = st.text_input('Patient Name')

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')

    with col1:
        Glucose = st.text_input('Glucose Level')

    with col1:
        BloodPressure = st.text_input('Blood Pressure value')

    with col2:
        SkinThickness = st.text_input('Skin Thickness value')

    with col2:
        Insulin = st.text_input('Insulin Level')

    with col2:
        BMI = st.text_input('BMI value')

    with col3:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')

    with col3:
        Age = st.text_input('Age of the Person')

    with col3:
        Gender = st.text_input('Gender')

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):

        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]

        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)
    language = st.selectbox("Select Language", ["English", "Hindi", "Marathi", "Tamil"])

    if st.button('Get AI Recommendations'):
        input_data = {
            "Patient Name": patientName,
            "Pregnancies": Pregnancies,
            "Glucose": Glucose,
            "Blood Pressure": BloodPressure,
            "Skin Thickness": SkinThickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "Diabetes Pedigree Function": DiabetesPedigreeFunction,
            "Age": Age,
            "Gender": Gender
        }
        print(input_data)
    # Collect input data
        report = SehatAIDiabetesReport(
         language=language,
         patient_name=patientName,
         age=int(Age),
         gender=Gender,
         glucose=float(Glucose),
         blood_pressure=float(BloodPressure),
         bmi=float(BMI),
         insulin=float(Insulin)
        )

        diabetes_report = report.generate_report()
        st.write(diabetes_report)


# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':

    # page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        patientName = st.text_input("Patient Name")

    with col1:
        age = st.text_input('Age')

    with col1:
        sex = st.text_input('Sex')

    with col1:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')


    with col2:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col2:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col2:
        exang = st.text_input('Exercise Induced Angina')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col3:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col3:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    language = st.selectbox("Select Language", ["English", "Hindi", "Marathi", "Tamil"])

    if st.button('Get AI Recommendations'):
        report = SehatAIHeartDiseaseReport(
            language=language,
            patient_name=patientName,
            age=int(age),
            sex=sex,
            chest_pain_type=cp,
            resting_bp=int(trestbps),  # Convert to int
            fasting_blood_sugar=int(fbs),  # Convert to int
            rest_ecg=int(restecg),  # Convert to int
            max_heart_rate=int(thalach),  # Convert to int
            exercise_angina=int(exang),  # Convert to int
            cholesterol=int(chol),  # Convert to int
            st_depression=float(oldpeak),  # Convert to float (decimal values possible)
            st_slope=int(slope),  # Convert to int
            major_vessels=int(ca),  # Convert to int
            thal=int(thal)  # Convert to int
        )


        diabetes_report = report.generate_report()
        st.write(diabetes_report)
   


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # page title
    st.title("Parkinson's Disease Prediction using ML")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        patientName = st.text_input("Patient Name")

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col1:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col1:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    

    with col2:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col2:
        DDP = st.text_input('Jitter:DDP')

    with col2:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col2:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

   
    with col3:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col3:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col3:
        DDA = st.text_input('Shimmer:DDA')

    with col3:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col4:
        NHR = st.text_input('NHR')

    with col4:
        HNR = st.text_input('HNR')

    with col4:
        RPDE = st.text_input('RPDE')

    with col4:
        DFA = st.text_input('DFA')

    with col5:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col5:
        D2 = st.text_input('D2')

    with col5:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)
    language = st.selectbox("Select Language", ["English", "Hindi", "Marathi", "Tamil"])

    if st.button("Get AI Recommendations"):
     report = SehatAIParkinsonsReport(
        language=language,
        patient_name=patientName,
        fo=float(fo),
        fhi=float(fhi),
        flo=float(flo),
        Jitter_percent=float(Jitter_percent),
        Jitter_Abs=float(Jitter_Abs),
        RAP=float(RAP),
        PPQ=float(PPQ),
        DDP=float(DDP),
        Shimmer=float(Shimmer),
        Shimmer_dB=float(Shimmer_dB),
        APQ3=float(APQ3),
        APQ5=float(APQ5),
        APQ=float(APQ),
        DDA=float(DDA),
        NHR=float(NHR),
        HNR=float(HNR),
        RPDE=float(RPDE),
        DFA=float(DFA),
        spread1=float(spread1),
        spread2=float(spread2),
        D2=float(D2),
        PPE=float(PPE),
    )

    parkinsons_report = report.generate_report()
    st.write(parkinsons_report)

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
from sklearn.preprocessing import StandardScaler
from keras.models import load_model

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))

# loading the saved models
diabetes_model = pickle.load(open(f'F:/Projects/Multiple_Disease_prediction_system/saved/diabetes_prediction_model.sav', 'rb'))
heart_disease_model = load_model(f'F:/Projects/Multiple_Disease_prediction_system/saved/heart_disease_model.h5')
parkinsons_model = load_model(f'F:/Projects/Multiple_Disease_prediction_system/saved/parkinsons_disease_model.h5')
breast_cancer_model = load_model(f'F:/Projects/Multiple_Disease_prediction_system/saved/breast_cancer_model.h5')

# Load the saved scaler
with open('F:/Projects/Multiple_Disease_prediction_system/saved/scaler.sav', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Breast Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person', 'virus'],
                           default_index=0)

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    st.title('Diabetes Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    diab_diagnosis = ''
    
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholesterol in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    heart_diagnosis = ''
    
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)

# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
    with col1:
        RAP = st.text_input('MDVP:RAP')
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    with col3:
        DDP = st.text_input('Jitter:DDP')
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
    with col3:
        APQ = st.text_input('MDVP:APQ')
    with col4:
        DDA = st.text_input('Shimmer:DDA')
    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
    with col2:
        RPDE = st.text_input('RPDE')
    with col3:
        DFA = st.text_input('DFA')
    with col4:
        spread1 = st.text_input('spread1')
    with col5:
        spread2 = st.text_input('spread2')
    with col1:
        D2 = st.text_input('D2')
    with col2:
        PPE = st.text_input('PPE')

    parkinsons_diagnosis = ''
    
    if st.button("Parkinson's Test Result"):
        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)

# Breast Cancer Prediction Page
if selected == 'Breast Cancer Prediction':
    st.title('Breast Cancer Prediction using ML')

    col1, col2, col3 = st.columns(3)

    with col1:
        radius_mean = st.text_input('Mean Radius')
    with col2:
        texture_mean = st.text_input('Mean Texture')
    with col3:
        perimeter_mean = st.text_input('Mean Perimeter')
    with col1:
        area_mean = st.text_input('Mean Area')
    with col2:
        smoothness_mean = st.text_input('Mean Smoothness')
    with col3:
        compactness_mean = st.text_input('Mean Compactness')
    with col1:
        concavity_mean = st.text_input('Mean Concavity')
    with col2:
        concave_points_mean = st.text_input('Mean Concave Points')
    with col3:
        symmetry_mean = st.text_input('Mean Symmetry')
    with col1:
        fractal_dimension_mean = st.text_input('Mean Fractal Dimension')
    with col2:
        radius_se = st.text_input('Radius SE')
    with col3:
        texture_se = st.text_input('Texture SE')
    with col1:
        perimeter_se = st.text_input('Perimeter SE')
    with col2:
        area_se = st.text_input('Area SE')
    with col3:
        smoothness_se = st.text_input('Smoothness SE')
    with col1:
        compactness_se = st.text_input('Compactness SE')
    with col2:
        concavity_se = st.text_input('Concavity SE')
    with col3:
        concave_points_se = st.text_input('Concave Points SE')
    with col1:
        symmetry_se = st.text_input('Symmetry SE')
    with col2:
        fractal_dimension_se = st.text_input('Fractal Dimension SE')
    with col3:
        radius_worst = st.text_input('Worst Radius')
    with col1:
        texture_worst = st.text_input('Worst Texture')
    with col2:
        perimeter_worst = st.text_input('Worst Perimeter')
    with col3:
        area_worst = st.text_input('Worst Area')
    with col1:
        smoothness_worst = st.text_input('Worst Smoothness')
    with col2:
        compactness_worst = st.text_input('Worst Compactness')
    with col3:
        concavity_worst = st.text_input('Worst Concavity')
    with col1:
        concave_points_worst = st.text_input('Worst Concave Points')
    with col2:
        symmetry_worst = st.text_input('Worst Symmetry')
    with col3:
        fractal_dimension_worst = st.text_input('Worst Fractal Dimension')

    breast_cancer_diagnosis = ''
    
if st.button('Breast Cancer Test Result'):
    user_input = [radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean, compactness_mean,
                  concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
                  radius_se, texture_se, perimeter_se, area_se, smoothness_se, compactness_se,
                  concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
                  radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
                  compactness_worst, concavity_worst, concave_points_worst, symmetry_worst,
                  fractal_dimension_worst]

    user_input = [float(x) for x in user_input]
    breast_cancer_prediction = breast_cancer_model.predict([user_input])

    # Since breast_cancer_prediction is likely an array, check if any element in it is 1 for positive prediction
    if breast_cancer_prediction.any() == 1:
        breast_cancer_diagnosis = 'The tumor is malignant (cancerous).'
    else:
        breast_cancer_diagnosis = 'The tumor is benign (non-cancerous).'

        st.success(breast_cancer_diagnosis)


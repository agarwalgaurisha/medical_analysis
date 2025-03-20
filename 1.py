import streamlit as st
import pickle

st.set_page_config(page_title="Disease Prediction", page_icon="$")
hide_st_style = """<style>
                      #MainMenu{visibility:hidden;}
                      footer{visibility:hidden;}
                      header{visibility:hidden;}
                      </style>
                      """
st.markdown(hide_st_style, unsafe_allow_html=True)
background_image_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQU_E_rBSGo4gn1tPhg29pB-7bTcv7EZvRMaQ&s"
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}
[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0, 0, 0, 0.7);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)


# Load the models
models = {
    "parkison": pickle.load(open("parkison_model.sav", "rb")),
    "diabetes": pickle.load(open("diabetes_model.sav", "rb")),
    "heart_disease": pickle.load(open("heart_disease_model.sav", "rb")),
    

}

# Disease selection
select = st.selectbox(
    "Select a disease to predict", [
        "Diabetes prediction",
        "Parkinson prediction",
        "Heart disease prediction",
        
    ]
)

# Function to handle input fields dynamically
def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)
st.markdown('<h1 style="color:purple;">Welcome to Disease Prediction</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:green;">Please select a disease from the dropdown to get started with the prediction.</p>', unsafe_allow_html=True)

# Diabetes Prediction Page
if select == 'Diabetes prediction':
    st.title('Diabetes')
    st.write("Enter the following details to predict diabetes:")

    Pregnancies = display_input('Number of Pregnancies', 'Enter number of times pregnant', 'Pregnancies', 'number')
    Glucose = display_input('Glucose Level', 'Enter glucose level', 'Glucose', 'number')
    BloodPressure = display_input('Blood Pressure value', 'Enter blood pressure value', 'BloodPressure', 'number')
    SkinThickness = display_input('Skin Thickness value', 'Enter skin thickness value', 'SkinThickness', 'number')
    Insulin = display_input('Insulin Level', 'Enter insulin level', 'Insulin', 'number')
    BMI = display_input('BMI value', 'Enter Body Mass Index value', 'BMI', 'number')
    DiabetesPedigreeFunction = display_input('Diabetes Pedigree Function value', 'Enter diabetes pedigree function value', 'DiabetesPedigreeFunction', 'number')
    Age = display_input('Age of the Person', 'Enter age of the person', 'Age', 'number')

    # Prediction on button click
    diab_diagnosis = ''
    if st.button('Diabetes Test Result'):
        try:
            # Make the prediction using the trained model
            features = [
                Pregnancies, Glucose, BloodPressure, SkinThickness, 
                Insulin, BMI, DiabetesPedigreeFunction, Age
            ]
            
            # Predict the result using the model
            diab_prediction = models['diabetes'].predict([features])  # Pass a 2D array
            if diab_prediction[0] == 1:
                diab_diagnosis = 'The person is diabetic'
            else:
                diab_diagnosis = 'The person is not diabetic'
            st.markdown(f"<h3 style='color:orange;'>{diab_diagnosis}</h3>", unsafe_allow_html=True)

            # Show the result
            st.success(diab_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")
# Parkinson's Prediction Page
if select == "Parkinson prediction":
    st.title("Parkinson Disease")
    st.write("Enter the following details to predict Parkinson's disease:")

    # Collect input data
    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        # Preparing the input data for prediction
        features = [
            fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, 
            Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, 
            spread2, D2, PPE
        ]
        
        try:
            # Predict the result using the Parkinson's model
            parkinsons_prediction = models['parkinsons'].predict([features])
            # Set diagnosis based on the prediction
            parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
            st.success(parkinsons_diagnosis)
        except Exception as e:
            st.error(f"Error in prediction: {e}")
if select == 'Heart disease prediction':
    st.title('Heart Disease Prediction')
    st.write("Enter the following details to predict heart disease:")

    # Collect user input for heart disease prediction
    age = display_input('Age', 'Enter age of the person', 'age', 'number')
    sex = display_input('Sex (1 = male; 0 = female)', 'Enter sex of the person', 'sex', 'number')
    cp = display_input('Chest Pain types (0, 1, 2, 3)', 'Enter chest pain type', 'cp', 'number')
    trestbps = display_input('Resting Blood Pressure', 'Enter resting blood pressure', 'trestbps', 'number')
    chol = display_input('Serum Cholesterol in mg/dl', 'Enter serum cholesterol', 'chol', 'number')
    fbs = display_input('Fasting Blood Sugar > 120 mg/dl (1 = true; 0 = false)', 'Enter fasting blood sugar', 'fbs', 'number')
    restecg = display_input('Resting Electrocardiographic results (0, 1, 2)', 'Enter resting ECG results', 'restecg', 'number')
    thalach = display_input('Maximum Heart Rate achieved', 'Enter maximum heart rate', 'thalach', 'number')
    exang = display_input('Exercise Induced Angina (1 = yes; 0 = no)', 'Enter exercise induced angina', 'exang', 'number')
    oldpeak = display_input('ST depression induced by exercise', 'Enter ST depression value', 'oldpeak', 'number')
    slope = display_input('Slope of the peak exercise ST segment (0, 1, 2)', 'Enter slope value', 'slope', 'number')
    ca = display_input('Major vessels colored by fluoroscopy (0-3)', 'Enter number of major vessels', 'ca', 'number')
    thal = display_input('Thal (0 = normal; 1 = fixed defect; 2 = reversible defect)', 'Enter thal value', 'thal', 'number')

    heart_diagnosis = ''

    # Display inputs and check if any input is missing
    if st.button('Heart Disease Test Result'):
        if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]):
            st.warning("Please fill in all fields.")
        else:
            try:
                # Prepare the input data for prediction
                features = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

                # Check if all features are correctly passed as a 2D list (required for prediction)
                prediction_input = [features]

                # Make prediction
                heart_prediction = models['heart_disease'].predict(prediction_input)

                # Display result
                if heart_prediction[0] == 1:
                    heart_diagnosis = 'The person has heart disease'
                else:
                    heart_diagnosis = 'The person does not have heart disease'

                st.success(heart_diagnosis)

            except Exception as e:
                st.error(f"Error in prediction: {e}")
                
                
                
                

# Imports
import streamlit as st
import pandas as pd
import pickle

# Opening intro text
st.write('# Are You Concerned About Having Diabetes?')

st.write('After answering a few questions, this application will be able to provide you with a prediction of whether you have diabetes,\
    as well as the probability that this prediction is correct.')

st.write('### Answer a few questions about yourself:')

# First field: High Blood Pressure
HighBP = st.checkbox(
    label='Have you ever been told you have high blood pressure by a doctor, nurse, or other health professional?',
    key='HighBP')
if HighBP == False:
    HighBP = 0.0
else:
    HighBP = 1.0

# Second field: High Cholesterol
HighChol = st.checkbox(
    label='Have you ever been told you have high blood cholesterol by a doctor, nurse, or other health professional?',
    key='HighChol')
if HighChol == False:
    HighChol = 0.0
else:
    HighChol = 1.0

# Third field: Cholesterol Check
CholCheck = st.checkbox(
    label='Have you had your cholesterol checked within the last five years?',
    key='CholCheck')
if CholCheck == False:
    CholCheck = 0.0
else:
    CholCheck = 1.0

# Fourth field: BMI
st.write('How tall are you?')
feet = st.slider(
    label='Feet',
    min_value=4.0,
    max_value=6.0,
    step=1.0)
inches = st.slider(
    label='Inches',
    min_value=0.0,
    max_value=11.0,
    step=1.0)
height = (feet * 12) + inches
st.write('How much do you weigh?')
weight = st.slider(
    label='Pounds',
    min_value=0.0,
    max_value=1000.0,
    step=1.0)
BMI = float(int(weight / height**2 * 703))

# Fifth field: Smoker
Smoker = st.checkbox(
    label='Have you smoked at least 100 cigarettes in your entire life? [Note: 5 packs = 100 cigarettes]',
    key='Smoker')  
if Smoker == False:
    Smoker = 0.0
else:
    Smoker = 1.0

# Sixth field: Stroke
Stroke = st.checkbox(
    label='Have you ever been told you had a stroke?',
    key='Stroke')
if Stroke == False:
    Stroke = 0.0
else:
    Stroke = 1.0

# Seventh field: Heart Disease or Heart Attack
HeartDiseaseorAttack = st.checkbox(
    label='Have you ever had coronary heart disease (CHD) or a myocardial infarction (MI)?',
    key='HeartDiseaseorAttack')
if HeartDiseaseorAttack == False:
    HeartDiseaseorAttack = 0.0
else:
    HeartDiseaseorAttack = 1.0

# Eighth field: Physical Activity
PhysActivity = st.checkbox(
    label='Have you done physical activity or exercise during the past 30 days other than your regular job?',
    key='PhysActivity')
if PhysActivity == False:
    PhysActivity = 0.0
else:
    PhysActivity = 1.0

# Ninth field: Fruits
Fruits = st.checkbox(
    label='Do you consume fruit 1 or more times per day?',
    key='Fruits')
if Fruits == False:
    Fruits = 0.0
else:
    Fruits = 1.0

# Tenth field: Vegetables
Veggies = st.checkbox(
    label='Do you consume veggies 1 or more times per day?',
    key='Veggies')
if Veggies == False:
    Veggies = 0.0
else:
    Veggies = 1.0

# Eleventh field: Heavy Alcohol Consumption
HvyAlcoholConsump = st.checkbox(
    label='Are you a heavy drinker (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)?',
    key='HvyAlcoholConsump')
if HvyAlcoholConsump == False:
    HvyAlcoholConsump = 0.0
else:
    HvyAlcoholConsump = 1.0

# Twelfth field: Healthcare
AnyHealthcare = st.checkbox(
    label='Do you have any kind of health care coverage, including health insurance, prepaid plans such as HMOs,\
        or government plans such as Medicare, or Indian Health Service?',
    key='AnyHealthcare')
if AnyHealthcare == False:
    AnyHealthcare = 0.0
else:
    AnyHealthcare = 1.0

# Thirteenth field: No Doctor Because of Cost
NoDocbcCost = st.checkbox(
    label='Was there a time in the past 12 months when you needed to see a doctor but could not because of cost?',
    key='NoDocbcCost')
if NoDocbcCost == False:
    NoDocbcCost = 0.0
else:
    NoDocbcCost = 1.0

# Fourteenth field: General Health
GenHlth = st.radio(
    label='How would you say that, in general, your health is?',
    options=(
        'Excellent',
        'Very Good',
        'Good',
        'Fair',
        'Poor'))
if GenHlth == 'Excellent':
    GenHlth = 1.0
elif GenHlth == 'Very Good':
    GenHlth = 2.0
elif GenHlth == 'Good':
    GenHlth = 3.0
elif GenHlth == 'Fair':
    GenHlth = 4.0
else:
    GenHlth = 5.0

# Fifteenth field: Mental Health
MentHlth = st.slider(
    label='Now thinking about your mental health, which includes stress, depression, and problems with emotions,\
        for how many days during the past 30 days would you say that your mental health was not good?',
    min_value=0.0,
    max_value=30.0,
    step=1.0)

# Sixteenth field: PhysHlth
PhysHlth = st.slider(
    label='Now thinking about your physical health, which includes physical illness and injury,\
        for how many days during the past 30 days would you say that your physical health not good?',
    min_value=0.0,
    max_value=30.0,
    step=1.0)

# Seventeenth field: Difficulty Walking
DiffWalk = st.checkbox(
    label='Do you have serious difficulty walking or climbing stairs?',
    key='DiffWalk')
if DiffWalk == False:
    DiffWalk = 0.0
else:
    DiffWalk = 1.0

# Eighteenth field: Sex
Sex = st.radio(
    label='What is your sex?',
    options=(
        'Female',
        'Male'))
if Sex == 'Female':
    Sex = 0.0
else:
    Sex = 1.0

# Nineteenth field: Age
Age = st.slider(
    label='What is your age?',
    min_value=0,
    max_value=100,
    step=1)
if Age >= 18 <= 24:
    Age = 1.0
elif Age >= 25 <= 29:
    Age = 2.0
elif Age >= 30 <= 34:
    Age = 3.0
elif Age >= 35 <= 39:
    Age = 4.0
elif Age >= 40 <= 44:
    Age = 5.0
elif Age >= 45 <= 49:
    Age = 6.0
elif Age >= 50 <= 54:
    Age = 7.0
elif Age >= 55 <= 59:
    Age = 8.0
elif Age >= 60 <= 64:
    Age = 9.0
elif Age >= 65 <= 69:
    Age = 10.0
elif Age >= 70 <= 74:
    Age = 11.0
elif Age >= 75 <= 79:
    Age = 12.0
else:
    Age = 13.0

# Twentieth field: Education
Education = st.radio(
    label='What is the highest grade or year of school you completed?',
    options=(
        'Never attended school or only kindergarten',
        'Grades 1 through 8 (Elementary)',
        'Grades 9 through 11 (Some high school)',
        'Grade 12 or GED (High school graduate)',
        'College 1 year to 3 years (Some college or technical school)',
        'College 4 years or more (College graduate)'))
if Education == 'Never attended school or only kindergarten':
    Education = 1.0
elif Education == 'Grades 1 through 8 (Elementary)':
    Education = 2.0
elif Education ==  'Grades 9 through 11 (Some high school)':
    Education = 3.0
elif Education == 'Grade 12 or GED (High school graduate)':
    Education = 4.0
elif Education ==  'College 1 year to 3 years (Some college or technical school)':
    Education = 5.0
else:
    Education = 6.0

# Twenty-first field: Income
Income = st.radio(
    label='What is your annual household income from all sources?',
    options=(
        'Less than $10,000',
        'Less than $15,000 ($10,000 to less than $15,000)',
        'Less than $20,000 ($15,000 to less than $20,000)',
        'Less than $25,000 ($20,000 to less than $25,000)',
        'Less than $35,000 ($25,000 to less than $35,000)',
        'Less than $50,000 ($35,000 to less than $50,000)',
        'Less than $75,000 ($50,000 to less than $75,000)',
        '$75,000 or more'))
if Income == 'Less than $10,000':
    Income = 1.0
elif Income == 'Less than $15,000 ($10,000 to less than $15,000)':
    Income = 2.0
elif Income ==  'Less than $20,000 ($15,000 to less than $20,000)':
    Income = 3.0
elif Income == 'Less than $25,000 ($20,000 to less than $25,000)':
    Income = 4.0
elif Income ==  'Less than $35,000 ($25,000 to less than $35,000)':
    Income = 5.0
elif Income ==  'Less than $50,000 ($35,000 to less than $50,000)':
    Income = 6.0
elif Income == 'Less than $75,000 ($50,000 to less than $75,000)':
    Income = 7.0
else:
    Income = 8.0

# Creating the dataframe to run predictions on
values = [HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies,
    HvyAlcoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]
fields = ['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies',
       'HvyAlcoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income']

record = pd.DataFrame(dict(zip(fields, values)), index=[0])

loaded_scaler = pickle.load(open('ss.sav', 'rb'))

record_scaled = loaded_scaler.transform(record)

# Now - predicting!
if st.button(label="Click to Predict"):

    # Load the model
    loaded_model = pickle.load(open('gbc2_model.sav', 'rb'))
    # Make predictions (and get out pred probabilities)
    pred = loaded_model.predict(record_scaled)[0]
    proba = loaded_model.predict_proba(record_scaled)[:,1][0]
    
    # Sharing the predictions
    if pred == 0:
        st.write("### You are not predicted to have diabetes")
        st.write(f"Predicted probability of diabetes: {proba*100:.2f} %")

    elif pred == 1:
        st.write("### You are predicted to have diabetes")
        st.write(f"Predicted probability of diabetes: {proba*100:.2f} %")
import mysql.connector
import streamlit as st
import numpy as np
import joblib 
import streamlit.components.v1 as components  # Import the components module


# Function to connect to MySQL Workbench
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",  # Change if your database is hosted remotely
        user="root",
        password="Disha@2002",
        database="practice"
    )

# Load the trained model
model = joblib.load("random_forest_diabetes.pkl")

# -------------------- Front Page (Landing Page) --------------------
def front_page():
    st.markdown("<h1 style='text-align: center;'>Welcome to the Diabetes Prediction App 🩺</h1>", unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])  # Adjust the ratio to control size

    with col1:
        st.write("""
            This application is designed to help predict the likelihood of having diabetes 
            based on key health metrics such as age, weight, height, and lifestyle habits. 
            By entering your details, you will receive a prediction of your health status: 
            **No Diabetes** or **Diabetes**.
            
            To get started, simply click the button below to proceed to the diabetes prediction form.
        """)

    with col2:
        st.image("Screenshot 2025-02-06 031937.png")  # Ensure the image file exists in your working directory
    
    # Button to navigate to the Prediction Page
    if st.button("Start Prediction"):
        st.session_state.page = "Prediction"

# Function to display the Tableau dashboard
def tableau_dashboard():
    st.title("Diabetes Data Explorer Dashboard")

    tableau_html = """
    <div class='tableauPlaceholder' id='viz1739223867426' style='position: relative'>
        <noscript>
            <a href='#'>
                <img alt=' ' src='https://public.tableau.com/static/images/Di/Diabetes_data_explorer/Dashboard1/1_rss.png' style='border: none' />
            </a>
        </noscript>
        <object class='tableauViz'  style='display:none;'>
            <param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
            <param name='embed_code_version' value='3' /> 
            <param name='site_root' value='' />
            <param name='name' value='Diabetes_data_explorer/Dashboard1' />
            <param name='tabs' value='yes' />
            <param name='toolbar' value='yes' />
            <param name='static_image' value='https://public.tableau.com/static/images/Di/Diabetes_data_explorer/Dashboard1/1.png' /> 
            <param name='animate_transition' value='yes' />
            <param name='display_static_image' value='yes' />
            <param name='display_spinner' value='yes' />
            <param name='display_overlay' value='yes' />
            <param name='display_count' value='yes' />
            <param name='language' value='en-US' />
            <param name='filter' value='publish=yes' />
        </object>
    </div>                
    <script type='text/javascript'>                    
        var divElement = document.getElementById('viz1739223867426');                    
        var vizElement = divElement.getElementsByTagName('object')[0];                    
        if (divElement.offsetWidth > 800) { 
            vizElement.style.width='100%'; 
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else if (divElement.offsetWidth > 500) { 
            vizElement.style.width='100%'; 
            vizElement.style.height=(divElement.offsetWidth*0.75)+'px';
        } else { 
            vizElement.style.width='100%'; 
            vizElement.style.minHeight='2400px'; 
            vizElement.style.maxHeight=(divElement.offsetWidth*1.77)+'px';
        }                     
        var scriptElement = document.createElement('script');                    
        scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
        vizElement.parentNode.insertBefore(scriptElement, vizElement);                
    </script>
    """

    # Render the Tableau dashboard in Streamlit
    components.html(tableau_html, height=800, width=1000)


def calculate_bmi(weight, height):    
    if height > 0:  # Ensure height is greater than zero to avoid division by zero
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    else:
        return "Height cannot be zero or negative"  # Return a message if height is zero or negative

# Function to generate age code based on age group
def generate_age_code(age):
    if 18 <= age <= 24:
        return 1
    elif 25 <= age <= 29:
        return 2
    elif 30 <= age <= 34:
        return 3
    elif 35 <= age <= 39:
        return 4
    elif 40 <= age <= 44:
        return 5
    elif 45 <= age <= 49:
        return 6
    elif 50 <= age <= 54:
        return 7
    elif 55 <= age <= 59:
        return 8
    elif 60 <= age <= 64:
        return 9
    elif 65 <= age <= 69:
        return 10
    elif 70 <= age <= 74:
        return 11
    elif 75 <= age <= 79:
        return 12
    elif age >= 80:
        return 13

# Convert income to scale based on INR
def convert_income_to_scale(income_inr):
    # income_in_usd_1 = 10000  # less than $10,000
    # income_in_usd_5 = 35000  # less than $35,000
    # income_in_usd_8 = 75000  # $75,000 or more
    
    # # Convert USD values to INR
    # income_inr_1 = income_in_usd_1 * 80
    # income_inr_5 = income_in_usd_5 * 80
    # income_inr_8 = income_in_usd_8 * 80
    
    # Determine the income scale based on INR
    # if income_inr < income_inr_1:
    #     return 1  # less than $10,000
    # elif income_inr < income_inr_5:
    #     return 5  # less than $35,000
    # elif income_inr >= income_inr_8:
    #     return 8  # $75,000 or more
    
    if income_inr < 10000:
        return 1
    elif 10000 <= income_inr < 15000:
        return 2
    elif 15000 <= income_inr < 20000:
        return 3
    elif 20000 <= income_inr < 25000:
        return 4
    elif 25000 <= income_inr < 35000:
        return 5
    elif 35000 <= income_inr < 50000:
        return 6
    elif 50000 <= income_inr < 75000:
        return 7
    elif income_inr >= 75000:
        return 8


# Function to insert data into MySQL
def insert_data(HighBP, HighChol, BMI, Stroke, HeartDiseaseorAttack, PhysActivity, 
                HvyAlcoholConsump, AnyHealthcare, GenHlth, PhysHlth, DiffWalk, Sex, 
                Age, Education, Income, Prediction):
    
    conn = connect_to_db()
    cursor = conn.cursor()

    # Ensure the table exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS health_data2 (
            id INT AUTO_INCREMENT PRIMARY KEY,
            HighBP INT,
            HighChol INT,
            BMI FLOAT,
            Stroke INT,
            HeartDiseaseorAttack INT,
            PhysActivity INT,
            HvyAlcoholConsump INT,
            AnyHealthcare INT,
            GenHlth INT,
            PhysHlth INT,
            DiffWalk INT,
            Sex INT,
            Age INT,
            Education INT,
            Income INT,
            Prediction VARCHAR(50),
            Timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Insert the data
    cursor.execute("""
        INSERT INTO health_data2 
        (HighBP, HighChol, BMI, Stroke, HeartDiseaseorAttack, PhysActivity, 
         HvyAlcoholConsump, AnyHealthcare, GenHlth, PhysHlth, DiffWalk, Sex, 
         Age, Education, Income, Prediction) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (HighBP, HighChol, BMI, Stroke, HeartDiseaseorAttack, PhysActivity, 
          HvyAlcoholConsump, AnyHealthcare, GenHlth, PhysHlth, DiffWalk, Sex, 
          Age, Education, Income, Prediction))

    conn.commit()
    cursor.close()
    conn.close()

# Prediction Page
def prediction_page():
    st.markdown("<h1 style='text-align: center;'>Diabetes Prediction App 🩺</h1>", unsafe_allow_html=True)
    st.write("Enter your health details below to predict the likelihood of diabetes.")

    # Input fields
    HighBP = st.selectbox("High Blood Pressure (0 = No, 1 = Yes)", [0, 1])
    HighChol = st.selectbox("High Cholesterol (0 = No, 1 = Yes)", [0, 1])
    BMI = st.number_input("Body Mass Index (BMI)", min_value=10.0, max_value=50.0, step=0.1)
    Stroke = st.selectbox("Ever had a Stroke? (0 = No, 1 = Yes)", [0, 1])
    HeartDiseaseorAttack = st.selectbox("Heart Disease or Heart Attack? (0 = No, 1 = Yes)", [0, 1])
    PhysActivity = st.selectbox("Physically Active? (0 = No, 1 = Yes)", [0, 1])
    HvyAlcoholConsump = st.selectbox("Heavy Drinker? (0 = No, 1 = Yes)", [0, 1])
    AnyHealthcare = st.selectbox("Has Healthcare Coverage? (0 = No, 1 = Yes)", [0, 1])
    GenHlth = st.slider("General Health (1 = Excellent to 5 = Poor)", 1, 5, 3)
    PhysHlth = st.slider("Number of days physical health was bad (0-30)", 0, 30, 0)
    DiffWalk = st.selectbox("Difficulty Walking? (0 = No, 1 = Yes)", [0, 1])
    Sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
    Age = st.number_input("Age")
    Education = st.slider("Education Level (1-6, see codebook)", 1, 6, 4)
    Income = st.number_input("Income Level")

    # Convert categorical values to numerical
    #HighBP = 1 if HighBP == "Yes" else 0
    #Smoker = 1 if Smoker == "Yes" else 0

    # Convert income and age
    a_income = convert_income_to_scale(Income)
    a_age = generate_age_code(Age)
    
    # Calculate BMI
    #BMI = calculate_bmi(Weight, Height)

    # Check if BMI is a valid number or an error message
    if BMI == "Height cannot be zero or negative":
        st.error(BMI)  # Show an error if BMI calculation fails
    else:
        # Prediction button
        if st.button("Predict"):
            # Create input feature array
            features = np.array([[HighBP,HighChol,BMI,Stroke,HeartDiseaseorAttack,PhysActivity,HvyAlcoholConsump,AnyHealthcare,GenHlth,PhysHlth,DiffWalk,Sex,a_age,Education,a_income]])

            # Make prediction
            prediction = model.predict(features)[0]

            # Convert prediction to readable text
            prediction_text = "No Diabetes" if prediction == 0 else "Diabetes" 

            # Store data in MySQL
            insert_data(HighBP, HighChol, BMI, Stroke, HeartDiseaseorAttack, PhysActivity, 
                    HvyAlcoholConsump, AnyHealthcare, GenHlth, PhysHlth, DiffWalk, Sex, 
                    a_age, Education, a_income, prediction_text)


            # Display result
            st.success(f"Prediction: **{prediction_text}**")


# Streamlit App
# -------------------- Main App Logic --------------------
def app():
    if "page" not in st.session_state:
        st.session_state.page = "Home"

    # Sidebar Navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Prediction", "Dashboard"])

    # Navigate to the selected page
    if page == "Home":
        front_page()
    elif page == "Prediction":
        prediction_page()
    elif page == "Dashboard":
        tableau_dashboard()

if __name__ == "__main__":
    app()



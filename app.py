import streamlit as st
from prediction import *

st.header('Student Prediction App (Prototype)')

data = pd.DataFrame()

col1, col2, col3, col4 = st.columns(4)
 
with col1:
    labels = {'Single':1, 'Married':2, 'Widower':3, 'Divorced': 4, 'Facto Union':5, 'Legally Separated':6} #encoder_Marital_status.classes_
    Marital_status = st.selectbox(label='Marital_status', options=list(labels.keys()), index=0)
    data["Marital_status"] = [labels[Marital_status]]
 
with col2:
    labels = {'No': 0, 'Yes': 1} #encoder_Debtor.classes_
    Debtor = st.selectbox(label='Debtor', options=list(labels.keys()), index=0)
    data["Debtor"] = [labels[Debtor]]

with col3:
    labels = {'No': 0, 'Yes': 1} #encoder_Displaced.classes_
    Displaced = st.selectbox(label='Displaced', options=list(labels.keys()), index=1)
    data["Displaced"] = [labels[Displaced]]

with col4:
    labels = {'Male': 0, 'Female': 1} #encoder_Gender.classes_
    Gender = st.selectbox(label='Gender', options=list(labels.keys()), index=1)
    data["Gender"] = [labels[Gender]]


col1, col2, col3, col4 = st.columns(4)
 
with col1:
    labels = {
        '1st phase - general contingent': 1,
        'Ordinance No. 612/93': 2,
        '1st phase - special contingent (Azores Island)': 5,
        'Holders of other higher courses': 7,
        'Ordinance No. 854-B/99': 10,
        'International student (bachelor)': 15,
        '1st phase - special contingent (Madeira Island)': 16,
        '2nd phase - general contingent': 17,
        '3rd phase - general contingent': 18,
        'Ordinance No. 533-A/99, item b2) (Different Plan)': 26,
        'Ordinance No. 533-A/99, item b3 (Other Institution)': 27,
        'Over 23 years old': 39,
        'Transfer': 42,
        'Change of course': 43,
        'Technological specialization diploma holders': 44,
        'Change of institution/course': 51,
        'Short cycle diploma holders': 53,
        'Change of institution/course (International)': 57
    } #encoder_Application_mode.classes_

    Application_mode = st.selectbox(label='Application_mode', options=list(labels.keys()), index=13)
    data["Application_mode"] = [labels[Application_mode]]
 
with col2:
    labels = {
        'Secondary education': 1,
        "Higher education - bachelor's degree": 2,
        'Higher education - degree': 3,
        "Higher education - master's": 4,
        'Higher education - doctorate': 5,
        'Frequency of higher education': 6,
        '12th year of schooling - not completed': 9,
        '11th year of schooling - not completed': 10,
        'Other - 11th year of schooling': 12,
        '10th year of schooling': 14,
        '10th year of schooling - not completed': 15,
        'Basic education 3rd cycle (9th/10th/11th year) or equiv.': 19,
        'Basic education 2nd cycle (6th/7th/8th year) or equiv.': 38,
        'Technological specialization course': 39,
        'Higher education - degree (1st cycle)': 40,
        'Professional higher technical course': 42,
        'Higher education - master (2nd cycle)': 43
    } #encoder_Previous_qualification.classes_
    Previous_qualification = st.selectbox(label='Previous_qualification', options=list(labels.keys()), index=0)
    data["Previous_qualification"] = [labels[Previous_qualification]]

with col3:
    labels = {'No': 0, 'Yes': 1} #encoder_Tuition_fees_up_to_date.classes_
    Tuition_fees_up_to_date = st.selectbox(label='Tuition_fees_up_to_date', options=list(labels.keys()), index=1)
    data["Tuition_fees_up_to_date"] = [labels[Tuition_fees_up_to_date]]

with col4:
    labels = {'No': 0, 'Yes': 1} #encoder_Scholarship_holder.classes_
    Scholarship_holder = st.selectbox(label='Scholarship_holder', options=list(labels.keys()), index=0)
    data["Scholarship_holder"] = [labels[Scholarship_holder]]


col1, col2, col3, col4 = st.columns(4)
 
with col1:
    Application_order = int(st.number_input(label='Application_order', value=2))
    data["Application_order"] = Application_order
 
with col2:
    Previous_qualification_grade = int(st.number_input(label='Prev_qualification_grade', value=130))
    data["Previous_qualification_grade"] = Previous_qualification_grade

with col3:
    Admission_grade = int(st.number_input(label='Admission_grade', value=159))
    data["Admission_grade"] = Admission_grade

with col4:
    Age_at_enrollment = int(st.number_input(label='Age_at_enrollment', value=25))
    data["Age_at_enrollment"] = Age_at_enrollment


col1, col2, col3 = st.columns(3)
 
with col1:
    Curricular_units_1st_sem_enrolled = int(st.number_input(label='Curricular_units_1st_sem_enrolled', value=7))
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled
 
with col2:
    Curricular_units_1st_sem_approved = int(st.number_input(label='Curricular_units_1st_sem_approved', value=7))
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved

with col3:
    Curricular_units_1st_sem_grade = float(st.number_input(label='Curricular_units_1st_sem_grade', value=11.857143))
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade


col1, col2, col3 = st.columns(3)
 
with col1:
    Curricular_units_2nd_sem_enrolled = int(st.number_input(label='Curricular_units_2nd_sem_enrolled', value=8))
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled
 
with col2:
    Curricular_units_2nd_sem_approved = int(st.number_input(label='Curricular_units_2nd_sem_approved', value=5))
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved

with col3:
    Curricular_units_2nd_sem_grade = float(st.number_input(label='Curricular_units_2nd_sem_grade', value=11.700000))
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade

with st.expander("View the Raw Data"):
    st.dataframe(data=data, width=800, height=10)

if st.button('Predict'):
    new_data = data_preprocessing(data=data)
    with st.expander("View the Preprocessed Data"):
        st.dataframe(data=new_data, width=800, height=10)
    st.write("Status: {}".format(prediction(new_data)))

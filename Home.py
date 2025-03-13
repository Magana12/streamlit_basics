import streamlit as st
import pandas as pd
import time as tym


@st.dialog("Details Form")
def details_form():
    username=st.text_input("Enter your username here: ")
    email=st.text_input("Email: ")
    if st.button("Submit Details"):
        st.write(f"Details on {username} has been submitted successfully")




st.write("This is my streamlit web application")
st.header("This is a header")
st.title("This is a title")
st.caption("This is a caption")
st.code("""
st.write("This is my streamlit web application")
st.header("This is a header")
st.title("This is a title")
st.caption("This is a caption here")
""")
with st.echo():
    st.write("This statement will be executed")

st.divider()
st.write("--------------")

#loading datasets with pandas
df=pd.read_csv("data.csv")
st.dataframe(df.head())

edited_df=st.data_editor(df)
st.dataframe(edited_df.head())


st.metric("Temperature", 26,2)
st.metric("Rainfall",1800,-200)

#Adding buttons
submit_button=st.button("Submit")
if submit_button:
    st.write("The button has been clicked")

feedback=st.feedback()
if feedback==0:
    st.write("The user dislikes the content")
elif feedback==1:
    st.write("The user likes the content")

stars=st.feedback("stars")
if stars or stars==0:
    if stars==0 or stars==1:
        st.write("Low rating")
    elif stars==2:
        st.write("Medium rating")
    elif stars>2:
        st.write("High rating")
terms=st.checkbox("I agree to the terms and conditions")
if terms:
    st.write("The user agrees to the terms and conditions")

st.toggle("Activate")
st.toggle("Dark mode")

#Radio button allows us to choose between options, can only choose one
gender=st.radio("Select your gender here: ",["Male", "Female","Other"])
if gender=="Male":
    st.write("the mens conference will be on 28th")
elif gender=="Female":
    st.write("the girls conference will be on 28th")

team=st.selectbox("Select your team here: ",["Liverpool","ManU","Arsenal","chelsea"])
if team=="Liverpool":
    st.write("You'll never walk alone")
elif team=="ManU":
    st.write("Glory glory man united")
elif team=="Arsenal":
    st.write("London is red")
elif team=="chelsea":
    st.write("London is blue")

#multiselect allows for multiple selection
breakfast=st.multiselect("what did you have for breakfast?: ",["Milk","Bread","Eggs","Tea"])
st.write(breakfast)

#select slider-allows for selection of categorical values which have a particular relationship
size=st.select_slider("Enter your size here: ",["S","M","L","XL","XXL"])
st.write(size)

age=st.number_input("enter your age here: ", min_value=18,max_value=50,value=25)
st.write(age)

number=st.slider("Enter a number here: ",min_value=1,max_value=100,value=50)
st.write(number)

#date input-picking dates, has an inbuilt calendar, can only go exactly +-10 years from the current date
date=st.date_input("Select the date for the appointment here: ")

#time input, has 15 mins interval and can type the exact specified time e.g 23:51
time=st.time_input("Enter time of the appointment here: ")

#taking text inputs from the user

#in st we have unique identifiers being passed,can't take duplicated
name=st.text_input("Enter your name here: ")
email=st.text_input("Enter your email here: ")
if st.button("Submit info"):
    st.write(f"The details on the {name} have been submitted successfully")

#text area is larger than text input and you can specify the size
essay=st.text_area("Write an essay here: ",height=300)
st.write(f"Number of characters: {len(essay)}")
st.write(f"Number of words: {len(essay.split())}")
#.split()-splits into the component words and can get length/number of words

uploaded_file=st.file_uploader("Upload your file here:")
st.write(uploaded_file)

# passport_photo=st.camera_input("Take a passport sized photo here: ")

st.image("image (14).png")

col1,col2,col3=st.columns(3)
with col1:
    f_name=st.text_input("first name")
with col2:
    s_name=st.text_input("second name")
with col3:
    t_name=st.text_input("third name")
st.write(f"{f_name} {s_name} {t_name}")

trigger=st.selectbox("Do you want to display the dialog box?",["No","Yes"])
if trigger=="Yes":
    details_form()

#when we don't want to show all the details to the customer, with has a lot of things/further details within them
with st.expander("Click to see details on the sale"):
    st.write("sale id: 6458764958")
    st.write("sale date: 23rd April 2025")
    st.write("sale amount: 6500")
    st.write("Customer id: CU645")

# with st.sidebar:
#     st.write("this is part of the sidebar")
#     st.write("this is also another part of the sidebar")
#     st.write("this is the last part of the sidebar")
#     st.button("Sidebar")

#notifying the user a process is happening behind the scenes
# with st.spinner("Operation in progress. Please wait."):
#     tym.sleep(1)
#     st.write("Operation complete")

#displayed on top right of the screen,emojis on streamlit emojis and get the shortcode
st.toast("You have  successfully logged in",icon="👍")


# st.balloons()

#callout messages-texts wrapped around colors
st.success("You have successfully logged in")
st.info("Upload a .csv or .tsv file")
st.warning("Exceeds the maximum word count")
st.error("Failed to load the image")


#mulptiple pages in the same web application
#project structure and create a new directory and name it pages(in lower case), appears on the sidebar
#pushing project to github using IDE







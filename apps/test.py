import streamlit as st 
import pandas as pd


st.title("Test Dashboard")
st.text("Welcome to Streamlit !")

st.subheader("Code")

code = """
x = 10
y = 20
print(x + y)
"""
st.code(code, language="python")

st.subheader("Data")

data = {
    "Name": ["Donald", "Joe", "George"],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)
st.dataframe(df)

st.subheader("Charts")

st.text("Line Chart")

line_data = pd.DataFrame({
    "Sales": [0, 100, 150, 130, 200, 300, 250, 400, 320, 500, 440]
})
st.line_chart(line_data)

st.text("Bar Chart")

bar_data = pd.DataFrame({
    "Product": ["iPhone17", "iPhone15", "iPhone16"],
    "Sales": [120, 180, 150]
})
st.bar_chart(bar_data, x="Product", y="Sales")

st.text("Map")

map_data = pd.DataFrame({
    "lat": [18.86, 19.07],
    "lon": [72.78, 72.90]
})
st.map(map_data)

st.subheader("Input Widgets")

if st.button("Click Me"):
    st.write("Button clicked!")

show_data = st.checkbox("Show Data")

if show_data:
    st.write("Data is visible.")

language = st.radio(
    "Choose a language",
    ["Python", "Java", "SQL"]
)

st.write("Selected:", language)

city = st.selectbox(
    "Choose a city",
    ["Delhi", "Mumbai", "Bengaluru"]
)

st.write("Selected city:", city)

skills = st.multiselect(
    "Choose your skills",
    ["Python", "SQL", "Spark", "BI"]
)

st.write("Selected Skills:", skills)

age = st.number_input(
    "Enter your age",
    min_value=1,
    max_value=100
)

st.write("Age:", age)

name = st.text_input("Enter your name")

if name:
    st.write("Hello", name)

message = st.text_area("Enter your message")

st.write("Message:", message)

dark_mode = st.toggle("Dark Mode")

st.write("Enabled:", dark_mode)

st.subheader("Image")

st.image(
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTryhJT8nr-5V1R1O4Y3V1TenCiPZe2VbTGOslqkfBJ9pw13Rk3RwjL-Ex&s=10",
    caption="Sample Image"
)

st.subheader("Containers")

col1, col2 = st.columns(2)

with col1:
    st.metric("Users", 1000)

with col2:
    st.metric("Revenue", "$25K")

st.sidebar.title("Filters")

category = st.sidebar.selectbox(
    "Choose Category",
    ["Agentic AI", "Generative AI"]
)

st.write("Selected:", category)

tab1, tab2 = st.tabs([
    "Overview",
    "Details"
])

with tab1:
    st.write("Overview")

with tab2:
    st.write("Details")

with st.expander("View Details"):
    st.write("Additional information is displayed here.")

container = st.container()

container.write("First container")
container.write("Second container")

st.header("Section 1")
st.write("Content")

st.divider()

st.header("Section 2")
st.write("More Content")

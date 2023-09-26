import streamlit
import pandas   

streamlit.title('YP Stores Welcomes you')

   

streamlit.header('Breakfast Menu')
streamlit.text(' 🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text(' 🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text(' 🐔 Hard-Boiled Free-Range Egg')
streamlit.text(' 🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_food_list = pandas.read_csv(https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt)
streamlit.data_frame(my_food_list)

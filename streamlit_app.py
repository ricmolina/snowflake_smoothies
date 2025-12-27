# Import python packages
import streamlit as st
import requests
from snowflake.snowpark.functions import col


# Write directly to the app
st.title(f":cup_with_straw: Pending Orders :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!.
  """
)

cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()


if ingredients_list:
  ingredients_string= ''

for fruit_chosen in ingredients_list:
  ingredients_string += fruit_chosen + ' '
  smoothiefroot_response = smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
  sf_df = st.dataframe(data=smoothiefroot_response.json(), use_container_width=True)


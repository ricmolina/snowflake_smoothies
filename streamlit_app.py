# Import python packages
import streamlit as st
import requests
from snowflake.snowpark.functions import col
from snowflake.snowpark.functions import when_matched


# Write directly to the app
st.title(f":cup_with_straw: Pending Orders :cup_with_straw:")
st.write(
  """Choose the fruits you want in your custom Smoothie!.
  """
)


#session = get_active_session()
cnx=st.connection("snowflake")
session=cnx.session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
#editable_df = st.data_editor(my_dataframe)
#st.dataframe(data=my_dataframe, use_container_width=True)
smoothiefroot_response = requests.get("https://my.smoothiefroot.com/api/fruit/watermelon")
st.text(smoothiefroot_response).json())

if my_dataframe:
  editable_df = st.data_editor(my_dataframe)
  submitted = st.button('Submit')
  if submitted:
    og_dataset = session.table("smoothies.public.orders")
    edited_dataset = session.create_dataframe(editable_df)
    try:
      og_dataset.merge(edited_dataset
                       , (og_dataset['ORDER_UID'] == edited_dataset['ORDER_UID'])
                       , [when_matched().update({'ORDER_FILLED': edited_dataset['ORDER_FILLED']})]
                      )
      st.success("Someon clicked the button.", icon='👍')
    except:
        st.write('Something went wrong.')
  else:
      st.success('There are no pending orders right now', icon='👍')


import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# Display Title and Description
st.title("Project Management Tool")

# Setup Google Sheets connection including the spreadsheet ID
conn = st.connection("gsheets", type=GSheetsConnection)

# Print to confirm the connection object
st.write("Connection Object:", conn)

try:
    # Attempt to read data from the specified sheet
    df = conn.read(sheet_name=sheet_name)
    st.write("Dataframe Loaded Successfully:", df.head())  # Display the first few rows of the dataframe

    # Display data
    for row in df.itertuples():
        st.write(f"{row.name} has a :{row.pet}:")
except Exception as e:
    # Print any error that occurs during the read operation
    st.error("Failed to load data from Google Sheets:")
    st.error(str(e))

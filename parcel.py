import streamlit as st
import pandas as pd

# Title of the app
st.title('Parcel Lookup App')

# Upload CSV file
uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)

    # Show the first few rows of the dataframe
    st.write("Here's a preview of your data:")
    st.write(df.head())

    # Ask user to input Parcel ID
    parcel_id = st.text_input('Enter Parcel ID:')

    # Check if Parcel ID exists in the dataframe
    if parcel_id:
        # Filter the dataframe based on Parcel ID
        filtered_data = df[df['ParcelID'] == parcel_id]

        # Show the result
        if not filtered_data.empty:
            st.write("Parcel details:")
            st.write(filtered_data)
        else:
            st.write("Parcel ID not found. Please check the ID and try again."
)
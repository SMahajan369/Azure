import streamlit as st
import pandas as pd

st.title("📑 Excel Sheet Viewer with Dropdown")

# Upload Excel file
uploaded_file = st.file_uploader("Upload an Excel file", type=["xlsx", "xls"])

# Proceed if a file is uploaded
if uploaded_file:
    try:
        # Load Excel file and get sheet names
        excel_file = pd.ExcelFile(uploaded_file)
        sheet_names = excel_file.sheet_names

        # Dropdown to select sheet
        selected_sheet = st.selectbox("Select a sheet", sheet_names)

        # Button to process
        if st.button("Process Data"):
            try:
                # Read selected sheet
                df = pd.read_excel(excel_file, sheet_name=selected_sheet)

                st.success(f"Displaying data from: {selected_sheet}")
                st.dataframe(df, use_container_width=True)
            except Exception as e:
                  st.error(f"Error reading selected sheet: {e}")

    except Exception as e:
        st.error(f"Failed to read Excel file: {e}")
else:
    st.info("Please upload an Excel file to begin.")

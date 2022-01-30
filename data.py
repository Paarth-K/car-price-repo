import numpy as np
import pandas as pd
import streamlit as st

def app(df):
	st.header("View Data")
	with st.expander("View Dataset: "):
		st.table(df)

	st.subheader("Column Description")
	beta_col1, beta_col2 = st.columns(2)

	with beta_col1:
		if st.checkbox("Show All Column Names"):
			st.table(df.columns)

	with beta_col2:
		if st.checkbox("View Column Data"):
			column_name = st.selectbox("Select Column Name", ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price'))
			st.write(df[column_name])

	if st.checkbox("View Summary"):
		st.table(df.describe())
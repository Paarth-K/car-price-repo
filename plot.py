# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

# Define a function 'app()' which accepts 'car_df' as an input.
all_features = ('carwidth', 'enginesize', 'horsepower', 'drivewheel_fwd', 'car_company_buick', 'price')
def app(car_df):
	st.header("Visualize Data")
	st.set_option("deprecation.showPyplotGlobalUse", False)
	plt.style.use("ggplot")

	st.subheader("Visualizer Selector")
	plots_to_plot = st.multiselect("Select Plots to Plot", ("Scatter Plot", "Box Plot", "Histogram", "Correlation Heatmap"))

	for i in plots_to_plot:
		exec(f"{i}(car_df)".replace(" ", ""))



def ScatterPlot(car_df):
	st.subheader("Scatter Plot")
	features = st.multiselect("Select X Axis Values", all_features, key="1")
	for i in features:
		st.subheader(f"Scatter Plot between {i} and Price")
		plt.figure(figsize=(10, 5), dpi=150)
		sns.scatterplot(x=i, y="price", data=car_df)
		st.pyplot()



def Histogram(car_df):
	st.subheader("Histogram")
	features = st.selectbox("Select X Axis Values", ("carwidth", "enginesize", "horsepower"), key="2")
	plt.figure(figsize=(10, 5), dpi=150)
	plt.hist(car_df[features], bins="sturges")
	st.pyplot()

def BoxPlot(car_df):
	st.subheader("Box Plot")
	features = st.selectbox("Select X Axis Values", ("carwidth", "enginesize", "horsepower"), key="3")
	plt.figure(figsize=(10, 5), dpi=150)
	sns.boxplot(car_df[features])
	st.pyplot()

def CorrelationHeatmap(car_df):
	st.subheader("Correlation Heatmap")
	plt.figure(figsize=(10, 5), dpi=150)
	sns.heatmap(car_df.corr(), annot=True)
	st.pyplot()


	

import pandas as pd
import numpy as np
import pickle
import streamlit as st
from PIL import Image

pickle_in = open('score_prediction1.pkl', 'rb')
pickler = pickle.load(pickle_in)

def predict_score(Battingteam,Bowlingteam,Currentscore,overs,Wickets,RunsinLast_5, WicketsinLast_5):
  temp_array = list()

  # Batting Team
  if Battingteam == 'India':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif Battingteam == 'Sri Lanka':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif Battingteam == 'South Africa':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif Battingteam == 'Australia':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif Battingteam == 'Pakistan':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif Battingteam == 'West Indies':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif Battingteam == 'England':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif Battingteam == 'New Zealand':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  # Bowling Team
  if Bowlingteam == 'India':
    temp_array = temp_array + [1,0,0,0,0,0,0,0]
  elif Bowlingteam == 'Sri Lanka':
    temp_array = temp_array + [0,1,0,0,0,0,0,0]
  elif Bowlingteam == 'South Africa':
    temp_array = temp_array + [0,0,1,0,0,0,0,0]
  elif Bowlingteam == 'Australia':
    temp_array = temp_array + [0,0,0,1,0,0,0,0]
  elif Bowlingteam == 'Pakistan':
    temp_array = temp_array + [0,0,0,0,1,0,0,0]
  elif Bowlingteam == 'West Indies':
    temp_array = temp_array + [0,0,0,0,0,1,0,0]
  elif Bowlingteam == 'England':
    temp_array = temp_array + [0,0,0,0,0,0,1,0]
  elif Bowlingteam == 'New Zealand':
    temp_array = temp_array + [0,0,0,0,0,0,0,1]

  # Overs, Runs, Wickets, Runs_in_prev_5, Wickets_in_prev_5
  temp_array = [Currentscore,overs, Wickets, RunsinLast_5, WicketsinLast_5] + temp_array
  # Converting into numpy array
  temp_array = pd.DataFrame([temp_array])

  # Prediction
  return int(pickler.predict(temp_array))
  
def main():
	html_temp = ""
	st.markdown(html_temp, unsafe_allow_html = True)
      	
	st.title("Cricket Score Predictor !")

	st.header(" Predict the final score of a cricket match- during the match")

	Battingteam = st.selectbox("Batting Team:", ['India','England','Australia','Sri Lanka','Pakistan','New Zealand','South Africa','West Indies'])	
	Bowlingteam = st.selectbox("Bowling Team:", ['India','England','Australia','Sri Lanka','Pakistan','New Zealand','South Africa','West Indies'])

	Currentscore= st.number_input('Enter the current score', min_value=0, step=1)
	overs = st.number_input('Enter the overs bowled', min_value=5, max_value=20, step=1)
	Wickets = st.number_input("Enter the wickets taken so far", min_value=0, max_value=9 , step=1)
	RunsinLast_5 = st.number_input("Enter the runs scored in last 5 overs", min_value=0, step=1)
	WicketsinLast_5 = st.number_input("Enter the wickets taken in last 5 overs", min_value=0, max_value=9 , step=1)
	result =""
	if st.button("Predict"):
		result = predict_score(Battingteam,Bowlingteam,Currentscore,overs,Wickets,RunsinLast_5, WicketsinLast_5)
	st.success('The final predicted score is {}'.format(result))
     
if __name__=='__main__':
    main()

  
import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import random
import os
import json

text = ""
correct_answer = 0
check =0
num_question = 0
video_id = st.text_input("Send YouTube video Id")
st.write("For example You can J82z1hkl3Bo or 1ooqsxtdGS0")
num_question =10 #st.text_input("How many questions Do you Want? [1,10]")

if st.button("next"):
  txtfile_name = video_id + ".json"
  print("here",txtfile_name)
  file_path = "C:\Future\\for git\\Quiz_Scribe\\" + txtfile_name
  
  if  os.path.exists(file_path):
    with open(file_path) as f:
      text = json.load(f)
      
  else:
      dictSubtitle = YouTubeTranscriptApi.get_transcript(video_id) 
      general_text = " ".join(i['text'] for i in dictSubtitle)
      for i in dictSubtitle:
       general_text += " " + i['text']
      client = OpenAI()
      completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "system", "content": f"I am sending you a text.you MUST represent 10 quetion,the questions and  send answers as json file.  which qontainn keys and values like: \"qeuestion\",\"A\":answer,\"B\":answer,\"C\":answer,\"D\":answer, correct: same  answer which is correct: TEXT{general_text}"},
          #{"role": "user", "content": f"{generalText}"}
      ]
      )

      quizfile_json = json.loads(completion.choices[0].message.content)
      with open(file_path, "w") as json_file:
        json.dump(quizfile_json, json_file)
      with open(file_path, "r") as json_file:
        text = json.load(json_file)

  quiz_Text = text 


# TODO Tab size issue 
  for i in range(num_question):
    question_text = str(i+1) + ". " + quiz_Text["questions"][i]["question"]
    answer = quiz_Text["questions"][i]["correct"]
    option = st.radio(label= question_text,options = (quiz_Text["questions"][i]["A"], quiz_Text["questions"][i]["B"], quiz_Text["questions"][i]["C"], quiz_Text["questions"][i]["D"])
      )          
    
    
    
        
    
    


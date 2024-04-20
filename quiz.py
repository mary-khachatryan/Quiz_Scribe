import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import random
import os
correct_answer = 0
check =0

video_id = st.text_input("Send YouTube video Id")
num_question = int(st.text_input("How many questions Do you Want? [1,10]"))
 
if st.button("next"):
  txtfile_name = video_id + ".txt"
  print("here",txtfile_name)
  file_path = "C:\Future\\for git\\Quiz_Scribe\\" + txtfile_name
  check = 1
  if  os.path.exists(file_path):
    with open(file_path, "r") as f:
      text = f.read()
  else:
      dictSubtitle = YouTubeTranscriptApi.get_transcript(video_id) 
      general_text = " ".join(i['text'] for i in dictSubtitle)
      for i in dictSubtitle:
        general_text += " " + i['text']
      client = OpenAI()
      completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
      {"role": "system", "content": f"I am sending you a text.you MUST represent 10 quetion,the questions and answers as a list of dicts in Python in this way: like json file. without python``` and without numbering, only listof dicts: answers must did not have \"symbol \"qeuestion\",\"A\":answer,\"B\":answer,\"C\":answer,\"D\":answer, correct: same  answer which is correct: TEXT{general_text}"},
        #{"role": "user", "content": f"{generalText}"}
      ]
      )

      with open(file_path, "w") as f:
        f.write(completion.choices[0].message.content)
      with open(file_path, "r") as f:
        text = f.read()

  quiz_Text = eval(text) 

# TODO Tab size issue 
for i in range(0,num_question):
    question_text = str(i+1) + ". " + quiz_Text[i]["question"]
    answer = quiz_Text[i]["correct"]
    option = st.radio(label= question_text,options = (quiz_Text[i]["A"], quiz_Text[i]["B"], quiz_Text[i]["C"], quiz_Text[i]["D"])
    )          
    if(option == answer):
      correct_answer+=1
if st.button("Submit"):
     st.write("correct_answer",correct_answer)
    


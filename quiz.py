import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import random
import os
correct_answer = 0


dictSubtitle = YouTubeTranscriptApi.get_transcript('1ooqsxtdGS0') 
generalText = " ".join(i['text'] for i in dictSubtitle)
for i in dictSubtitle:
   generalText += " " + i['text']
 
client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
  {"role": "system", "content": f"I am sending you a text.you MUST represent 10 quetion,the questions and answers as a list of dicts in Python in this way: like json file. without python``` and without numbering, only listof dicts: answers must did not have \"symbol \"qeuestion\",\"A\":answer,\"B\":answer,\"C\":answer,\"D\":answer, correct: same  answer which is correct: TEXT{generalText}"},
    #{"role": "user", "content": f"{generalText}"}
  ]
)
path_file = 'C:\Future\\for git\Quiz_Scribe\q.txt' # os path join
# print("pf",path_file)
# if os.path.exists('q.txt'):
#    os.remove(path_file)

# with open('q.txt', "x") as f:
#     f.write(completion.choices[0].message.content)
#     #\text = f.read()
# with open('q.txt', "r") as f:
#    text = f.read()
# print(text)
# def load_quiz_text():
#    return eval(tex  
text = completion.choices[0].message.content
quiz_Text = eval(text) #load_quiz_text()

# TODO Tab size issue 


for i in range(10):
  question_text = str(i+1) + ". " + quiz_Text[i]["question"]
  answer = quiz_Text[i]["correct"]
  option = st.radio(label= question_text,options = (quiz_Text[i]["A"], quiz_Text[i]["B"], quiz_Text[i]["C"], quiz_Text[i]["D"])
  )          
  if(option == answer):
    correct_answer+=1
if st.button("Submit"):
   st.write("correct_answer",correct_answer)

   




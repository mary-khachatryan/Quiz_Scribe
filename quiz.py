import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import random
correct_answer = 0


dictSubtitle = YouTubeTranscriptApi.get_transcript('dQw4w9WgXcQ') 
generalText = " ".join(i['text'] for i in dictSubtitle)
for i in dictSubtitle:
   generalText += " " + i['text']

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
  {"role": "system", "content": f"I am sending you a text.you MUST represent 10 quetion,the questions and answers as a list of dicts in Python in this way: like json file. without python``` and without numbering, only listof dicts: answers must did not have \"symbol \"qeuestion\",\"A\":answer,\"B\":answer,\"C\":answer,\"D\":answer, correct: same  answer which is correct: TEXT{generalText}"},
    {"role": "user", "content": f"{generalText}"}
  ]
)

quiz_Text = eval(completion.choices[0].message.content)

print(quiz_Text)
for i in range(10):

  question_text = str(i+1) + ". " + quiz_Text[i]["question"]
  answer = quiz_Text[i]["correct"]
  option =st.radio(
    label= question_text,
    options = (quiz_Text[i]["A"], quiz_Text[i]["B"], quiz_Text[i]["C"], quiz_Text[i]["D"])
  )
  if(option == answer):
      correct_answer+=1

if(st.button("Submit")):
   st.write("correct_answer",correct_answer)




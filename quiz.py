import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi

correct_answer = 0


dictSubtitle = YouTubeTranscriptApi.get_transcript('dQw4w9WgXcQ') 
generalText = " ".join(i['text'] for i in dictSubtitle)
for i in dictSubtitle:
   generalText += " " + i['text']
#print(generalText)

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
  {"role": "system", "content": f"I am sending you a text.you MUST represent 10 quetion,the questions and answers as a list of dicts in Python in this way: like json file. without python``` and without numbering, only listof dicts: answers must did not have \"symbol \"qeuestion\",\"A\":answer,\"B\":answer,\"C\":answer,\"D\":answer, correct: same  answer which is correct: TEXT{generalText}"},
    {"role": "user", "content": f"{generalText}"}
  ]
)

quiz_Text = completion.choices[0].message.content
print(quiz_Text)
quiz_Text1 = eval(quiz_Text)

print(2,(quiz_Text1[1]["question"]))
for i in range(9):
   st.text(quiz_Text1[i]["question"])
   st.button(quiz_Text1[i]["A"])
   st.button(quiz_Text1[i]["B"])
   st.button(quiz_Text1[i]["C"])
   st.button(quiz_Text1[i]["D"])
#print(3,quiz_Text[1]["question"])
# if st.button(quiz_Text[1]):
#   st.write('Why hello there')
# else:
#   st.write('Goodbye')
# name = st.text_input("HEy heey")




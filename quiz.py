import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi



dictSubtitle = YouTubeTranscriptApi.get_transcript('xnfWVZtFYJU') 
generalText = ''
for i in dictSubtitle:
    for k,v in i.items():
        if k ==  'text':
            generalText += ' '
            generalText += v
print(generalText)

client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"I am sending you a text, after the word TEXT, your job is to formulate 10 questions about the content of that text, after each question write 4 answers, only one of which is correct, write *Correct*  after correct answer,and always Number the answers.like this and always write qwuetion and their number,  question1. and in new line :1.answer,2.answer..,2 Quetion 1.answer.TEXT{generalText}"},
   # {"role": "user", "content": "CHEESE"}
  ]
)

quiz_Text = completion.choices[0].message.content
name = st.text_input("HEy heey")



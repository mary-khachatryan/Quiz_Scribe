import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi



dictSubtitle = YouTubeTranscriptApi.get_transcript('xnfWVZtFYJU') 
generalText = " ".join(i['text'] for i in dictSubtitle)
#for i in dictSubtitle:
#    generalText += " " + i['text']
#print(generalText)

client = OpenAI()
completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": f"I am sending you a text. After the word TEXT, your job is to formulate 10 questions about the content of that text. After each question, write 4 answers, only one of which is correct. Write Correct (that should be in a random number) after the correct answer. Always number the answers. Like this, and always write the question and its number. For example: Question 1. Answer 1. Answer 2. Answer 3. Answer 4.TEXT{generalText}"},
   # {"role": "user", "content": "CHEESE"}
  ]
)

quiz_Text = completion.choices[0].message.content
print(quiz_Text)
name = st.text_input("HEy heey")



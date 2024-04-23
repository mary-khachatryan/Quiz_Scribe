import openai
import streamlit as st
from openai import OpenAI
from youtube_transcript_api import YouTubeTranscriptApi
import os
import json
player_name = None
video_id = None
with open("iterator.txt",'r+') as f:
      num_question = f.read()

int_num_question = int(num_question)
if(int_num_question == 0):
   player_name = st.text_input("Your name and surname")
   video_id = st.text_input("Send YouTube video Id")
   st.write("For example You can J82z1hkl3Bo or 1ooqsxtdGS0")
   countof_question = 10 #st.text_input("How many questions Do you Want? [1,10]")
   current_directory = os.getcwd()
   print(current_directory,"::::::::")
   if st.button("Play"):
    directory = ".."  # Root directory
    subdirectories = ["Quiz_Scribe"]
    file_name = f"{video_id}.json"
    answer_name = f"{player_name}_answer.txt"
    file_path = os.path.join(directory, *subdirectories, file_name)
    answer_path = os.path.join(directory, *subdirectories, answer_name)
  
    if  os.path.exists(file_path):
      with open(file_path) as f:
        quiz_Text = json.load(f)
      with open("copy.json","w") as f:
        json.dump(quiz_Text,f)
        #copy_text = json.load(f)
       
  

      
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
        quiz_Text = json.load(json_file)
      with open("copy.json","r+") as f:
        f.write(quiz_Text)
        copy_text = json.load(f)
    question_text = str(int_num_question+1) + ". " + quiz_Text["questions"][int_num_question]["question"]
    answer = quiz_Text["questions"][int_num_question]["correct"]
    option = st.radio(label= question_text,options = (quiz_Text["questions"][int_num_question]["A"], quiz_Text["questions"][int_num_question]["B"], quiz_Text["questions"][int_num_question]["C"], quiz_Text["questions"][int_num_question]["D"])
    )
    
    if st.button('Next'):

      
      with open("iterator.txt",'w') as f:
        num_question = str(int_num_question)
        f.write(num_question)
      if int_num_question > 10:
        st.write(int_num_question,"verj ape jan")
      int_num_question +=1
else:
   with open("copy.json") as f:
        quiz_Text = json.load(f)
   question_text = str(int_num_question+1) + ". " + quiz_Text["questions"][int_num_question]["question"]
   answer = quiz_Text["questions"][int_num_question]["correct"]
   option = st.radio(label= question_text,options = (quiz_Text["questions"][int_num_question]["A"], quiz_Text["questions"][int_num_question]["B"], quiz_Text["questions"][int_num_question]["C"], quiz_Text["questions"][int_num_question]["D"])
   )
   
   
   if int_num_question > 10:
    st.write(int_num_question,"verj ape jan")
    with open("iterator.txt",'w') as f:
      num_question = str(int_num_question)
      f.write(num_question)
int_num_question +=1
if st.button('Next'):

      
      with open("iterator.txt",'w') as f:
        num_question = str(int_num_question)
        f.write(num_question)
      if int_num_question > 10:
        st.write(int_num_question,"verj ape jan")
      int_num_question +=1

     
    
    
        
    
    


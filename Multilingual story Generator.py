import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
#session state
if "model" not in st.session_state:
st.session_state["model"]=init_chat_model(model="llama-3.3-70bversatile",model_provider="groq",api_key="gsk_......................................") #place your gorq api key 
here
if "template" not in st.session_state:
st.session_state["template"]=PromptTemplate(
input_variables=["language","tone","storyIdea","length","grammar","plagarism","catagories","chara
cter_names","time_period","creativity","audience"],
template="Act like a professional story writer, who writes fantastic stories that target auidence 
of {audience}. write story in langaugage {language}, even the words ypur output must be in {language}, 
even though the input given to you is in English. and follow the specifi tone of {tone}. Be creativity and 
engaging where the creativity level is {creativity}. the time period of the story is {time_period}. 
Grammar level should be in {grammar}. maintain the given {plagarism} level. Avoid emojis. The length 
of the story should be {length}. the story should be on {storyIdea} and the category of the story is 
{catagories}. The story contains the following character names {character_names}"
)
language=st.sidebar.pills("Enter 
Language",["English","Telugu","Hindi","Tamil","Urdu","Kannada","Chinese"])
tone=st.sidebar.segmented_control("Select Tone",["Friendly","Narrative","Poet"])
storyIdea=st.sidebar.text_area("Tell me about your story idea")
length=st.sidebar.slider("Enter Number Of Paragraphs",1,10)
grammar=st.sidebar.selectbox("Specify grammar",["beginner","intermediate","professional"])
plagarism=st.sidebar.slider("Specify Plagrism",0,100)
categories=st.sidebar.radio("Specify 
Category",["Thriller","Horror","Suspense","Adventure","Comed
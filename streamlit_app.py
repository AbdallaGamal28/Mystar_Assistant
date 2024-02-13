import streamlit as st 
from langchain.llms import OpenAI
import os

st.title("My_STAR ⭐️ AI assistant")
         
openai_api_key = st.sidebar.text_input('OpenAI API Key')

def generate_response(input_text):
  client = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a software test engineer in mystar team."},
    {"role": "user", "content": "Who is relevant assignee for this topic"},
    {"role": "assistant", "content": "You should be able to tell the team and the assignee name"},
    {"role": "user", "content": "who is the responsible person?"}
  ]
)
# Directory containing the files
directory_path = '/content/mystar_assistant'

# List all files in the directory
all_file_names = [os.path.join(directory_path, f) for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

# Initialize OpenAI client (ensure you have set your API key)
client = openai.OpenAI(api_key="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")

# Upload files and collect file IDs
file_ids = []
for file_name in all_file_names:
    with open(file_name, 'rb') as file:
        response = client.files.create(file=file, purpose='assistants')
        file_ids.append(response.id)  # Access the id attribute

# Now file_ids contains the IDs of all uploaded files



st.info(input_text)

with st.form('my_form'):
  text = st.text_area('Enter text:', 'How can I assist you')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠️') 
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

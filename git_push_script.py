import os
import openai

# Directory containing the files
directory_path = '~/documents'

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
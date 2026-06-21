import gdown
from langchain_cohere import ChatCohere
from langchain_core.prompts import PromptTemplate

# Download file from Google Drive
# Replace with your actual Google Drive file ID
file_id = "1xnfosewraVuKewjjWXeBiNAUPj2ou7Zr"
url = f"https://drive.google.com/uc?id={file_id}"
gdown.download(url, "sample.txt", quiet=False)

# Read file
with open("sample.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Cohere LLM
llm = ChatCohere(
    cohere_api_key="XXXX",
    model="command-a-plus-05-2026"
)

# Prompt Template
prompt = PromptTemplate(
    input_variables=["text"],
    template="""
{text}

Give the output in exactly this format:

Generated Summary:
<brief summary in 3-4 lines>
"""
)

# Generate Response
response = llm.invoke(prompt.format(text=text))

# Extract only the generated text
for item in response.content:
    if item["type"] == "text":
        summary = item["text"]
        break

# Display Output
print("\nGenerated Output:\n")
print(summary)
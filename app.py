from flask import Flask, request, jsonify
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
from decouple import config

app = Flask(__name__)

# Load HuggingFace API token from environment variables
HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')

# Initialize the prompt template and LLM
template = "<s>[INST]Write short answer of</s>{question}[/INST]"
prompt_template = PromptTemplate.from_template(template)
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)

# Define the route for POST requests
@app.route('/generate-response', methods=['POST'])
def generate_response():
    # Get the prompt from the POST request
    data = request.json
    humanQue = data.get("prompt")

    # Format the prompt using the template
    formatted_prompt_template = prompt_template.format(question=humanQue)

    # Get the response from the model
    response_stream = llm.stream(formatted_prompt_template)
    response_text = "".join([res for res in response_stream])

    # Return the response as JSON
    return jsonify({"response": response_text})



# from langchain_core.prompts import PromptTemplate
# from langchain_community.llms import HuggingFaceEndpoint
# from decouple import config
# HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')

# template = "<s>[INST]Write short answer of</s>{question}[/INST]"
# # print(template)

# humanQue = input()

# prompt_template = PromptTemplate.from_template(template)
# formatted_prompt_template = prompt_template.format(
#     question=humanQue
# )

# # print(formatted_prompt_template)

# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
# llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)
# # response = llm.invoke(formatted_prompt_template)
# # print(response) 

# # streamming
# response = llm.stream(formatted_prompt_template)
# for res in response:
#     print(res, end="", flush=True)


##### Old Code Up

from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceEndpoint
from decouple import config

HUGGINGFACEHUB_API_TOKEN = config('HUGGINGFACEHUB_API_TOKEN')

template = "<s>[INST]Write short answer of</s>{question}[/INST]"

prompt_template = PromptTemplate.from_template(template)

# Initialize LLM once at the start
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"
llm = HuggingFaceEndpoint(repo_id=repo_id, huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN)

while True:
    humanQue = input("Ask a question (or type 'exit' to quit): ")

    # Exit loop if user types 'exit'
    if humanQue.lower() == 'exit':
        break

    # Format the prompt with the user input
    formatted_prompt_template = prompt_template.format(question=humanQue)

    # Stream the response
    response = llm.stream(formatted_prompt_template)
    for res in response:
        print(res, end="", flush=True)

    print("\n")  # For better formatting after each response

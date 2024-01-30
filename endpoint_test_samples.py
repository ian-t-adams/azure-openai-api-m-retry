from openai import AzureOpenAI

azure_openai_key: str = "{KEY_FOR_YOUR_APIM_SUBSCRIPTION}"
azure_open_endpoint: str = "{YOUR_APIM_ENDPOINT}"

aoai_api_version: str = "2023-12-01-preview"

# Define the AzureOpenAI client object
client = AzureOpenAI(
  azure_endpoint=azure_open_endpoint,
  api_key=azure_openai_key,
  api_version=aoai_api_version
)

# Chat Completions model test

aoai_chat_model: str = "gpt-4-turbo" # Put in the {deployment_id} name you used during your deployment of the API
aoai_temp_value: str = 0.75
aoai_top_p_value: str = 0.95

system_role_message = {
  "role": "system",
  "content": "You are an AI assistant that helps people find information."
}

user_message_esg = {
  "role": "user",
  "content": "Tell me a joke about the Azure API Management Service?"
}

response = client.chat.completions.create(
    model=aoai_chat_model,
    messages=[
        system_role_message,
        user_message_esg
    ],
    stream=False,
    temperature=aoai_temp_value,
    top_p=aoai_top_p_value
)
assistant_response=response.choices[0].message.content
print(f"{aoai_chat_model}'s joke was: " + "\n" + "\n" + assistant_response)

# Embeddings Test
response = client.embeddings.create(
    input = "Your text string goes here",
    model= "text-embedding-ada-002" # Put in the {deployment_id} name you used during your deployment of the API, probably text-embedding-ada-002 for this one
)

print(response.model_dump_json(indent=2))

# Gpt-4v
aoai_gpt4v_model: str = "gpt-4v" # You may need to change this to the {deployment_id} name you used during your deployment of the API

response = client.chat.completions.create(
    model=aoai_gpt4v_model,
    messages=[
        { "role": "system", "content": "You are a helpful assistant." },
        { "role": "user", "content": [  
            { 
                "type": "text", 
                "text": "Is there a flag in this photo?" 
            },
            { 
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/3/39/AS12-47-6983_%2821668759581%29.jpg"
                }
            }
        ] } 
    ],
    max_tokens=2000 
)

print(response)
from ollama import chat

from ollama import Client
client = Client(host='http://ollama:11434')

print("running...")

response = client.chat(
model="qwen2.5vl", #instead change to qwen when done. qwen2.5vl
#response = client.chat(
#    model = "llama3.2-vision:11b",
    messages=[
        {
            "role": "user",
            "content": """
            Describe the scene in as much detail as possible.
            Include:
            - People
            - Objects
            - Actions
            - Environments
            - Visible emotions if clearly visible

            Do not infer motivations or events that are not dirently seen in the image. 
            Return a single paragraph description of the scene.
            """,
            "images": ["./exampleGDELT.png"],
        }
    ],
    stream=True,
)

print("message complete...")

for chunk in response:
    print(chunk.message.content, end="", flush=True)
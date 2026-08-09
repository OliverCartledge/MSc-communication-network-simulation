from ollama import chat

from ollama import Client
client = Client(host='http://ollama:11434')

PROMOPTS = {
    "neutral" : """
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
    "positive" : """
    Describe the scene in as much detail as possible with a positive outlook.
        Include:
        - People
        - Objects
        - Actions
        - Environments
        - Visible emotions if clearly visible
    
        Do not infer motivations or events that are not dirently seen in the image. 
        Return a single paragraph description of the scene.

    """,
    "negative" : """
    Describe the scene in as much detail as possible with a negative outlook.
        Include:
        - People
        - Objects
        - Actions
        - Environments
        - Visible emotions if clearly visible
    
        Do not infer motivations or events that are not dirently seen in the image. 
        Return a single paragraph description of the scene.
    """
}

def describeImage(actor, role):

    systemPrompt = PROMOPTS[role]

    response = client.chat(
    model="qwen2.5vl",
    #response = client.chat(
    #    model = "llama3.2-vision:11b",
        messages=[
            {
                "role": "user",
                "content": systemPrompt,
                "images": [f"./generateTesting{actor}.png"],
            }
        ],
        stream=False,
    )

    
    print("\n\nTesting image analysis:\n")

    fullResponse = response.message.content
    print(fullResponse)

    return fullResponse
        
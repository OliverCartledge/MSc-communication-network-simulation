from ollama import chat

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

    response = chat(
        model="qwen2.5vl",
        messages=[
            {
                "role": "user",
                "content": systemPrompt,
                "images": [f"./generateTesting{actor}.png"],
            }
        ],
        stream=True,
    )

    fullResponse = ""

    print("\n\nTesting image anaylsis:\n")

    for chunk in response:
        #print(chunk.message.content, end="", flush=True)
        fullResponse += chunk.message.content

    return fullResponse
        
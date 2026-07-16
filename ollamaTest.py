from ollama import chat

response = chat(
    model='llama3.1',
    messages=[{'role': 'user', 'content': 'Rewrite this setnence using a small amount of semantic shift in a negative direction. "A lackluster rally fizzled out on the universitys quad."!'}],
    stream= True
)

for chunk in response:
    print(chunk.message.content, end="", flush=True)
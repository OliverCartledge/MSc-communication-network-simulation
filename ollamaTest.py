# ollama vision model notes: https://ollama.com/library/llama3.2-vision

from ollama import chat

response = chat(
    model="llava",
    messages=[
        {
            "role": "user",
            "content": "Describe this image in a sentence.",
            "images": ["./exampleOctQwen.png"],
        }
    ],
    stream=True,
)

for chunk in response:
    print(chunk.message.content, end="", flush=True)
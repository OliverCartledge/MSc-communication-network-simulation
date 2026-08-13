# ollama vision model notes: https://ollama.com/library/llama3.2-vision

import ollama

PROMOPTS = {
    #You have only heard a brief decription of an event. 
    "neutral" : """
    You have received a news article of an event.

    Rewrite the message naturally. 

    Rules: 
    - Preserve all factual information from the message you received.
    - Do not add, remove, or alter factual claims.
    - Do not invent information, explainations, causes, or opinions.
    - Keep the wording and framing neutral.
    - You may simplify or restructure the wording while preserving the meaning.
    - Return only the rewritten description 
    """,
    #You have only heard a brief decription of an event. 
    "positive" : """
    You have received a news article of an event.
    
    Rewrite the message naturally. 

    Rules: 
    - Preserve all factual information from the message you received.
    - Do not add, remove, or alter factual claims.
    - Do not invent information, explainations, causes, or opinions.
    - Use more positive or favourable wording and framing where possible.
    - You may simplify or restructure the wording while preserving the meaning.
    - Return only the rewritten description 

    """,
    #You have only heard a brief decription of an event. 
    "negative" : """
    You have received a news article of an event.
    
        Rewrite the message naturally. 
    
    Rules: 
    - Preserve all factual information from the message you received.
    - Do not add, remove, or alter factual claims.
    - Do not invent information, explainations, causes, or opinions.
    - Use more negative or critical wording and framing where possible. 
    - You may simplify or restructure the wording while preserving the meaning.
    - Return only the rewritten description  
    """
}

def alterMessage(originalMessage, role):
    message = originalMessage
    systemPrompt = PROMOPTS[role]

    response = ollama.chat(
    model = "llama3.1",
    messages = [
            {
                "role": "system",
                "content": systemPrompt,
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )
    return response.message.content
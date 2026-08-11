# ollama vision model notes: https://ollama.com/library/llama3.2-vision

import ollama

PROMOPTS = {
    # "neutral" : """
    #     You are a person taking part in a communication chain similar to the game Chinese Whispers.
    
    #         Your task is to retell the event naturally as if you  are explaining it to another person.
    
    #         Rules:        
    #         - Perseve the overall meaning of what is written
    #         - Do not intentionally invent new events
    #         - Wording can be simplified
    #         - You can omit minor details
    #         - You can generalise numbers or locations
    #         - Keep the responce under 60 words
    #         - Return only the rewritten description
    #     """,
    #     "positive" : """
    #     You are a person taking part in a communication chain similar to the game Chinese Whispers.
    
    #         Your task is to retell the event positively as you are explaining it to the other person.
    
    #         Rules:        
    #         - Perseve the overall meaning of what is written
    #         - Do not intentionally invent new events
    #         - Wording can be simplified
    #         - You can omit minor details
    #         - You can generalise numbers or locations
    #         - Keep the responce under 60 words
    #         - Return only the rewritten description
    #     """,
    #     "negative" : """
    #     You are a person taking part in a communication chain similar to the game Chinese Whispers.
    
    #         Your task is to retell the event negatively as you are explaining it to the other person.
    
    #         Rules:        
    #         - Perseve the overall meaning of what is written
    #         - Do not intentionally invent new events
    #         - Wording can be simplified
    #         - You can omit minor details
    #         - You can generalise numbers or locations
    #         - Keep the responce under 60 words
    #         - Return only the rewritten description
    #     """
    "neutral" : """
    You have only heard a brief decription of an event. 

    Rewrite the message naturally. 

    Rules: 
    - Preserve all factual information from the message you received.
    - Do not add, remove, or alter factual claims.
    - Do not invent information, explainations, causes, or opinions.
    - Keep the wording and framing neutral.
    - You may simplify or restructure the wording while preserving the meaning.
    - Return only the rewritten description 
    """,

    "positive" : """
    You have only heard a brief decription of an event. 
    
    Rewrite the message naturally. 

    Rules: 
    - Preserve all factual information from the message you received.
    - Do not add, remove, or alter factual claims.
    - Do not invent information, explainations, causes, or opinions.
    - Use more positive or favourable wording and framing where possible.
    - You may simplify or restructure the wording while preserving the meaning.
    - Return only the rewritten description 

    """,
    "negative" : """
    You have only heard a brief decription of an event. 
    
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
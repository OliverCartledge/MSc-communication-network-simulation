# ollama vision model notes: https://ollama.com/library/llama3.2-vision

import ollama

# originalDescription = """
# south-dakota-confirms-three-cyclosporiasis-cases-cdc-investigates-growing-outbreak
# """

# systemPrompt = """
# You have only heard a brief description of an event.

# Your task is to pass this information to another person.

# Rules:
# - Only use information contained in the message you receive.
# - Do not invent people, locations, motivations, or outcomes.
# - If information is missing, leave it missing.
# - You may naturally rephrase the wording.
# - You may simplify or generalise details.
# - You may accidentally omit minor details.
# - Keep the overall meaning the same.
# - Return only the rewritten description.
# """

# for i in range(10):

#     if i == 8:
#         systemPrompt = """
#         You have only heard a brief description of an event.

#         Your task is to pass this information to another person in a negative lense.

#         Rules:
#         - Only use information contained in the message you receive.
#         - Do not invent people, locations, motivations, or outcomes.
#         - If information is missing, leave it missing.
#         - You may naturally rephrase the wording.
#         - You may simplify or generalise details.
#         - You may accidentally omit minor details.
#         - Keep the overall meaning the same.
#         - Return only the rewritten description.
#         """
#     else:
#         systemPrompt = """
#         You are a person taking part in a communication chain similar to the game Chinese Whispers.

#         Your task is to retell the event naturally as if you  are explaining it to another person.

#         Rules:
#         - Perseve the overall meaning of what is written
#         - Do not intentionally invent new events
#         - Wording can be simplified
#         - You can omit minor details
#         - You can generalise numbers or locations
#         - Keep the responce under 60 words
#         - Return only the rewritten description
#         """


#     response = ollama.chat(
#         model = "llama3.1",
#         messages = [
#             {
#                 "role": "system",
#                 "content": systemPrompt,
#             },
#             {
#                 "role": "user",
#                 "content": originalDescription,
#             },
#         ],
#     )


#     newDescription = response["message"]["content"]

#     if i == 8:
#         print("negative actor")
#     print("Original description: ")
#     print(originalDescription)

#     print("New description: ")
#     print(newDescription)

#     print("\n")

#     originalDescription = newDescription    
#     newDescription = ""


def alterMessage(originalMessage):
    message = originalMessage
    systemPrompt = """
    You have only heard a brief description of an event.
    Your task is to pass this information to another person in a negative lense.
    Rules:
    - Only use information contained in the message you receive.
    - Do not invent people, locations, motivations, or outcomes.
    - If information is missing, leave it missing.
    - You may naturally rephrase the wording.
    - You may simplify or generalise details.
    - You may accidentally omit minor details.
    - Keep the overall meaning the same.
    - Return only the rewritten description.
    """
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
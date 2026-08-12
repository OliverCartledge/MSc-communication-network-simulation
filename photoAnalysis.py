import torch
from pathlib import Path
from csvEditor import getSimulationNumber

from transformers import (
    Qwen2_5_VLForConditionalGeneration,
    AutoProcessor,
)

from qwen_vl_utils import process_vision_info


MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct"

print("Loading Qwen2.5-VL...")

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

processor = AutoProcessor.from_pretrained(
    MODEL_NAME
)

print("Qwen2.5-VL loaded.")


PROMOPTS = {
    "neutral": """
Describe the scene in as much detail as possible.

Include:
- People
- Objects
- Actions
- Environments
- Visible emotions if clearly visible

Do not infer motivations or events that are not directly seen in the image.

Return a single paragraph description of the scene.
""",

    "positive": """
Describe the scene in as much detail as possible with a positive outlook.

Include:
- People
- Objects
- Actions
- Environments
- Visible emotions if clearly visible

Do not infer motivations or events that are not directly seen in the image.

Return a single paragraph description of the scene.
""",

    "negative": """
Describe the scene in as much detail as possible with a negative outlook.

Include:
- People
- Objects
- Actions
- Environments
- Visible emotions if clearly visible

Do not infer motivations or events that are not directly seen in the image.

Return a single paragraph description of the scene.
"""
}


def describeImage(actor, role):

    systemPrompt = PROMOPTS[role]
    
    outputFolder = Path("simulationNumber", str(getSimulationNumber()))
    
    image_path = outputFolder / f"generateTesting{actor}.png"

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "image": str(image_path),
                },
                {
                    "type": "text",
                    "text": systemPrompt,
                },
            ],
        }
    ]

    # Convert messages into the format expected by Qwen
    text = processor.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
    )

    # Process image
    image_inputs, video_inputs = process_vision_info(messages)

    inputs = processor(
        text=[text],
        images=image_inputs,
        videos=video_inputs,
        padding=True,
        return_tensors="pt",
    )

    inputs = inputs.to("cuda")

    print("\n\nTesting image analysis:\n")

    with torch.inference_mode():

        generated_ids = model.generate(
            **inputs,
            max_new_tokens=256,
        )

    # Remove the prompt from the generated output
    generated_ids_trimmed = [
        out_ids[len(in_ids):]
        for in_ids, out_ids in zip(
            inputs.input_ids,
            generated_ids
        )
    ]

    fullResponse = processor.batch_decode(
        generated_ids_trimmed,
        skip_special_tokens=True,
        clean_up_tokenization_spaces=False,
    )[0]

    print(fullResponse)

    return fullResponse
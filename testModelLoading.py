import torch

from transformers import (
    Qwen2_5_VLForConditionalGeneration,
    AutoProcessor,
)

from qwen_vl_utils import process_vision_info


MODEL_NAME = "Qwen/Qwen2.5-VL-7B-Instruct"

print("Loading model...")

model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)

processor = AutoProcessor.from_pretrained(MODEL_NAME)

print("Model loaded.")

image_path = "./generateTesting0.png"

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "image",
                "image": image_path,
            },
            {
                "type": "text",
                "text": """
                Describe this image in detail.

                Include:
                - People
                - Objects
                - Actions
                - Environment
                - Lighting

                Only describe things that are visibly present.
                Do not infer motivations or events that cannot be seen.
                """,
            },
        ],
    }
]

text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

image_inputs, video_inputs = process_vision_info(messages)

inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt",
)

inputs = inputs.to("cuda")

print("Generating description...")

generated_ids = model.generate(
    **inputs,
    max_new_tokens=256,
)

# Remove the input tokens so we only decode the generated response
generated_ids_trimmed = [
    out_ids[len(in_ids):]
    for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]

output_text = processor.batch_decode(
    generated_ids_trimmed,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False,
)

print("\nQwen2.5-VL response:")
print(output_text[0])
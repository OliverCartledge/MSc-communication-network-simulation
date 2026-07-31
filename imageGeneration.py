from diffusers import AutoPipelineForText2Image
import torch

model_name = "stabilityai/sdxl-turbo"

if torch.cuda.is_available():
    device = "cuda"
    dtype = torch.float16
else:
    device = "cpu"
    dtype = torch.float32

print(f"Using: {device}")

pipe = AutoPipelineForText2Image.from_pretrained(
    model_name,
    torch_dtype=dtype,
    variant="fp16" if device == "cuda" else None
)

pipe = pipe.to(device)

#image.save("thirdRun1Step.png")

def createImageTest(actor, message):
    print(f"testing generation saving by actor for actor {actor}")

    prompt = message

    generator = torch.Generator(device = device).manual_seed(42)

    image = pipe(
        prompt = prompt,
        guidance_scale=0.0,
        num_interference_steps=4,
        generator=generator,
        width=512,
        height = 512
    ).images[0]
    image.save(f"generateTesting{actor}.png")
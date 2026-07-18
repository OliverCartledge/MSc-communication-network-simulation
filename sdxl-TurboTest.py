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

prompt = """
This image captures a dramatic scene of a stormy sky. Dominating the left side of the image is a large, dark cloud, its ominous presence contrasting with the deep blue backdrop. The right side of the image presents a lighter, more ethereal cloud, its white color standing out against the darker one.

A powerful bolt of lightning cuts across the sky, connecting the two clouds and adding a sense of dynamism to the scene. The lighting is especially dramatic in the lower right corner, where a second lightning bolt strikes, this time igniting a tree that stands tall amidst the stormy weather.

The bottom left corner features a third lightning bolt, which illuminates another cloud in the distance, while the top right corner showcases a fourth one that seems to be dissipating into the sky. The image is framed by two trees on either side of the frame, adding context and depth to the scene.

Overall, this image paints a vivid picture of a powerful stormy sky, filled with dramatic lightning bolts and towering clouds.
"""

generator = torch.Generator(device = device).manual_seed(42)

image = pipe(
    prompt = prompt,
    guidance_scale=0.0,
    num_interference_steps=1,
    generator=generator,
    width=512,
    height = 512
).images[0]

image.save("thirdRun1Step.png")

print("Prompted image was saved")
from diffusers import DiffusionPipeline
import torch

model_name = "Qwen/Qwen-Image"

# Load model in BF16 if CUDA is available
torch_dtype = torch.bfloat16 if torch.cuda.is_available() else torch.float32

pipe = DiffusionPipeline.from_pretrained(
    model_name,
    torch_dtype=torch_dtype,
)

# IMPORTANT:
# Do NOT call pipe.to("cuda")
if torch.cuda.is_available():
    pipe.enable_sequential_cpu_offload()
else:
    pipe.to("cpu")

# Optional memory saving
pipe.vae.enable_tiling()

positive_magic = {
    "en": ", HD",
}

prompt = """
This image captures a dramatic scene of a stormy sky. Dominating the left side of the image is a large, dark cloud, its ominous presence contrasting with the deep blue backdrop. The right side of the image presents a lighter, more ethereal cloud, its white color standing out against the darker one.

A powerful bolt of lightning cuts across the sky, connecting the two clouds and adding a sense of dynamism to the scene. The lighting is especially dramatic in the lower right corner, where a second lightning bolt strikes, this time igniting a tree that stands tall amidst the stormy weather.

The bottom left corner features a third lightning bolt, which illuminates another cloud in the distance, while the top right corner showcases a fourth one that seems to be dissipating into the sky. The image is framed by two trees on either side of the frame, adding context and depth to the scene.

Overall, this image paints a vivid picture of a powerful stormy sky, filled with dramatic lightning bolts and towering clouds.
"""

negative_prompt = ""

image = pipe(
    prompt=prompt + positive_magic["en"],
    negative_prompt=negative_prompt,
    width=256,
    height=256,
    num_inference_steps=8,
    true_cfg_scale=4.0,
    generator=torch.Generator(device="cuda").manual_seed(42),
).images[0]

image.save("exampleGDELTMoreSteps.png")
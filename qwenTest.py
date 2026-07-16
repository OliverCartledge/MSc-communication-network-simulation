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

prompt = "flash flood emergency issued in southern texas around camp mystic area"

negative_prompt = ""

image = pipe(
    prompt=prompt + positive_magic["en"],
    negative_prompt=negative_prompt,
    width=256,
    height=256,
    num_inference_steps=20,
    true_cfg_scale=4.0,
    generator=torch.Generator(device="cuda").manual_seed(42),
).images[0]

image.save("exampleGDELT.png")
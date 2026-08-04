from diffusers import DiffusionPipeline
import torch

MODEL_NAME = "Qwen/Qwen-Image"

device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

print(f"Using: {device}")

pipe = DiffusionPipeline.from_pretrained(
    MODEL_NAME,
    torch_dtype=dtype,
)

pipe.to(device)

pipe.vae.enable_tiling()

try:
    pipe.enable_xformers_memory_efficient_attention()
    print("Using xFormers attention")
except Exception:
    print("xFormers not available")

prompt = """
The image appears to be a photograph of a building through a window, with a yellow caution tape in the foreground. The building is white and has a few windows, but it is difficult to make out any details due to the reflection of the sky and trees in the glass. The overall atmosphere of the image is one of uncertainty and potential danger, as suggested by the presence of the yellow tape. The image raises more questions than it answers, leaving the viewer to wonder what is happening in the building and why it is being treated as a potentially hazardous area. The lack of context and details makes it difficult to interpret the scene, leaving the viewer to fill in the blanks with their own imaginations. The image could be seen as a symbol of the unknown or the unknowns that lie within our own lives. It could also be seen as a representation of the often-inadequate or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequate or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or incomplete information we have about others and their lives. The image could also be seen as a representation of the often-inadequately or.
"""

with torch.inference_mode():

    image = pipe(
        prompt=prompt + ", HD",
        negative_prompt="",
        width=1024,
        height=1024,
        num_inference_steps=20,
        true_cfg_scale=4.0,
        generator=torch.Generator(device=device).manual_seed(42),
    ).images[0]

image.save("QwenExample.png")
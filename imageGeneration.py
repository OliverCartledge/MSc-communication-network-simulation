from diffusers import DiffusionPipeline
import torch
from pathlib import Path
from csvEditor import getSimulationNumber

MODEL_NAME = "Qwen/Qwen-Image"
#MODEL_NAME = "stabilityai/sdxl-turbo"
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

def createImageTest(actor, message):
    print(f"testing generation saving by actor for actor {actor}")

    outputFolder = Path("simulationNumber", str(getSimulationNumber()))
    outputFolder.mkdir(parents=True, exist_ok=True)
    
    prompt = message

    print("\n\nTesting simulation number:", )

    with torch.inference_mode():

        image = pipe(
            prompt = prompt,
            width=1024,
            height=1024,
            num_inference_steps=20,
            generator=torch.Generator(device=device).manual_seed(42),
        ).images[0]
        image.save(outputFolder / f"generateTesting{actor}.png")
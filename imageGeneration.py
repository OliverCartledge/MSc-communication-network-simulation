from diffusers import DiffusionPipeline
import torch

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

    prompt = message

    #generator = torch.Generator(device = device).manual_seed(42)
#
    #image = pipe(
    #    prompt = prompt,
    #    guidance_scale=0.0,
    #    num_interference_steps=20,
    #    generator=generator,
    #    width=1024,
    #    height = 1024
    #).images[0]
    with torch.inference_mode():

        image = pipe(
            prompt = prompt,
            width=1024,
            height=1024,
            num_inference_steps=20,
            generator=torch.Generator(device=device).manual_seed(42),
        ).images[0]
        image.save(f"generateTesting{actor}.png")



# old image generation

# from diffusers import AutoPipelineForText2Image
# import torch

# model_name = "stabilityai/sdxl-turbo"

# if torch.cuda.is_available():
#     device = "cuda"
#     dtype = torch.float16
# else:
#     device = "cpu"
#     dtype = torch.float32

# print(f"Using: {device}")

# pipe = AutoPipelineForText2Image.from_pretrained(
#     model_name,
#     torch_dtype=dtype,
#     variant="fp16" if device == "cuda" else None
# )

# pipe = pipe.to(device)

# #image.save("thirdRun1Step.png")

# def createImageTest(actor, message):
#     print(f"testing generation saving by actor for actor {actor}")

#     prompt = message

#     generator = torch.Generator(device = device).manual_seed(42)

#     image = pipe(
#         prompt = prompt,
#         guidance_scale=0.0,
#         num_interference_steps=4,
#         generator=generator,
#         width=512,
#         height = 512
#     ).images[0]
#     image.save(f"generateTesting{actor}.png")
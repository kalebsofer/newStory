# %%
from diffusers import DiffusionPipeline
# %%
pipe = DiffusionPipeline.from_pretrained("Vhey/childrens-stories-v1-semi-real")

# %%
prompt = "The very hungry caterpillar looked for food on the moon, in the style of Eric Carle"
# %%
image = pipe(prompt).images[0]

# %%
image.show()
# %%

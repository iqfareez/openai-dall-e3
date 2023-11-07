from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
# client = OpenAI(
#   api_key=os.environ.get("CUSTOM_ENV_NAME"),
# )

prompt = input("Prompt: ")

if (prompt == ""):
  print("No prompt provided. Exiting...")
  exit(1)

print("Generating image...")

response = client.images.generate(
  model="dall-e-3",
  prompt=prompt,
  size="1024x1024", # Available size: 1024x1024, 1024x1792 or 1792x1024
  quality="standard", # Available quality: "standard" or "hd"
  n=1, # Number of images to generate (Current limit is only 1)
)

image_url = response.data[0].url

print("Image URL: " + image_url)
print()
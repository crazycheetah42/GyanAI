# Import the necessary modules needed for the GyanAI Shorten function
import main_function, os

# Setup LLaMa API and add it to the environment variables
rkey = open("key.txt", 'r').read().strip()
os.environ["REPLICATE_API_TOKEN"] = rkey

def sShorten(prompt):
    prompt_input = "Shorten this text without removing the context. The shortened text should still convey the meaning of the message. Do not add any extra sentences or explanations, just give the shortened text. Use the text below as reference: \n" + prompt
    response = main_function.run_llama(prompt_input)
    return response
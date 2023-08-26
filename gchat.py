# Import the necessary modules needed for the GyanAI Chat function
import os, main_function

# Setup LLaMa API and add it to the environment variables as it's needed for the replicate model to run
rkey = open("key.txt", 'r').read().strip()
os.environ["REPLICATE_API_TOKEN"] = rkey

def cGenerate(prompt):
    response = main_function.run_llama(prompt)
    return response
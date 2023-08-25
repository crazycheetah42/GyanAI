# Import the necessary modules needed for the GyanAI Chat function
import replicate, os

# Setup LLaMa API and add it to the environment variables as it's needed for the replicate model to run
rkey = open("key.txt", 'r').read().strip()
os.environ["REPLICATE_API_TOKEN"] = rkey

def cGenerate(prompt):
    prompt_input = prompt
    output = replicate.run(
    "replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
    input={"prompt": prompt_input}
        )
    full_response = ""

    for item in output:
        full_response += item
    return full_response
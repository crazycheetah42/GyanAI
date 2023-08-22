# Import the necessary modules needed for the GyanAI Shorten function
import replicate, os

# Setup LLaMa API and add it to the environment variables
rkey = open("key.txt", 'r').read().strip()
os.environ["REPLICATE_API_TOKEN"] = rkey

def sShorten(prompt):
    prompt_input = "Shorten this text without removing the context. The shortened text should still convey the meaning of the message. Do not add any extra sentences or explanations, just give the shortened text. Use the text below as reference: \n" + prompt
    output = replicate.run(
    "replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
    input={"prompt": prompt_input}
        )
    full_response = ""

    for item in output:
        # https://replicate.com/replicate/llama-2-70b-chat/versions/58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781/api#output-schema
        full_response += item
    return full_response
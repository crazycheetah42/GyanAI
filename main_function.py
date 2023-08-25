import replicate

def run_llama(prompt_input):
    output = replicate.run(
        "replicate/llama-2-70b-chat:58d078176e02c219e11eb4da5a02a7830a283b14cf8f94537af893ccff5ee781",
        input={"prompt": prompt_input}
            )
    full_response = ""

    for item in output:
        full_response += item
    return full_response
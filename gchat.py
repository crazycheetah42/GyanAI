# Import the necessary modules needed for the GyanAI Chat function
import bardapi

# Setup Bard API and store the result of the prompt
bKey = open("bard.txt", "r").read().strip()
bard = bardapi.Bard(token=bKey)


def cGenerate(prompt):
    bard_result = bard.get_answer(prompt)['content']
    return bard_result
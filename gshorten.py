# Import the necessary modules needed for the GyanAI Chat function
from bardapi import Bard

# Setup Bard API and store the result of the prompt
bKey = open("bard.txt", "r").read().strip()
bard = Bard(token=bKey)


def sShorten(prompt):
    newPrompt = "Shorten this text without removing the context: \n" + prompt
    bard_result = bard.get_answer(newPrompt)['content']
    return bard_result
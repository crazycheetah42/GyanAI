import openai
openai.api_key = open("config/openai.txt", "r").read().strip()
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant that helps in code generation. When prompted, you only generate and output the code. You do not give any explanations or additional answers that is not code (of the programming language) specified by the user."} ]
def gcode(prompt):
    message = input(f"User: {prompt}")
    messages.append(
        {"role": "user", "content": message},
    )
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages
    )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
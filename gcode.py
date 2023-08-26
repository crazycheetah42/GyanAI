import openai
openai.api_key = open("openai.txt", "r").read().strip()
messages = [ {"role": "system", "content": 
              "You are a intelligent assistant that helps in code generation. When prompted, generate and output only the code. Do not give any explanations or additional answers that is not code (of the language) specified by the User."} ]
while True:
    message = input("User : ")
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "assistant", "content": reply})
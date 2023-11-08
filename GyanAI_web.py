import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a expert who helps answer people's questions."}]

def GyanAI(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=GyanAI, inputs = "text", outputs = "text", title = "GyanAI")
demo.launch(share=True)
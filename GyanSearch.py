import tkinter as tk
from tkinter import ttk
import openai
import speech_recognition as sr

openai_api_key = open("key.txt", "r").read().strip()
if openai_api_key == "":
    window = tk.Tk()
    window.geometry("630x430")
    window.iconbitmap("search.ico")
    window.wm_title("OpenAI API key")

    label = ttk.Label(window, text="OpenAI API key", font=("Segoe UI", 22))
    label.pack()

    space_lbl = ttk.Label(window, text="")
    space_lbl.pack()

    label2 = ttk.Label(window, text="An OpenAI API key is required to proceed. Proceeding without an API key will cause errors while using the app.")
    label2.pack()

    space_lbl2 = ttk.Label(window, text="")
    space_lbl2.pack()
    space_lbl3 = ttk.Label(window, text="")
    space_lbl3.pack()

    label3 = ttk.Label(window, text="Enter OpenAI API key here:")
    label3.pack()
    space_lbl4 = ttk.Label(window, text="")
    space_lbl4.pack()

    var = tk.StringVar()
    new_api_key = ttk.Entry(window, textvariable=var, width=75)
    new_api_key.pack()

    def write_api_key_to_file():
        api_key = var.get()
        key_file = open("key.txt", "w")
        key_file.write(api_key)
        window.destroy()
        from tkinter import messagebox
        messagebox.showinfo("API key added", "The OpenAI API key has been added. You may now restart the program.")

    space_lbl5 = ttk.Label(window, text="")
    space_lbl5.pack()
    button = ttk.Button(window, text="OK", command=write_api_key_to_file)
    button.pack()

    space_lbl6 = ttk.Label(window, text="")
    space_lbl6.pack()
    space_lbl7 = ttk.Label(window, text="")
    space_lbl7.pack()

    link = ttk.Label(window, text="See how to generate an API key", cursor="hand2")
    link.pack()
    def open_link(url):
        import webbrowser
        webbrowser.open(url)
    link.bind("<Button-1>", lambda e: open_link("https://www.google.com"))
    link.config(foreground='blue')
    
    window.mainloop()
else:
    openai.api_key = openai_api_key

    def voice():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            text = r.recognize_google(audio)
            prompt.insert(0, text)
            text_prompt = (f"User: {text}\n"
                    f"ChatGPT: ")
            response = openai.Completion.create(engine="text-davinci-003", prompt=text_prompt, temperature=0.5, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0)
            response_text = response['choices'][0]['text']

            answer.delete(1.0, tk.END)
            answer.insert(1.0, response_text)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def search():
        text = var.get()
        
        text_prompt = (f"User: {text}\n"
                    f"ChatGPT: ")
        response = openai.Completion.create(engine="text-davinci-003", prompt=text_prompt, temperature=0.5, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0)
        response_text = response['choices'][0]['text']

        answer.delete(1.0, tk.END)
        answer.insert(1.0, response_text)

    root = tk.Tk()
    root.geometry("1280x768")
    root.wm_title("Gyan Search")
    root.iconbitmap("search.ico")

    header_lbl = ttk.Label(root, text="Gyan Search", font=("Segoe UI", 22))
    header_lbl.pack()

    var = tk.StringVar()

    space_lbl = ttk.Label(root, text="", font=("Segoe UI", 12))
    space_lbl.pack()

    input_hint_lbl = ttk.Label(root, text="Enter prompt", font=("Segoe UI", 14))
    input_hint_lbl.pack()

    prompt = ttk.Entry(root, textvariable=var, width=170)
    prompt.pack()

    submit_btn = tk.PhotoImage(file="search.png")

    btn_frame = tk.LabelFrame(root)
    btn_frame.pack()

    submit_button = ttk.Button(btn_frame, image=submit_btn, command=search)
    submit_button.pack(side="left")

    voice_btn = tk.PhotoImage(file="voice.png")

    voice_button = ttk.Button(btn_frame, image=voice_btn, command=voice)
    voice_button.pack(side="right")

    space_lbl2 = ttk.Label(root, text="", font=("Segoe UI", 12))
    space_lbl2.pack()
    space_lbl3 = ttk.Label(root, text="", font=("Segoe UI", 12))
    space_lbl3.pack()

    answer = tk.Text(root, height=25, width=120)
    answer.pack(pady=5)

    space_lbl4 = ttk.Label(root, text="", font=("Segoe UI", 12))
    space_lbl4.pack()
    space_lbl5 = ttk.Label(root, text="", font=("Segoe UI", 12))
    space_lbl5.pack()

    link1 = ttk.Label(root, text="Need help?", cursor="hand2")
    link1.pack()
    def open_link(url):
        import webbrowser
        webbrowser.open(url)
    link1.bind("<Button-1>", lambda e: open_link("https://www.google.com"))
    link1.config(foreground='blue')

    root.mainloop()

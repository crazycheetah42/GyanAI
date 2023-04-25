import tkinter as tk
import openai
import speech_recognition as sr

openai_api_key = open("key.txt", "r").read().strip()

def add_api_key():
    window = tk.Tk()
    window.geometry("750x550")
    window.wm_title("OpenAI API key")

    label = tk.Label(window, text="OpenAI API key", font=("Segoe UI", 22))
    label.pack()

    space_lbl = tk.Label(window, text="")
    space_lbl.pack()

    label2 = tk.Label(window, text="An OpenAI API key is required to proceed. Proceeding without an API key will cause errors while using the app.")
    label2.pack()

    space_lbl2 = tk.Label(window, text="")
    space_lbl2.pack()
    space_lbl3 = tk.Label(window, text="")
    space_lbl3.pack()

    label3 = tk.Label(window, text="Enter your OpenAI API key here:")
    label3.pack()
    space_lbl4 = tk.Label(window, text="")
    space_lbl4.pack()

    var = tk.StringVar()
    new_api_key = tk.Entry(window, textvariable=var, width=75)
    new_api_key.pack()

    def write_api_key_to_file():
        api_key = var.get()
        key_file = open("key.txt", "w")
        key_file.write(api_key)
        window.destroy()
        from tkinter import messagebox
        messagebox.showinfo("API key added", "The OpenAI API key has been added. You may now restart the program.")

    space_lbl5 = tk.Label(window, text="")
    space_lbl5.pack()
    button = tk.Button(window, text="OK", command=write_api_key_to_file)
    button.pack()

    space_lbl6 = tk.Label(window, text="")
    space_lbl6.pack()
    space_lbl7 = tk.Label(window, text="")
    space_lbl7.pack()

    link = tk.Label(window, text="See how to generate an API key", cursor="hand2")
    link.pack()
    def open_link(url):
        import webbrowser
        webbrowser.open(url)
    link.bind("<Button-1>", lambda e: open_link("https://apps.aryatechspace.com/Gyan-Search/api_key.html"))
    link.config(foreground='blue')
    
    window.mainloop()
def main_application():
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
        temp = 0.5
        max_tkns = 1024
        top_p = 1
        freq_penalty = 0
        pres_penalty = 0
        response = openai.Completion.create(engine="text-davinci-003", prompt=text_prompt, temperature=temp, max_tokens=max_tkns, top_p=top_p, frequency_penalty=freq_penalty, presence_penalty=pres_penalty)
        response_text = response['choices'][0]['text']

        answer.delete(1.0, tk.END)
        answer.insert(1.0, response_text)

    root = tk.Tk()
    root.geometry("1280x750")
    root.wm_title("GyanGPT")
    from tkinter import ttk
    tabControl = ttk.Notebook(root)
    tabControl.pack(fill="both", expand=1)

    regular = tk.Frame(tabControl)
    txt_summarizer = tk.Frame(tabControl)
    tabControl.add(regular, text='Regular')
    tabControl.add(txt_summarizer, text='Text Summarizer')

    header_lbl = tk.Label(regular, text="GyanGPT", font=("Segoe UI", 22))
    header_lbl.pack()
    var = tk.StringVar()
    space_lbl = tk.Label(regular, text="", font=("Segoe UI", 12))
    space_lbl.pack()
    input_hint_lbl = tk.Label(regular, text="Enter your prompt below", font=("Segoe UI", 14))
    input_hint_lbl.pack()
    prompt = tk.Entry(regular, textvariable=var, width=170)
    prompt.pack()
    submit_btn = tk.PhotoImage(file="search.png")
    btn_frame = tk.LabelFrame(regular)
    btn_frame.pack()
    submit_button = tk.Button(btn_frame, image=submit_btn, command=search)
    submit_button.pack(side="left")
    voice_btn = tk.PhotoImage(file="voice.png")
    voice_button = tk.Button(btn_frame, image=voice_btn, command=voice)
    voice_button.pack(side="right")
    space_lbl2 = tk.Label(regular, text="", font=("Segoe UI", 12))
    space_lbl2.pack()
    space_lbl3 = tk.Label(regular, text="", font=("Segoe UI", 12))
    space_lbl3.pack()
    answer = tk.Text(regular, height=25, width=120)
    answer.pack(pady=5)
    space_lbl4 = tk.Label(regular, text="", font=("Segoe UI", 12))
    space_lbl4.pack()
    space_lbl5 = tk.Label(regular, text="", font=("Segoe UI", 12))
    space_lbl5.pack()
    link1 = tk.Label(regular, text="Need help?", cursor="hand2")
    link1.pack()
    def open_link(url):
        import webbrowser
        webbrowser.open(url)
    link1.bind("<Button-1>", lambda e: open_link("https://apps.aryatechspace.com/Gyan-Search/"))
    link1.config(foreground='blue')

    header_lbl = tk.Label(txt_summarizer, text="Text Summarizer", font=("Segoe UI", 22))
    header_lbl.pack()

    var2 = tk.StringVar()
    space_lbl = tk.Label(txt_summarizer, text="", font=("Segoe UI", 12))
    space_lbl.pack()

    input_hint_lbl = tk.Label(txt_summarizer, text="Enter text to summarize", font=("Segoe UI", 14))
    input_hint_lbl.pack()

    space_lbl2 = tk.Label(txt_summarizer, text="", font=("Segoe UI", 12))
    space_lbl2.pack()

    def summarize():
        prompt = input.get("1.0",'end-1c')

        final_prompt = "Summarize this text:\n\n" + prompt
        
        text_prompt = (f"User: {final_prompt}\n"
                    f"ChatGPT: ")
        temp = 0.5
        max_tkns = 1024
        top_p = 1
        freq_penalty = 0
        pres_penalty = 0
        response = openai.Completion.create(engine="text-davinci-003", prompt=text_prompt, temperature=temp, max_tokens=max_tkns, top_p=top_p, frequency_penalty=freq_penalty, presence_penalty=pres_penalty)
        response_text = response['choices'][0]['text']
        from tkinter import filedialog
        output = filedialog.asksaveasfile(defaultextension='.txt',
                                          filetypes=[
                                            ("Text Document (*.txt)", ".txt"),
                                            ("All files", ".*")
                                          ])
        if output is None:
            return
        output_text = str(response_text)
        output.write(output_text)
        output.close()

    submit_button2 = tk.Button(txt_summarizer, text="Summarize", command=summarize)
    submit_button2.pack()

    space_lbl3 = tk.Label(txt_summarizer, text="", font=("Segoe UI", 12))
    space_lbl3.pack()

    input = tk.Text(txt_summarizer, height=28, width=132)
    input.pack()

    space_lbl4 = tk.Label(txt_summarizer, text="", font=("Segoe UI", 12))
    space_lbl4.pack()
    
    
    space_lbl5 = tk.Label(txt_summarizer, text="", font=("Segoe UI", 12))
    space_lbl5.pack()

    root.mainloop()
if openai_api_key == "":
    add_api_key()
else:
    main_application()

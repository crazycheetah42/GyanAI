"""
GyanAI is open-source, and it uses the replicate model. This is the main file (made for Windows) with the UI and function calls. Please feel free to contribute changes. 
Read the README for more info.
"""

# Import the necessary modules for the main program
import tkinter as tk
from tkinter import ttk

def main_application():
    # Setup the basic tkinter window
    root = tk.Tk()
    root.wm_title("GyanAI")
    root.geometry("1280x768")
    root.iconbitmap("main_icon.ico")
    # Add the basic tkinter skeleton
    gHeader = ttk.Label(root, text="GyanAI", font=("Segoe UI", 24))
    gHeader.pack()
    gTabWidget = ttk.Notebook(root)
    gTabWidget.pack(fill="both", expand=1)

    # Add the Chat tab to the tab widget
    chat = ttk.Frame(gTabWidget)
    gTabWidget.add(chat, text='Chat')

    # Add the widgets to the chat tab
    cPromptVar = tk.StringVar()
    chat_lbl = ttk.Label(chat, text="Chat", font=("Segoe UI", 18))
    chat_lbl.pack()
    cHintLbl = ttk.Label(chat, text="Enter your prompt below", font=("Segoe UI", 14))
    cHintLbl.pack()
    cPrompt = ttk.Entry(chat, textvariable=cPromptVar)
    # This code packs the prompt into the tkinter window. The fill parameter tells tkinter to stretch the prompt to the edge of the window.
    cPrompt.pack(fill="x")
    # Add the function for generation in the chat function
    def cSubmit():
        import gchat
        cPrompt = cPromptVar.get()
        cResult = gchat.cGenerate(cPrompt)
        cAnswer.delete(1.0, tk.END)
        cAnswer.insert(1.0, cResult)
    cSubmitBtn = ttk.Button(chat, text="Submit", command=cSubmit)
    cSubmitBtn.pack()
    cAnswer = tk.Text(chat)
    # This is another pack command with the fill parameter. The 'both' means it will fill/stretch to both x and y.
    cAnswer.pack(fill="both")

    # Add shorten text tab to tabWidget
    shortenText = ttk.Frame(gTabWidget)
    gTabWidget.add(shortenText, text='Shorten Text')

    # Add widgets for the shorten text function
    sHeader = ttk.Label(shortenText, text='Shorten Text', font=("Segoe UI", 18))
    sHeader.pack()
    sHintLbl = ttk.Label(shortenText, text="Enter your text below", font=("Segoe UI", 14))
    sHintLbl.pack()
    sText = tk.Text(shortenText)
    sText.pack(fill="both")
    # Add the function for generation in the shortenText function
    def sShorten():
        import gshorten
        sPrompt = sText.get(1.0, tk.END)
        sResult = gshorten.sGenerate(sPrompt)
        from tkinter import filedialog
        filename = filedialog.asksaveasfilename(
        title="Save your shortened file",
        filetypes=[("Text File", "*.txt"), ("All Files", "*")]
            )
        with open(filename, "w") as f:
            f.write(sResult)
    cSubmitBtn = ttk.Button(shortenText, text="Submit", command=sShorten)
    cSubmitBtn.pack()


    # Configure the tkinter window to run until the user closes the program
    root.mainloop()
def api_keys_add():
    # Setup basic tkinter window for api key adding function
    window = tk.Tk()
    window.geometry("1024x768")
    window.wm_title("Add API Keys")

    heading = ttk.Label(window, text="Add API Keys", font=("Segoe UI", 24))
    heading.pack()

    label = ttk.Label(window, text="Please add a Replicate and OpenAI API key.")
    label.pack()

    rKeyHint = ttk.Label(window, text="Enter Replicate API Key")
    rKeyHint.pack()
    rkeyVar = tk.StringVar()
    rKey = ttk.Entry(window, textvariable=rkeyVar)
    rKey.pack()

    oKeyHint = ttk.Label(window, text="Enter OpenAI API Key")
    oKeyHint.pack()
    okeyVar = tk.StringVar()
    oKey = ttk.Entry(window, textvariable=okeyVar)
    oKey.pack()
    def add_keys():
        new_r_key = rkeyVar.get()
        new_o_key = okeyVar.get()
        r_key_file = open("key.txt", "w")
        o_key_file = open("openai.txt", "w")

        r_key_file.write(new_r_key)
        o_key_file.write(new_o_key)

    submit_btn = ttk.Button(window, text="Add API Keys", command=add_keys)
    submit_btn.pack()
    
    window.mainloop()
if __name__ == "__main__":
    with open("key.txt", "r") as r:
        with open("openai.txt", "r") as o:
            rkey = r.read().strip()
            okey = o.read().strip()
            if rkey == "" or okey == "" or rkey == "" and okey == "":
                api_keys_add()
            else:
                main_application()
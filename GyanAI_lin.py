# Import the necessary modules for the main program
import tkinter as tk
from tkinter import ttk
import speech_recognition as sr

# Setup the basic tkinter window
root = tk.Tk()
root.wm_title("GyanAI")
root.geometry("1280x768")
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
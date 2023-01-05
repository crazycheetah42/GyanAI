from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "YOUR_API_KEY_FROM_OPENAI"

class Ui_MainWindow(object):
    def image_search(self):
        self.textEdit.setText("Searching...")
        prompt = self.textEdit.toPlainText()
        response= openai.Image.create (prompt=prompt, n=1, size="1024x1024")
        image_url = response['data'][0]['url']
        import webbrowser
        webbrowser.open(image_url)
    def search(self):
        self.textEdit.setText("Searching...")
        text = self.textEdit.toPlainText()            

        # Send the text to the ChatGPT API and receive a response
        prompt = (f"User: {text}\n"
                    f"ChatGPT: ")
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.5, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0)
        response_text = response['choices'][0]['text']

        # Convert the ChatGPT response to speech and play it back to the user
        self.textBrowser.setText(response_text)
    def speak(self):
        self.textEdit.setText("Listening...")
         # Set up the ChatGPT API client

        # Initialize the text-to-speech engine
        engine = pyttsx3.init()
        
        
        # Record the user's voice input
        
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        # Transcribe the audio to text
        try:
            text = r.recognize_google(audio)
            if text == "exit":
                import sys
                sys.exit()
            self.textEdit.setText(f"{text}")
        except Exception as e:
            print("Sorry, I wasn't able to understand.")
            

        # Send the text to the ChatGPT API and receive a response
        prompt = (f"User: {text}\n"
                    f"ChatGPT: ")
        response = openai.Completion.create(engine="text-davinci-003", prompt=prompt, temperature=0.5, max_tokens=1024, top_p=1, frequency_penalty=0, presence_penalty=0)
        response_text = response['choices'][0]['text']

        # Convert the ChatGPT response to speech and play it back to the user
        self.textBrowser.setText(response_text)
        engine.say(response_text)
        engine.runAndWait()
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(360, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(112, 10, 120, 51))
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 60, 241, 30))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("background-color: transparent;")
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(280, 60, 31, 30))
        self.pushButton.setCursor(QCursor(Qt.ArrowCursor))
        icon = QIcon()
        icon.addFile(u"icons8-microphone-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 110, 341, 681))
        self.textBrowser.setAutoFillBackground(False)
        self.textBrowser.setTabChangesFocus(True)
        self.textBrowser.setUndoRedoEnabled(True)
        self.textBrowser.setLineWrapColumnOrWidth(0)
        self.pushButton_2 = QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet("background-color: transparent;")
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(250, 60, 31, 30))
        icon1 = QIcon()
        icon1.addFile(u"icons8-search-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_3 = QPushButton(self.centralwidget)
        self.pushButton_3.setStyleSheet("background-color: transparent;")
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(310, 60, 31, 30))
        self.pushButton_3.setCursor(QCursor(Qt.ArrowCursor))
        icon2 = QIcon()
        icon2.addFile(u"Camera-icon.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Code section (functionality)
        
        self.pushButton.clicked.connect(self.speak)
        self.pushButton_2.clicked.connect(self.search)
        self.pushButton_3.clicked.connect(self.image_search)
        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gyan Search", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Gyan Search", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Q:", None))

if __name__ == "__main__":
    import darkdetect
    import qdarkstyle
    if darkdetect.isDark():
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())

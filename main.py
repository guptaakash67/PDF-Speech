from tkinter import filedialog
import codecs
import os
from tkinter import *
from gtts import gTTS
from playsound import playsound
from translate import MyTranslate
from pdf_to_speech import PDFReader

root = Tk()
root.geometry("1250x950")
img = PhotoImage(file="Images/bg.png")
label = Label(root, image=img)
label.place(x=0, y=0)
root.title("TEXT TO SPEECH")

Label(root, text="TEXT_TO_SPEECH", font="arial 20 bold", fg='gray', bg='#36454F').pack()
Msg = StringVar()
lang = StringVar()

label1 = Label(root, text="Enter Text", font='arial 15 bold', fg='gray', bg='#36454F').place(x=220, y=160)
message_entry_field = Entry(root, textvariable=Msg, width=50, font="Robote 20")
message_entry_field.place(x=220, y=200, width=350, height=300)

label2 = Label(root, text="Enter Language (hindi=hi marathi= mr english =en )", font='arial 15 bold', fg='gray', bg='#36454F').place(x=600, y=160)
lang_entry_field = Entry(root, textvariable=lang, width=50)
lang_entry_field.place(x=600, y=200)

# translate_label = Label(root, text="Translate Label Test", font="arial 15 bold", fg="white", bg="#36454F").place(x=800, y=550)


def browse_files():
    filename = filedialog.askopenfilename(initialdir="C:/",
                                          title="Nilay",
                                          filetypes=(("Text files", "*.txt*"), ("all files", "*.*")))
    return filename


def text_to_speech_file():
    # language = lang_entry_field.get()
    # with codecs.open(browse_files(), encoding='utf-8') as f:
    #     file = f.read().replace("\n", " ")
    pdf_obj = PDFReader(file_path="/brief-history-of-time.pdf")
    pdf_data = pdf_obj.translate_pdf()
    language = lang_entry_field.get()
    test = MyTranslate(text_input=pdf_data, translate_to_language=language)
    translated_text = test.connection()
    message = translated_text
    speech = gTTS(text=message, lang=language, slow=False)
    speech.save('/speech.mp3')
    playsound('/speech.mp3')
    os.remove('/speech.mp3')


def text_to_speech():
    language = lang_entry_field.get()
    test = MyTranslate(text_input=message_entry_field.get(), translate_to_language=language)
    translated_text = test.connection()
    message = translated_text
    speech = gTTS(text=message, lang=language, slow=False)
    speech.save("sounds/speech.mp3")
    playsound('sounds/speech.mp3', True)
    os.remove('sounds/speech.mp3')


def exit():
    root.destroy()


def reset():
    Msg.set("")
    lang.set("")
    # os.remove('speech.mp3')


def stop():
    os.stop('/speech.mp3')


speak_button = PhotoImage(file="Images/speak-man.png")
Button(root, text="Speak", bg="white", compound=LEFT, image=speak_button, width=130, font="arial 14 bold",
       command=text_to_speech).place(x=600, y=320)

exit_button = PhotoImage(file="Images/exit.png")
Button(root, font='arial 15 bold', text='EXIT', compound=LEFT, image=exit_button, width=130, command=exit,
       bg='white').place(x=750, y=320)

reset_button = PhotoImage(file="Images/reset.png")
Button(root, font='arial 15 bold', text='RESET', compound=LEFT, image=reset_button, width=130, command=reset,
       bg='white').place(x=900, y=320)

file_button = PhotoImage(file="Images/file.png")
Button(root, text=" Play PDF File", font='arial 15 bold', command=text_to_speech_file, compound=LEFT, image=file_button,
       width=200, bg='white').place(x=600, y=400)

pause_file_button = PhotoImage(file="Images/pause.png")
Button(root, text="Pause File", font='arial 15 bold', command=stop, compound=LEFT, image=pause_file_button, width=180,
       bg='white').place(x=850, y=400)
root.mainloop()

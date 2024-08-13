from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create the main window
root = Tk()
root.geometry('1100x320')  # Set the window size
root.resizable(0, 0)  # Disable window resizing
root['bg'] = 'pink'  # Set background color
root.title('Real-time Translator')  # Set window title

# Create a label for the title
Label(root, text="Language Translator", font="Arial 20 bold").pack()

# Create a label for the input text
Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=165, y=90)

# Create an entry widget for user input
Input_text = Entry(root, width=60)
Input_text.place(x=30, y=130)

# Create a label for the output
Label(root, text="Output", font='arial 13 bold', bg='white smoke').place(x=780, y=90)

# Create a text widget for displaying the translation
Output_text = Text(root, font='arial 10', height=5, wrap=WORD, padx=5, pady=5, width=50)
Output_text.place(x=600, y=130)

# Retrieve language codes and names for the combobox
language_codes = list(LANGUAGES.keys())
language_names = list(LANGUAGES.values())

# Create a combobox for selecting the destination language
dest_lang = ttk.Combobox(root, values=language_names, width=22)
dest_lang.place(x=130, y=180)
dest_lang.set('Choose Language')


# Define the translation function
def Translate():
    try:
        translator = Translator()
        selected_lang_name = dest_lang.get()

        # Debug information
        print(f"Selected language: {selected_lang_name}")

        # Retrieve the language code from the selected language name
        lang_code = [code for code, name in LANGUAGES.items() if name == selected_lang_name]

        if lang_code:
            translation = translator.translate(Input_text.get(), dest=lang_code[0])
            Output_text.delete(1.0, END)
            Output_text.insert(END, translation.text)
        else:
            Output_text.delete(1.0, END)
            Output_text.insert(END, "Error: Selected language is not supported.")
    except Exception as e:
        print(f"Translation error: {e}")
        Output_text.delete(1.0, END)
        Output_text.insert(END, "Translation error.")


# Create a button for triggering translation
trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='orange',
                   activebackground='green')
trans_btn.place(x=445, y=180)

# Run the Tkinter main loop
root.mainloop()

# Import required libraries
from tkinter import Tk, Label, Entry, Text, Button, WORD
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Function to perform the translation
def perform_translation():
    try:
        # Create a Translator object with the selected language
        translator = Translator()
        target_language = language_selector.get()
        translation_result = translator.translate(text_input.get(), dest=target_language).text

        # Update the output text widget with the translation
        result_output.delete(1.0, 'end')
        result_output.insert('end', translation_result)
    except Exception as e:
        print(f"Error during translation: {e}")

# Set up the main application window
app = Tk()
app.geometry('1200x500')  # Increase height for better spacing
app.resizable(0, 0)  # Disable resizing
app.configure(bg='#E8F4F8')  # Light blue background color
app.title('Language Translator')  # Window title

# Create and place GUI components
Label(app, text="Language Translator", font=("Helvetica", 24, "bold"), bg='#E8F4F8', fg='#333').pack(pady=20)

# Entry section
Label(app, text="Enter Text:", font=("Helvetica", 14), bg='#E8F4F8', fg='#555').place(x=30, y=80)
text_input = Entry(app, font=("Helvetica", 14), width=60, bd=2, relief='sunken')
text_input.place(x=30, y=120)

# Output section
Label(app, text="Translation Output:", font=("Helvetica", 14), bg='#E8F4F8', fg='#555').place(x=650, y=80)
result_output = Text(app, font=("Helvetica", 14), height=6, wrap=WORD, padx=10, pady=10, width=50, bd=2, relief='sunken')
result_output.place(x=650, y=120)

# Dropdown for selecting the target language
available_languages = list(LANGUAGES.values())
language_selector = ttk.Combobox(app, values=available_languages, font=("Helvetica", 14), width=22, state='readonly')
language_selector.place(x=30, y=20)
language_selector.set('Select Language')

# Button to trigger the translation process
translate_button = Button(app, text='Translate', font=("Helvetica", 14, "bold"), pady=10, command=perform_translation, bg='#4CAF50', fg='white', activebackground='#45A049')
translate_button.place(x=30, y=270)

# Start the Tkinter event loop
app.mainloop()

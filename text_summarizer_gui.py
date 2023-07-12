import tkinter as tk
from tkinter import filedialog
from tkinter.ttk import Combobox
import pyperclip
from summarizetext import Summarizer

# Create an instance of the Summarizer class
summarizer = Summarizer()

# Function to browse for a file
def browse_file():
    filename = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, filename)

# Function to browse for stopwords file
def browse_stopwords():
    stopwords_file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    stopwords_entry.delete(0, tk.END)
    stopwords_entry.insert(0, stopwords_file)

# Function to summarize the text
def summarize_text():
    filename = file_entry.get()
    stopwords_file = stopwords_entry.get()
    language = language_combobox.get()

    if filename and stopwords_file and language:
        summarizer.read_stopwords_from_file(language, stopwords_file)
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        summary = summarizer.summarize(text)
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, summary)
    else:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Please provide all the required information.")

# Function to copy the summary to the clipboard
def copy_summary():
    summary = output_text.get(1.0, tk.END)
    pyperclip.copy(summary)

# Create the main window
window = tk.Tk()
window.title("Text Summarizer")

# Create labels and entry fields
file_label = tk.Label(window, text="Text File:")
file_label.grid(row=0, column=0, padx=10, pady=5)
file_entry = tk.Entry(window, width=30)
file_entry.grid(row=0, column=1, padx=10, pady=5)
file_button = tk.Button(window, text="Browse", command=browse_file)
file_button.grid(row=0, column=2, padx=5, pady=5)

stopwords_label = tk.Label(window, text="Stopwords File:")
stopwords_label.grid(row=1, column=0, padx=10, pady=5)
stopwords_entry = tk.Entry(window, width=30)
stopwords_entry.grid(row=1, column=1, padx=10, pady=5)
stopwords_button = tk.Button(window, text="Browse", command=browse_stopwords)
stopwords_button.grid(row=1, column=2, padx=5, pady=5)

language_label = tk.Label(window, text="Language:")
language_label.grid(row=2, column=0, padx=10, pady=5)
language_combobox = Combobox(window, values=["English", "Spanish"])
language_combobox.grid(row=2, column=1, padx=10, pady=5)

summarize_button = tk.Button(window, text="Summarize", command=summarize_text)
summarize_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

output_label = tk.Label(window, text="Summary:")
output_label.grid(row=4, column=0, padx=10, pady=5)
output_text = tk.Text(window, width=40, height=10)
output_text.grid(row=4, column=1, padx=10, pady=5)

copy_button = tk.Button(window, text="Copy", command=copy_summary)
copy_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()

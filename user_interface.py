import tkinter as tk
from tkinter import messagebox
from src.config import UI_TEXT_FIELD_ID, UI_MESSAGE_NAME


class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('GitHub Repo to PDF Converter')
        self.create_widgets()

    def create_widgets(self):
        self.repo_url_label = tk.Label(self.window, text='GitHub Repository URL:')
        self.repo_url_label.pack()

        self.repo_url_entry = tk.Entry(self.window, width=50)
        self.repo_url_entry.pack()

        self.convert_button = tk.Button(self.window, text='Convert to PDF', command=self.convert_to_pdf)
        self.convert_button.pack()

        self.message_label = tk.Label(self.window, text='', name=UI_MESSAGE_NAME)
        self.message_label.pack()

    def convert_to_pdf(self):
        repo_url = self.repo_url_entry.get()
        if not repo_url:
            messagebox.showerror('Error', 'Please enter a GitHub repository URL.')
            return

        try:
            # Call the convert_to_pdf function from the main module
            from src.main import convert_to_pdf
            convert_to_pdf(repo_url)
        except Exception as e:
            messagebox.showerror('Error', str(e))

    def run(self):
        self.window.mainloop()

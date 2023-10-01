```python
import tkinter as tk
from tkinter import messagebox
from src import config
from src import main

class UserInterface:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("GitHub Repo to PDF Converter")
        self.create_widgets()

    def create_widgets(self):
        self.repo_url_label = tk.Label(self.window, text="GitHub Repository URL:")
        self.repo_url_label.pack()

        self.repo_url_entry = tk.Entry(self.window)
        self.repo_url_entry.pack()

        self.convert_button = tk.Button(self.window, text="Convert to PDF", command=self.convert_to_pdf)
        self.convert_button.pack()

    def convert_to_pdf(self):
        repo_url = self.repo_url_entry.get()
        if not repo_url:
            messagebox.showerror("Error", "Please enter a GitHub repository URL.")
            return

        try:
            main.convert_repo_to_pdf(repo_url)
            messagebox.showinfo("Success", "The repository has been successfully converted to PDF.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    ui = UserInterface()
    ui.run()
```
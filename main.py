import tkinter as tk
from tkinter import filedialog, messagebox


class StickyNoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sticky Note")
        self.root.geometry("300x300")  # Increased height to accommodate buttons
        self.root.attributes('-topmost', True)  # Always on top

        self.transparency = False  # Track transparency state

        # UI Elements
        self.button_frame = tk.Frame(root)
        self.button_frame.pack(fill=tk.X, padx=5, pady=5)

        self.download_button = tk.Button(self.button_frame, text="Download", command=self.download_note)
        self.download_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        self.clear_button = tk.Button(self.button_frame, text="Clear All", command=self.clear_text)
        self.clear_button.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5, pady=5)

        self.text_frame = tk.Frame(root)
        self.text_frame.pack(expand=True, fill=tk.BOTH)

        self.scrollbar = tk.Scrollbar(self.text_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.text_area = tk.Text(self.text_frame, wrap=tk.WORD, font=("Arial", 12), bg="white",
                                 yscrollcommand=self.scrollbar.set)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=5, pady=5)
        self.scrollbar.config(command=self.text_area.yview)

        self.text_area.bind("<KeyRelease>", self.auto_save)

        # Bind focus in and out for automatic transparency
        self.root.bind("<FocusOut>", self.make_transparent)
        self.root.bind("<FocusIn>", self.make_opaque)

    def make_transparent(self, event=None):
        self.root.attributes('-alpha', 0.5)  # Semi-transparent
        self.text_area.configure(bg='light grey')

    def make_opaque(self, event=None):
        self.root.attributes('-alpha', 1.0)  # Opaque
        self.text_area.configure(bg='white')

    def auto_save(self, event=None):
        with open("autosave_note.txt", "w") as file:
            file.write(self.text_area.get("1.0", tk.END).strip())

    def download_note(self):
        content = self.text_area.get("1.0", tk.END).strip()
        if not content:
            messagebox.showwarning("Warning", "Note is empty! Nothing to save.")
            return

        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            try:
                with open(file_path, "w") as file:
                    file.write(content)
                messagebox.showinfo("Success", "Note saved successfully!")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save note: {e}")

    def clear_text(self):
        self.text_area.delete("1.0", tk.END)

    def on_close(self):
        self.auto_save()
        self.root.destroy()


def show_info_dialog():
    # Show info dialog box before opening the main GUI
    messagebox.showinfo("Welcome", "Welcome to the Sticky Note app! Click OK to start using the app.")


if __name__ == "__main__":
    show_info_dialog()  # Show info dialog before opening the main window
    root = tk.Tk()
    app = StickyNoteApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_close)
    root.mainloop()

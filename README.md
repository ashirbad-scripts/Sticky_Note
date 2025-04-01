# Sticky Note App

This is a simple Sticky Note app built using Python and Tkinter. Users can write, save, and clear notes. The app also supports transparency when unfocused.

## 🛠️ Requirements

- Python 3.6 or higher
- Tkinter (comes pre-installed with Python)
- PyInstaller (only required for `.exe` conversion)

## 📥 Installation

1. **Download the zip file** from this repository.
2. **Open the folder in a code editor and select a python interpreter**
3.  **Run  "main.py"**
     ```python main.py ```



## 🔄 Converting to .exe (Windows Only)

To create an executable `.exe` file from `main.py`, follow these steps:

1. **Install PyInstaller** (if not already installed):
   ```sh
   pip install pyinstaller
   ```
2. **Generate the `.exe` file**:
   ```sh
   pyinstaller --onefile --windowed main.py
   ```
   - `--onefile`: Packages everything into a single executable file.
   - `--windowed`: Hides the console window when running the app.

3. **Locate the `.exe` file**:
   - After the process completes, the `.exe` file will be inside the `dist/` folder.
   - Move the `.exe` file anywhere and run it without needing Python installed.

## 💡 Notes
- If you encounter any issues with PyInstaller, check if `pathlib` is installed and remove any conflicts.
- The `.exe` file is **platform-dependent** and will only work on Windows.

## 📜 License
This project is open-source and free to use.

---
Developed by Ashirbad

[Contact Me](https://ashirbad-scripts.github.io/Contact-me/)

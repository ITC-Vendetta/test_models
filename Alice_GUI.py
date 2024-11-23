import tkinter as tk
from tkinter import scrolledtext, messagebox, filedialog
import io

# Function to handle user input and display response
def on_send():
    query = entry.get()
    if not query.strip():
        return

    response = qwen(query)  # Assuming qwen is a function that returns the response from Qwen
    conversation_box.insert(tk.END, "User: " + query + "\n")
    conversation_box.insert(tk.END, "Qwen: " + response + "\n\n")
    entry.delete(0, tk.END)

# Function to handle file drop
def on_drop(event):
    files = event.data.split('\n')
    for file in files:
        if file and file.endswith('.txt'):  # Assuming you want to process only .txt files
            with open(file, 'r') as f:
                content = f.read()
                response = qwen(content)  # Assuming qwen processes the file content
                conversation_box.insert(tk.END, "File: " + file + "\n")
                conversation_box.insert(tk.END, "Qwen: " + response + "\n\n")

# Mock function to simulate Qwen's response
def qwen(input_text):
    return input_text.upper()  # Simple transformation for demonstration

# Create the main window
root = tk.Tk()
root.title("Alice GUI")
root.geometry("800x600")

# Conversation Box
conversation_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=20)
conversation_box.pack(fill=tk.BOTH, expand=True)

# Entry Box and Send Button
entry_frame = tk.Frame(root)
entry_frame.pack(side=tk.BOTTOM, fill=tk.X)

entry = tk.Entry(entry_frame, width=80)
entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
send_button = tk.Button(entry_frame, text="Send", command=on_send)
send_button.pack(side=tk.RIGHT)

# Allow dragging and dropping files into the conversation box
conversation_box.drop_target_register(tk.DND_FILES)
conversation_box.dnd_bind('<<Drop>>', on_drop)

root.mainloop()


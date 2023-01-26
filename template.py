import tkinter as tk
from tkinter import messagebox

def send_message():
    message = message_entry.get()
    # Replace this with your chatbot's response logic
    response = "Your chatbot's response"
    conversation.config(state=tk.NORMAL)
    conversation.insert(tk.END, "You: " + message + "\n")
    conversation.insert(tk.END, "Bot: " + response + "\n")
    conversation.config(state=tk.DISABLED)
    message_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Chatbot")

conversation_frame = tk.Frame(root)
conversation_frame.pack(padx=10, pady=10)

conversation = tk.Text(conversation_frame, state=tk.DISABLED)
conversation.pack()

message_frame = tk.Frame(root)
message_frame.pack(padx=10, pady=10)

message_entry = tk.Entry(message_frame)
message_entry.pack(side=tk.LEFT)

send_button = tk.Button(message_frame, text="Send", command=send_message)
send_button.pack(side=tk.RIGHT)

root.mainloop()

import tkinter as tk
from tkinter import filedialog, messagebox
from aes_module import encrypt_file, decrypt_file

def encrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if not password:
            messagebox.showwarning("Missing", "Enter password.")
            return
        encrypt_file(file_path, password)
        messagebox.showinfo("Success", "File encrypted successfully!")

def decrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        password = password_entry.get()
        if not password:
            messagebox.showwarning("Missing", "Enter password.")
            return
        try:
            decrypt_file(file_path, password)
            messagebox.showinfo("Success", "File decrypted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

root = tk.Tk()
root.title("AES-256 File Encryptor")

tk.Label(root, text="Enter Password:").pack(pady=5)
password_entry = tk.Entry(root, show="*", width=40)
password_entry.pack(pady=5)

tk.Button(root, text="Encrypt File", command=encrypt_action).pack(pady=5)
tk.Button(root, text="Decrypt File", command=decrypt_action).pack(pady=5)

root.geometry("300x200")
root.mainloop()

import os
from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import speech_recognition as sr

# Generate a key for encryption and decryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to capture voice command
def get_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        try:
            messagebox.showinfo("Voice Command", "Listening for command...")
            audio = recognizer.listen(source)
            messagebox.showinfo("Voice Command", "Processing command...")
            command = recognizer.recognize_google(audio)
            return command
        except sr.UnknownValueError:
            messagebox.showerror("Error", "Could not understand the voice command.")
            return None
        except sr.RequestError as e:
            messagebox.showerror("Error", f"Speech Recognition service error: {e}")
            return None

# Lock file using a voice command
def lock_file():
    file_path = filedialog.askopenfilename(title="Select a File to Lock")
    if not file_path:
        return

    command = get_voice_command()
    if not command:
        return

    # Encrypt the file content
    try:
        with open(file_path, "rb") as file:
            data = file.read()
            encrypted_data = cipher_suite.encrypt(data)
        
        # Save the encrypted file
        with open(file_path, "wb") as file:
            file.write(encrypted_data)
        
        # Save the voice command for unlocking
        global stored_command
        stored_command = command
        
        messagebox.showinfo("Success", "File locked successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error locking file: {e}")

# Unlock file using a voice command
def unlock_file():
    file_path = filedialog.askopenfilename(title="Select a File to Unlock")
    if not file_path:
        return

    command = get_voice_command()
    if not command:
        return

    if command != stored_command:
        messagebox.showerror("Error", "Voice command does not match!")
        return

    # Decrypt the file content
    try:
        with open(file_path, "rb") as file:
            encrypted_data = file.read()
            decrypted_data = cipher_suite.decrypt(encrypted_data)
        
        # Save the decrypted file
        with open(file_path, "wb") as file:
            file.write(decrypted_data)
        
        messagebox.showinfo("Success", "File unlocked successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error unlocking file: {e}")

def main():
    global stored_command
    stored_command = None  # To store the voice command used for locking
    
    root = Tk()
    root.title("Voice-Based File Locker")
    root.geometry("400x200")

    Label(root, text="Voice-Based File Locker", font=("Helvetica", 16)).pack(pady=10)
    Button(root, text="Lock File", command=lock_file, width=20, bg="lightblue").pack(pady=10)
    Button(root, text="Unlock File", command=unlock_file, width=20, bg="lightgreen").pack(pady=10)
    Button(root, text="Exit", command=root.quit, width=20, bg="lightcoral").pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
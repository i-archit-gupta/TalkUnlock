# 🎤 Voice-Based File Locker and Unlocker

A Python application that locks and unlocks files using voice commands. This project utilizes **speech recognition** for capturing commands, **file encryption** for securing data, and **Tkinter** for an intuitive graphical user interface.

## 🌟 Features
- 🔒 **File Locking**: Encrypt files with a voice command.
- 🔓 **File Unlocking**: Decrypt files using the same voice command.
- 🎙️ **Voice Command Recognition**: Powered by `SpeechRecognition` and `PyAudio`.
- 🖥️ **User-Friendly Interface**: Built with `Tkinter` for a simple and interactive GUI.

## 📋 Prerequisites
Ensure you have the following installed before running the project:

- Python 3.8 or above
- Required Python libraries:
  - `speechrecognition`
  - `pyaudio`
  - `cryptography`
  - `tkinter` (usually comes with Python)

- Install these libraries using:
```bash
pip install speechrecognition pyaudio cryptography
```

## 🛠️ How It Works
- Lock a File:
- Select a file.
- Provide a voice command to lock it. The file content is encrypted.
- Unlock a File:
- Select the locked file.
- Speak the same voice command to decrypt and unlock it.

## 🚀 Getting Started
- Step 1: Clone the Repository
```bash
git clone https://github.com/i-archit-gupta/TalkUnlock.git
cd TalkUnlock
```
- Step 2: Run the Script
```bash
python main.py
```
- Step 3: Interact with the Application. Use the GUI to lock and unlock files with voice commands.

## 📸 Flow Diagram

![Flow Diagram](/files/Sequence_Diagram_TalkUnlock.png)

## 💡 Acknowledgments
- SpeechRecognition Library: For voice input processing.
- Cryptography Library: For file encryption and decryption.
- Tkinter: For building the graphical interface.
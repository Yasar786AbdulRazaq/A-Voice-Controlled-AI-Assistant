markdown
# 🤖 A Voice-Controlled AI Assistant (J.A.R.V.I.S Clone)

Welcome to the **J.A.R.V.I.S-inspired AI Assistant** built using Python and Google’s powerful **Gemini Pro API**! This smart assistant listens to your voice, understands your commands, talks back, opens websites, answers questions using AI, and even sends emails — all hands-free! 🧠🎤💻

## 🔥 Demo Video
🎥 Watch the full working demo of this project on [YouTube](https://your-demo-link.com) *(Replace this with your video link)*

## 🌐 Live Repository
🔗 GitHub: [A-Voice-Controlled-AI-Assistant](https://github.com/Yasar786AbdulRazaq/A-Voice-Controlled-AI-Assistant.git)

---

## 🚀 Features

✅ Real-time speech recognition  
✅ Text-to-speech interaction using `pyttsx3`  
✅ Smart Q&A using Gemini Pro (Google LLM)  
✅ Opens Gmail, Google, YouTube, GitHub, LinkedIn by voice  
✅ Sends emails via Gmail SMTP  
✅ Greets user personally  
✅ Answers common greetings (like “How are you?” or “Hi Jarvis”)  
✅ Runs local apps like Notepad and Calculator  
✅ Time-telling functionality  
✅ Works on Windows with natural conversation flow  

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Google Gemini Pro API** (Generative Language API)
- **SpeechRecognition**
- **Pyttsx3** (Text-to-Speech)
- **Webbrowser**
- **Requests**
- **Smtplib**
- **Wikipedia API**

---

## 📦 Installation Guide

### Step 1: Clone the repository
```bash
git clone https://github.com/Yasar786AbdulRazaq/A-Voice-Controlled-AI-Assistant.git
cd A-Voice-Controlled-AI-Assistant
````

### Step 2: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Setup Environment

Create a `.env` file in the root folder and add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

> 💡 [Get your Gemini API key here](https://aistudio.google.com/app/apikey)

### Step 4: Run the Assistant

```bash
python jarvis.py
```

---

## 🧠 How It Works

* The assistant listens for your voice input using `SpeechRecognition`.
* Your voice is converted to text and checked against supported commands.
* If no match is found, it sends your question to Gemini Pro for a smart AI-powered reply.
* It uses `pyttsx3` to talk back to you.
* Supports natural conversations and personalizes responses using your name.

---

## 📸 Example Commands

| Command                         | Action                                 |
| ------------------------------- | -------------------------------------- |
| "Open my email"                 | Opens Gmail inbox                      |
| "Open my LinkedIn"              | Opens LinkedIn profile                 |
| "Who is the founder of Google?" | AI-generated answer via Gemini         |
| "Send email"                    | Prompts for email content and sends it |
| "Open notepad"                  | Opens Notepad app                      |
| "What time is it now?"          | Tells the current time                 |
| "How are you?"                  | Replies: “I am fine Yasar, my friend…” |
| "Hi Jarvis"                     | Wakes up and responds personally       |

---

## 🧪 Tested On

✅ Windows 10/11
✅ Python 3.10+
✅ Google Gemini API

---

## 🙌 Contributing

Pull requests are welcome! If you have ideas or want to add more features like weather, reminders, or AI chat memory — fork this repo and go for it. 💡

---

## 👨‍💻 Author

**Yasar Abdul Razaq**
📫 [LinkedIn](https://www.linkedin.com/in/yasarabdulrazaq)
💻 [GitHub](https://github.com/Yasar786AbdulRazaq)

---

## ⭐ If you like this project

Drop a ⭐ on [this repo](https://github.com/Yasar786AbdulRazaq/A-Voice-Controlled-AI-Assistant.git) and share it to inspire more developers!
Let’s build the future of Human-AI interaction! 🌍🧠

```

Would you like me to create a nice `requirements.txt` file for this project as well?
```

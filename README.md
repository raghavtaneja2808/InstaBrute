
---

# 🚨 Instagram Password Cracker using Selenium

> **⚠️ Disclaimer: For Educational Purposes Only!**  
> This tool is designed to demonstrate the importance of strong passwords and cybersecurity practices.  
> **Do not use this tool for unauthorized activities.** Misuse may result in legal consequences.

---

## 📌 Introduction

This project uses **Selenium** to simulate human-like login attempts on Instagram. It includes a **custom wordlist generator** that builds password guesses based on natural patterns, making the process more realistic and less detectable by Instagram's anti-bot systems.

---

## ⚙️ How It Works

### 1. 🔐 Automated Login with Selenium
- **Automated Interaction**: Opens Instagram in a browser and inputs credentials.
- **Human-Like Simulation**: Slow typing, natural pauses, and realistic interaction prevent bot detection.

#### ✅ Key Features:
- Customizable delays
- Complete login automation
- Real-time feedback (success/failure status)

---

### 2. 🧠 Human-Like Wordlist Generator
Generates passwords using personal data and common user patterns.

#### 🛠️ Inputs:
- First/Last name
- Date of birth
- Nickname / Instagram username
- Significant names or dates

#### 🔄 How It Generates:
- Combines names, dates, special characters
- Mimics real password creation (e.g., `John@1996`, `Doe_!21`)
- Extensive combinations = better results

---

### 3. 🕵️ Stealth Features
Designed to avoid detection by Instagram's bot protection.

- **Variable Delays**: Configurable delay between attempts
- **Manual Typing Simulation**: Simulates human typing speed
- **Slower Submission Rates**: Less likely to trigger security flags

---

## 🚀 Getting Started

### 📁 Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/instagram-password-cracker.git
cd InstaBrute
cd instbrute
```

### 📦 Step 2: Install Dependencies
Make sure Python is installed, then run:
```bash
pip install -r requirements.txt
```

### 🧾 Step 3: Generate the Wordlist
Run the generator and follow the prompts:
```bash
python wordlist_creator.py
```
> Output file: `wordlist.txt`

### 💥 Step 4: Start Cracking!
Launch the cracker script with the target username:
```bash
python instagram_cracker.py --username <target_username> --wordlist wordlist.txt
```

---

## 💡 Special Features

| Feature               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| 🎯 Custom Wordlists   | Uses personal info for smarter guesses                                      |
| 🕶️ Stealth Mode       | Human-like delays and typing patterns                                       |
| ⏱️ Configurable Delay | Adjust login speed to avoid detection                                       |
| 📊 Real-Time Feedback | Instant info on login status (success/failure/blocked)                      |

---

## 📃 License

Licensed under the **Apache License 2.0**.  
See the [LICENSE](LICENSE) file for more details.

---

## ❗ Important Notes

- **Only test accounts you own or have explicit permission for.**
- **Avoid using this on your main Instagram account.** Too many failed attempts can result in account lockout.
- Contributions, improvements, and feedback are always welcome!

---

## 🙌 Stay Ethical

This tool is for learning and awareness only. Let’s build a safer internet together. 🛡️  
**Strong passwords save lives.**

---


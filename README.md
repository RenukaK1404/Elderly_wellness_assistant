#  Elderly Wellness Assistant 
### A Smart Companion for Safer, Healthier Aging – Built with AI, Streamlit, and Compassion

---

## 🚀 Overview

**Elderly Wellness Assistant** is a lightweight, AI-integrated Streamlit application designed to support elderly individuals in maintaining their health, safety, and daily routine with dignity and independence.

From tracking vitals to fall detection, and from managing daily reminders to having a friendly AI-powered conversation — this project offers a unified, intelligent assistant experience tailored for senior citizens and their caregivers.

---

## 🎯 Problem Statement

> _"How might we empower the elderly population to live independently while ensuring timely health alerts, safety checks, and emotional well-being — all through a cost-effective and accessible platform?"_

This project addresses that challenge by fusing **health monitoring**, **routine reminders**, **safety surveillance**, and **AI-powered conversation**, all in one app that works offline with local LLMs (like Ollama) — ensuring **privacy**, **reliability**, and **zero subscription cost**.

---

## 💡 Key Features

### 🩺 **Health Monitoring**
- Enter and visualize vitals: **Heart Rate**, **Glucose**, **SpO₂**
- Alerts for abnormal values using clinical thresholds
- Historical data display with automatic tagging (✅ Normal / 🟥 Alert)
- Advice from a local **LLM (e.g., Ollama running LLaMA 3)** for basic suggestions

### ⏰ **Daily Reminders**
- View scheduled medications, routines, or therapy sessions
- Mark reminders as “Done ✅”
- Real-time visual status: 🟢 Done / 🔴 Pending

### 🛡️ **Safety Monitoring**
- Fall detection and movement activity logs
- Location-based safety records
- Alert status per entry

### 🤖 **AI Assistant**
- Talk to your local LLM in a friendly, chat-like interface
- Ask health questions, emotional support, or general guidance
- Powered by **Ollama + LLaMA 3** (fully local, offline-capable)

---

## 🛠️ Tech Stack

| Tool/Library     | Purpose                        |
|------------------|--------------------------------|
| `Streamlit`      | UI Framework                   |
| `Pandas`         | CSV data loading & management  |
| `Matplotlib`     | Visualizing vital signs        |
| `Streamlit-Lottie` | Adding animations for UX     |
| `Ollama` + `LLaMA 3` | Lightweight local LLM for AI conversations |
| `Python`         | Core programming language      |

---
## 🧪 Installation & Running the App

1. **Clone the Repository**
   ```bash
   git clone https://github.com/RenukaK1404/Elderly_wellness_assistant.git
   cd elderly-wellness-assistant
   
2. **Set Up Python Environment**

 ```sh
pip install -r requirements.txt
```
3. **Run the Streamlit App**

```sh
streamlit run elderly.py
(Optional) Ensure Ollama is Installed for LLM Support
```
4. **Install Ollama**

Run the LLaMA model:
```sh
  ollama run llama3
```

### 🌍 Target Audience
- Elderly individuals living alone
- Caregivers and family members
- NGOs, early intervention centers, and home care services
- Smart Home Health Startups

### 🚀 Future Scope
  -  Integrate real-time vitals from IoT sensors (ESP32, Raspberry Pi, etc.)
  -  Deploy on mobile/tablet via Streamlit cloud or PWA
  -  Add notifications (SMS/email) to caregivers on alert
  -  Use pose estimation (OpenCV) to enhance fall detection

### 🏆 Why This Project Stands Out
  -  Privacy-first: Offline-ready with local AI model
  -  Zero cost to scale for homes or rural care centers
  -  Multi-dimensional support: health, routine, safety, companionship
  -  Hackathon-ready innovation — smart, impactful, and realistic
  -  Empathy-driven design — built with purpose for those who need it most

### 👥 Team
“Built with care by young engineers passionate about healthcare + technology.”
- Aafizaa K
- Renuka K	



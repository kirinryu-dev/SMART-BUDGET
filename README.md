# 💸 SMART BUDGET

[EN/FR] Simple budget tracker with personality

![Preview](assets/imgs/preview.png)

## 🚨 Important Deployment Notice
**This project requires Python/Flask backend** and cannot be directly deployed to:
- GitHub Pages (static hosting only , to deploy will have to recreate the page using JS)
- Vercel (Node.js focused , doesnt support anything else other than JS)

🔧 Local usage required - runs on your machine via Python

## 🚀 Local Setup Guide

### Requirements
- Python 3.x
- Modern web browser
- Basic terminal knowledge

### Quick Start
1. Clone repository:
```bash
git clone https://github.com/yourusername/SMART_BUDGET.git

Navigate to project folder: 
cd SMART_BUDGET
next go to the script folder
cd script
Run Flask application:
python smart_budget.py
Open in browser :
Automatically opens at ==> http://localhost:5000
 (If not, manually type the address  bar)

## Key Features
💰 Budget Checkup
Enter your:

Monthly income

Main expenses (housing/food/transport)

Savings amount

🎭 Instant Feedback
Get colorful responses:

text
✅ "Yatta! Pro money moves! （＾∀＾●）ﾉｼ" 
⚠️ "Aka alert! In the red! ！yabai!!"
😅 "Cutting it close...だけど walla"


## Project Structure

SMART_BUDGET/
├── public/          # Web pages
│   ├── index.html   # Home portal
│   └── result.html  # Results display
├── script/          # Python core
│   └── smart_budget.py (Flask server)
└── assets/          # Design assets
    └── css/
        └── style.css


///// Troubleshooting 
If you get "ModuleNotFoundError" mean you dont have pip instaled :

pip install flask 
Keep the terminal open while using the app - closing it stops the server or use ctrl + c to manually stop the server


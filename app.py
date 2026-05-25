import os
import random
from flask import Flask, render_template

# This finds the exact, absolute folder path where this app.py file is sitting
base_dir = os.path.dirname(os.path.abspath(__file__))

# This explicitly tells Flask exactly where to find the static and templates folders
app = Flask(__name__, 
            static_folder=os.path.join(base_dir, 'static'),
            template_folder=os.path.join(base_dir, 'templates'))

MOOD_BOOSTERS = [
    {
        "message": "Hey you... yes, YOU! Just a reminder that you are doing your absolute best, and I am incredibly proud of you. Take a deep breath. 💖",
        "image": "cute1.gif",
        "bgm": "bgm1.mp3"
    },
    {
        "message": "Sending you a massive, warm, squishy virtual hug right now! 🧸 You are not alone, and this tough moment will pass. Hang in there, love!",
        "image": "cute2.gif",
        "bgm": "bgm2.mp3"
    },
    {
        "message": "If nobody told you today: Your smile is beautiful, your heart is pure gold, and the world is a much brighter place just because you are in it. ✨",
        "image": "cute3.gif",
        "bgm": "bgm3.mp3"
    },
    {
        "message": "It is completely okay to feel overwhelmed and take a break. Your productivity doesn't define your worth. Rest up, drink some water, and be gentle with yourself. 🌸",
        "image": "cute4.gif",
        "bgm": "bgm4.mp3"
    },
    {
        "message": "You have survived 100% of your hardest days so far. You are so much stronger than you give yourself credit for! Sending you endless love and strength. 💕",
        "image": "cute5.gif",
        "bgm": "bgm5.mp3"
    },
    {
        "message": "Here is a tiny pocket full of sunshine and a million hearts for you! ☀️❤️ You are deeply cared for, deeply loved, and so precious.",
        "image": "cute6.gif",
        "bgm": "bgm6.mp3"
    },
    {
        "message": "Just checking in to wrap you in a blanket of comfort. Take it one tiny step at a time. I'm cheering for you every single day! 🐾💖",
        "image": "cute7.gif",
        "bgm": "bgm7.mp3"
    },
    {
        "message": "You are a literal gem. 💎 Don't let a bad day make you feel like you have a bad life. Tomorrow is a fresh start, but for now, close your eyes and feel this huge hug! 🥰",
        "image": "cute8.gif",
        "bgm": "bgm8.mp3"
    }
]

@app.route('/')
def home():
    booster = random.choice(MOOD_BOOSTERS)
    return render_template('index.html', booster=booster)

if __name__ == '__main__':
    app.run(debug=True)
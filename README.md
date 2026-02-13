Project Overview

Gamer Play Tracker is a Python + MongoDB based data analytics project that records and manages gamers' play history. It allows users to store and update games they play, track playtime, analyze gaming behavior, and visualize insights such as most played games, favorite genres, and total gaming hours.

This project demonstrates Python, MongoDB, data analysis, and visualization skills for a Data Analyst / Data Science portfolio.

🚀 Features

Add new game records

Update last played and playtime

View all stored games

Delete game records

Gaming analytics (most played game, total hours, favorite genre, average rating)

Data visualization using Matplotlib

Export dataset to CSV for analytics / BI tools

Secure MongoDB connection using .env

🧱 Tech Stack

Python 3.12

MongoDB

PyMongo

Pandas

Matplotlib

python-dotenv

📂 Project Structure
gamer-play-tracker/
│
├── gamer_tracker.py
├── requirements.txt
├── .gitignore
├── .env.example
├── README.md
└── data/
    └── sample_gamer_data.json (optional)

⚙️ Installation & Setup
1. Clone Repository
git clone https://github.com/your-username/gamer-play-tracker.git
cd gamer-play-tracker

2. Install Dependencies
pip install -r requirements.txt

3. Setup MongoDB Connection

Create a .env file in the project root:

MONGO_URI=mongodb://localhost:27017


For MongoDB Atlas:

MONGO_URI=your_atlas_connection_string

4. Run the Project
python gamer_tracker.py

📊 Example Analytics

Most played game

Total gaming hours

Favorite genre

Average rating

Hours played per game (Bar Chart)

📁 Export Dataset

You can export your tracked data:

gamer_data.csv


Useful for:

Power BI

Tableau

Machine Learning

Data Analysis

🔐 Security

MongoDB credentials stored securely using .env

.env is excluded using .gitignore

.env.example provided for safe setup

📈 Future Improvements

Streamlit Dashboard

Game Recommendation System (ML)

User Login System

MongoDB Atlas Cloud Integration

Advanced Gaming Trend Analysis

👨‍💻 Author

Vansh Mahajan
Data Science / Data Analyst Enthusiast

⭐ If you like this project

Give it a star ⭐ on GitHub

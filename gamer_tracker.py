# ==============================
# Gamer Play Tracker (Safe Version)
# ==============================

try:
    from pymongo import MongoClient
except ModuleNotFoundError:
    print("\n❌ ERROR: pymongo is not installed in THIS Python environment.")
    print("👉 Run this in CMD:")
    print("   python -m pip install pymongo pandas matplotlib\n")
    exit()

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# ==============================
# MongoDB Connection (Safe)
# ==============================

try:
    client = MongoClient(
        "mongodb://localhost:27017/",
        serverSelectionTimeoutMS=3000)
    client.server_info()   # Force connection test
    db = client["gamer_tracker"]
    collection = db["games"]
    print("✅ Connected to MongoDB successfully!")
except Exception:
    print("\n❌ ERROR: MongoDB is NOT running.")
    print("👉 Start MongoDB OR install MongoDB Community Server.")
    exit()

# ==============================
# Add Game
# ==============================


def add_game():
    username = input("Username: ")
    game = input("Game name: ")
    genre = input("Genre: ")
    hours = int(input("Hours played: "))
    rating = int(input("Rating (1-10): "))
    date = datetime.now().strftime("%Y-%m-%d")

    data = {
        "username": username,
        "game_name": game,
        "genre": genre,
        "hours_played": hours,
        "last_played": date,
        "rating": rating
    }

    collection.insert_one(data)
    print("✅ Game added!")


# ==============================
# Update Game
# ==============================

def update_game():
    game = input("Game to update: ")
    add_hours = int(input("Add hours: "))
    date = datetime.now().strftime("%Y-%m-%d")

    result = collection.update_one(
        {"game_name": game},
        {"$inc": {"hours_played": add_hours},
         "$set": {"last_played": date}}
    )

    if result.modified_count:
        print("✅ Updated!")
    else:
        print("❌ Game not found!")

# ==============================
# View Games
# ==============================

def view_games():
    games = list(collection.find())

    if not games:
        print("No data found!")
        return

    for g in games:
        print("\n🎮", g["game_name"])
        print("User:", g["username"])
        print("Genre:", g["genre"])
        print("Hours:", g["hours_played"])
        print("Last Played:", g["last_played"])
        print("Rating:", g["rating"])

# ==============================
# Delete Game
# ==============================

def delete_game():
    game = input("Game to delete: ")
    result = collection.delete_one({"game_name": game})

    if result.deleted_count:
        print("🗑️ Deleted!")
    else:
        print("❌ Game not found!")

# ==============================
# Analyze Data
# ==============================

def analyze():
    data = list(collection.find())
    if not data:
        print("No data!")
        return

    df = pd.DataFrame(data)

    print("\n📊 Analytics")
    print("Most Played:", df.loc[df['hours_played'].idxmax()]['game_name'])
    print("Total Hours:", df['hours_played'].sum())
    print("Favorite Genre:", df['genre'].value_counts().idxmax())
    print("Avg Rating:", round(df['rating'].mean(), 2))

# ==============================
# Plot Hours
# ==============================

def plot_hours():
    data = list(collection.find())
    if not data:
        print("No data!")
        return

    df = pd.DataFrame(data)
    df.groupby("game_name")["hours_played"].sum().plot(kind="bar")
    plt.title("Hours per Game")
    plt.tight_layout()
    plt.show()

# ==============================
# Export CSV
# ==============================

def export_csv():
    data = list(collection.find())
    if not data:
        print("No data!")
        return

    df = pd.DataFrame(data)
    df.drop(columns=["_id"], inplace=True)
    df.to_csv("gamer_data.csv", index=False)
    print("📁 Exported to gamer_data.csv")


# ==============================
# Menu
# ==============================

def menu():
    while True:
        print("\n🎮 Gamer Tracker")
        print("1 Add Game")
        print("2 Update Game")
        print("3 View Games")
        print("4 Delete Game")
        print("5 Analyze")
        print("6 Plot")
        print("7 Export CSV")
        print("8 Exit")

        c = input("Choice: ")

        if c == "1":
            add_game()
        elif c == "2":
            update_game()
        elif c == "3":
            view_games()
        elif c == "4":
            delete_game()
        elif c == "5":
            analyze()
        elif c == "6":
            plot_hours()
        elif c == "7":
            export_csv()
        elif c == "8":
            break
        else:
            print("Invalid!")


menu()

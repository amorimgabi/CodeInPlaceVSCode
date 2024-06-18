"""
file: outdoor_activity_suggestion.py
------------------------------------
This program creates a simple graphical user interface (GUI) to suggest outdoor activities based on the 
user's selected type (e.g., nature, cultural, sports, leisure) from a dropdown menu.
It uses the python library tkinter.
"""

import tkinter as tk
import random

# Define the categorized activities dictionary
activities = {
    "nature": {
        "beach": "Spend a peaceful time hearing the sound of the waves.",
        "hiking": "Explore nature and get some exercise by hiking a nearby trail.",
        "gardening": "Get your hands dirty and enjoy the therapeutic benefits of gardening.",
        "camping": "Set up a tent and enjoy a night under the stars.",
        "bird_watching": "Grab a pair of binoculars and watch birds in their natural habitat.",
        "stargazing": "Lay on a blanket and gaze at the stars on a clear night."
    },
    "cultural": {
        "bookstore": "Go pick a brand new story to dig into a whole new world!",
        "museum": "Visit a museum and immerse yourself in art and history.",
        "farmers_market": "Visit a local farmers market and discover fresh produce and handmade goods.",
        "street_fair": "Stroll through a street fair and enjoy the food, music, and local crafts."
    },
    "sports": {
        "cycling": "Go for a bike ride and explore new areas around your city.",
        "rock_climbing": "Challenge yourself with some rock climbing at a local climbing spot.",
        "beach_volleyball": "Join a game of beach volleyball and have some fun in the sun."
    },
    "leisure": {
        "concert": "Why not put a blanket over at the park and enjoy listening to that live concert?",
        "picnic": "Pack a picnic basket and enjoy a meal outdoors with friends or family.",
        "photography": "Take your camera and capture the beauty of the outdoors.",
        "kayaking": "Paddle along a river or lake and enjoy the tranquility of the water.",
        "fishing": "Spend a relaxing day by the lake or river fishing.",
        "amusement_park": "Have fun and enjoy the rides at an amusement park.",
        "zoo": "Visit the zoo and learn about different animals from around the world."
    }
}

# Function to suggest an activity based on the selected type
def suggest_activity():
    selected_type = activity_type_var.get()
    if selected_type in activities:
        activity = random.choice(list(activities[selected_type].keys()))
        description = activities[selected_type][activity]
        suggestion_label.config(text=f"Activity: {activity.capitalize()}\n\n{description}")
    else:
        suggestion_label.config(text="Please select a valid activity type.")

# Create the main window
root = tk.Tk()
root.title("Outdoor Activity Recommender")

# Set a larger font size for the button and label
font_large = ('Helvetica', 14)
# Set a different font and size for the description text
font_description = ('Helvetica', 12)

# Create and place the option menu for selecting activity type
activity_type_var = tk.StringVar(root)
activity_type_var.set("Select Activity Type")

activity_type_menu = tk.OptionMenu(root, activity_type_var, *activities.keys())
activity_type_menu.config(font=font_large)
activity_type_menu.pack(pady=10)

# Create and place the button with a larger font
button = tk.Button(root, text="Let's have fun today", command=suggest_activity, font=font_large)
button.pack(pady=10)

# Create and place the label to display the suggestion with the description font
suggestion_label = tk.Label(root, text="", wraplength=300, font=font_description)
suggestion_label.pack(pady=20)

# Run the application
root.mainloop()

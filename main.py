
import random
from datetime import datetime

# -----------------------------
# GAME VARIABLE
# -----------------------------
guess_number = random.randint(1, 10)

# -----------------------------
# MEMORY VARIABLES
# -----------------------------
name = ""

# -----------------------------
# TASK LIST
# -----------------------------
tasks = []

# -----------------------------
# RESPONSES
# -----------------------------
responses = {
    "greetings": [
        "Hello 😊",
        "Hi there!",
        "Hey!"
    ],

    "how_are_you": [
        "I'm doing great!",
        "Awesome 😄",
        "Doing well!"
    ],

    "thanks": [
        "You're welcome 😊",
        "Happy to help!",
        "No problem!"
    ],

    "bye": [
        "Goodbye 👋",
        "Take care!",
        "See you later!"
    ]
}


# -----------------------------
# MAIN BOT FUNCTION
# -----------------------------
def get_bot_response(user_input):

    global name
    global guess_number
    global tasks

    clean_input = user_input.lower().strip()

    # -----------------------------
    # EXIT
    # -----------------------------
    if clean_input in ["bye", "exit", "quit"]:
        return random.choice(responses["bye"])

    # -----------------------------
    # NAME MEMORY
    # -----------------------------
    elif clean_input.startswith("my name is"):

        name = user_input[11:].strip().title()

        return f"Nice to meet you, {name}!"

    elif clean_input == "what is my name":

        if name:
            return f"Your name is {name} 😊"

        return "I don't know your name yet."

    # -----------------------------
    # TIME
    # -----------------------------
    elif "time" in clean_input:

        current_time = datetime.now().strftime("%H:%M:%S")

        return f"Current time is {current_time}"

    # -----------------------------
    # DATE
    # -----------------------------
    elif "date" in clean_input:

        current_date = datetime.now().strftime("%d-%m-%Y")

        return f"Today's date is {current_date}"

    # -----------------------------
    # GREETINGS
    # -----------------------------
    elif any(word in clean_input for word in ["hello", "hi", "hey"]):

        return random.choice(responses["greetings"])

    # -----------------------------
    # HOW ARE YOU
    # -----------------------------
    elif "how are you" in clean_input:

        return random.choice(responses["how_are_you"])

    # -----------------------------
    # THANKS
    # -----------------------------
    elif "thank" in clean_input:

        return random.choice(responses["thanks"])

    # -----------------------------
    # JOKES
    # -----------------------------
    elif "joke" in clean_input:

        jokes = [
            "Why do programmers hate nature? Too many bugs 😂",
            "Why was Python sad? Because it had too many exceptions 😄",
            "I would tell you a UDP joke... but you might not get it 😎"
        ]

        return random.choice(jokes)

    # -----------------------------
    # MOOD
    # -----------------------------
    elif "sad" in clean_input:

        return "I'm sorry you're feeling sad 💙"

    elif "happy" in clean_input:

        return "That's amazing 😊"

    # -----------------------------
    # ROCK PAPER SCISSORS
    # -----------------------------
    elif clean_input == "play rps":

        return "Choose: rock, paper, or scissors"

    elif clean_input in ["rock", "paper", "scissors"]:

        bot_choice = random.choice(
            ["rock", "paper", "scissors"]
        )

        if clean_input == bot_choice:
            return f"I chose {bot_choice}. It's a tie 😄"

        elif (
            (clean_input == "rock" and bot_choice == "scissors")
            or
            (clean_input == "paper" and bot_choice == "rock")
            or
            (clean_input == "scissors" and bot_choice == "paper")
        ):
            return f"I chose {bot_choice}. You win 🎉"

        else:
            return f"I chose {bot_choice}. I win 🤖"

    # -----------------------------
    # COIN TOSS
    # -----------------------------
    elif clean_input == "flip coin":

        return random.choice([
            "Heads 🪙",
            "Tails 🪙"
        ])

    # -----------------------------
    # DICE ROLL
    # -----------------------------
    elif clean_input == "roll dice":

        return f"🎲 You rolled a {random.randint(1,6)}"

    # -----------------------------
    # MAGIC 8 BALL
    # -----------------------------
    elif clean_input == "magic 8 ball":

        answers = [
            "Yes definitely!",
            "No way!",
            "Maybe...",
            "Ask again later.",
            "Absolutely!"
        ]

        return "🔮 " + random.choice(answers)

    # -----------------------------
    # NUMBER GUESSING GAME
    # -----------------------------
    elif clean_input == "guess game":

        guess_number = random.randint(1, 10)

        return "Guess a number between 1 and 10"

    elif clean_input.isdigit():

        if int(clean_input) == guess_number:

            guess_number = random.randint(1, 10)

            return "Correct! 🎉"

        return "Wrong guess 😄 Try again"

    # -----------------------------
    # CALCULATOR
    # -----------------------------
    elif any(op in clean_input for op in ["+", "-", "*", "/"]):

        try:

            result = eval(clean_input)

            return f"🧮 Answer: {result}"

        except:

            return "Invalid calculation 😕"

    # -----------------------------
    # TODO MANAGER
    # -----------------------------
    elif clean_input.startswith("add task"):

        task = user_input[8:].strip()

        if task:
            tasks.append(task)
            return f"✅ Task added: {task}"

        return "Please enter a task."

    elif clean_input == "show tasks":

        if not tasks:
            return "No tasks found."

        result = "📋 Tasks:\n"

        for i, task in enumerate(tasks, start=1):
            result += f"{i}. {task}\n"

        return result

    # -----------------------------
    # DEFAULT
    # -----------------------------
    else:

        return "Sorry, I didn't understand that 😕"


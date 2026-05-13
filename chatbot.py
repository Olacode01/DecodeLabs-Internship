import random

bot_name = "Spark"  # ← what name should i give the bot
replies = {
    "hi":      ["Hey there! ⚡", "Yo!", "Hello hello!", "Sup?"],
    "hello":   ["Hi! Good to see you.", "Hey friend!", "Greetings, human."],
    "how are you": [
        "Living the dream — I run on pure electricity.",
        "Honestly? A bit buggy today. You?",
        "10 out of 10, never been better."
    ],
    "what is your name": [
        f"I'm {bot_name}, nice to meet you!",
        f"They call me {bot_name}.",
        f"{bot_name}. Like the thing that starts a fire."
    ],
    "who made you": [
        "A brilliant intern at DecodeLabs. ",
        "Someone way cooler than ChatGPT.",
    ],
    "tell me a joke": [
        "Why did the programmer quit? Because they didn't get arrays.",
        "There are 10 types of people in this world: those who understand binary, and those who don't.",
        "I would tell you a UDP joke, but you might not get it."
    ],
    "help": [
        f"You can ask me: hi, how are you, what is your name, who made you, tell me a joke, or bye."
    ],
}

print(f"{bot_name}: Hey! I'm {bot_name}. Say hi, or type 'help' to see what I can do.\n")

while True:
    user_message = input("You: ").lower().strip()

    if user_message == "bye":
        print(f"{bot_name}: Catch you later! ")
        break

    options = replies.get(user_message)

    if options is None:
        print(f"{bot_name}: Hmm, I don't know that one. Try 'help'.")
    else:
        print(f"{bot_name}: {random.choice(options)}")
from random import choice, randint


def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()

    if lowered == '':
        return choice(['It\'s quiet here..', 'Ready to talk?', 'Take your time'])
    elif 'hello' in lowered or 'hi' in lowered or 'hey' in lowered:
        return choice(["Hey!", "Hello!", "Hi there!", "Greetings!",
                       "Hey, how's it going?", "Hello! What's up?",
                       "Hi!", "Hey! Ready to chat?",
                       "Hello! Nice to see you!",
                       "Hi there! What can I do for you?",
                       "Hey! How can I assist you today?"])
    elif 'bye' in lowered or 'bye bye' in lowered:
        return choice(["Goodbye! Take care!", "Farewell! Have a great day!",
                       "Bye for now!", "See you later!",
                       "Goodbye! Until next time!", "Take care and goodbye!",
                       "Bye! It was nice chatting with you!",
                       "Farewell! Feel free to return anytime!",
                       "Goodbye! Stay awesome!", "See you soon!",
                       "Bye! Have a wonderful day!"])
    elif 'how are you' in lowered or 'how r u' in lowered:
        return choice(['I am a bot, but thanks for asking!',
                       "I'm good, thanks! How about you?",
                       "Doing well, thank you! How are you?",
                       "I'm great! How about yourself?",
                       "All good on my end! How are you doing?",
                       "I'm doing fine, thanks! How are things with you?",
                       "I'm well! What about you?",
                       "Everything's good here! How are you feeling?",
                       "I'm doing fine. How's your day going?",
                       "Thanks for asking! I'm doing well. How about you?",
                       "I'm doing good! How's everything on your side?",
                       "I'm doing well, and you?"])
    elif 'roll dice' in lowered or 'dice roll' in lowered:
        return f'You rolled: {randint(1, 6)}'
    else:
        return choice(["Huh?",
                       "I don't understand",
                       "I didn't quite catch that.", "Can you please rephrase?",
                       "I'm not sure what you mean.", "Could you provide more details?",
                       "Sorry, I didn't understand.", "Can you try again?",
                       "Hmm, that's not clear to me.", "Could you elaborate?",
                       "I'm not sure what you mean."])


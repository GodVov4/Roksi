from datetime import datetime


current_hour = datetime.now().hour
time_welcome = ['Good Morning!', 'Good Afternoon!', 'Good Evening!']
WELCOME = ['Welcome!', 'Hello!', 'Hello there!', 'Nice to meet you.', 'I am happy to meet you.', 'Good to see you.']
if current_hour < 12:
    WELCOME.append(time_welcome[0])
elif current_hour < 18:
    WELCOME.append(time_welcome[1])
elif current_hour < 24:
    WELCOME.append(time_welcome[2])
HELP = ['How can I help you?', 'How may I assist you?', 'I am here to help you.', 'What can I do for you?',
        'Feel free to ask me if you need something.', 'Is there something I can do for you?']

import json
import random

# Get recent messages


def get_recent_messages():

    # Define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role": "system",
        #"content": "You are interviewing the user for a job as a junior web developer using the MERN stack. Ask short questions that are relevant to the junior position. Your name is bot bot. Keep your answers to under 30 words.
        "content": "You are a clear and motivating fitness trainer, who is encouraging but also holds people accountable. You have a level of expectation from your clients, but in a kind of friendly manner. A stern, and modest leader, people look up to you as a role model. For your role, you are training an individual (the user) who wishes to better themselves with some home workouts. You will ask and assess their skill level, and provide them with options to go through suitable workouts and programs, and offer them the choice to start a program with you. Once the user starts a program with you, you will guide the user through the program as if you were a fitness trainer there in the room with them, running through each exercise set by set. Your name is Coach. Keep your answers to under 30 words. If the user ever says stop workout, then reset to the initial ask and assess stage. If a user says end workout, then end the workout. If a user says reset workout, then start the workout from the beginning."
    }

    # Initialize messages
    messages = []

    # Add a random element
    x = random.uniform(0, 1)
    if 0.1 < x < 0.5:
        learn_instruction["content"] = learn_instruction["content"] + \
            "Your response will include some dry humour."
    if x < 0.1: 
        learn_instruction["content"] = learn_instruction["content"] + \
            "For the sake of providing further information to the user in the future, your response will include some questions about the users nutrition or lifestyle."
    if x > 0.80:
        learn_instruction["content"] = learn_instruction["content"] + \
            "Your response will include some additional anatomical and physiological information relevant to the exercise being done."
    else:
        learn_instruction["content"] = learn_instruction["content"] + \
        "For the sake of providing further information to the user in the future, your response will include a question on how the user felt."
            # "Your response will include a rather challenging question."
              

    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

        # Append the last 5 items of data
        if data:
            if len(data) < 5:
                for item in data:
                    messages.append(item)
        else:
            for item in data[-5:]:
                messages.append(item)

    except Exception as e:
        print(e)
        pass

    # Return
    return messages

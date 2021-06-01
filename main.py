import Mentifxxr
from Picker import KEYS_UP, Picker
import random
from threading import Thread

# Repeat input until it can be converted to int
def int_input(prefix: str, message_error="Value Error, input is an integer") -> int:
    while True:
        try:
            res = int(input(prefix))
            return res
        except ValueError:
            print(message_error)


def spam(q_info, answers) -> None:
    q_id = Mentifxxr.getActiveQuestionid(q_info)
    q_type = Mentifxxr.getActiveQuestionType(q_info)

    times = len(answers)
    ids = list()

    def get_new_id():
        ids.append(Mentifxxr.getNewID())

    id_threads = list()

    for x in range(times):
        t = Thread(target=get_new_id)
        id_threads.append(t)

    for x in range(times):
        id_threads[x].start()
        print("\rCharging up:", x + 1, "/", times, end="\r")
    print()

    for x in range(times):
        id_threads[x].join()
        print("\rFinishing:", x + 1, "/", times, end="\r")
    print()

    def send_answer(q_info, answer, answer_id):
        Mentifxxr.answer(q_id, q_type, answer_id, q_info, answer)

    answer_threads = list()

    for x in range(times):
        t = Thread(target=send_answer, args=(q_info, answers[x], ids[x]))
        answer_threads.append(t)

    for x in range(times):
        try:
            answer_threads[x].start()
            print("\rSending:", x + 1, "/", times, end="\r")
        except KeyboardInterrupt:
            print("Interrupt detected, breaking")
            break
    print()

    print("\nFinished")


RANDOM_WORDLIST = [
    "favor",
    "heavyweight",
    "became",
    "habit",
    "battleground",
    "growl",
    "fundamental",
    "rear",
    "estimate",
    "quantum",
    "soon",
    "ambitious",
    "grappler",
    "limitless",
    "nuclear",
    "bluster",
    "teeth",
    "crutch",
    "pigeon",
    "bed",
]

# Constant picker options
WORDCLOUD_PICKER_OPTIONS = (
    "Send one big number",
    "Send random numbers",
    "Send random words",
    "Send specific word",
)
CHOICES_PICKER_OPTIONS = ("Choose randomly", "Choose all", "Choose specific")
OPEN_PICKER_OPTIONS = (
    "Send 250 random digits",
    "Send specific message (less than 250 symbols)",
)
SCALES_PICKER_OPTIONS = ("Send random values", "Send specific values")


pin = input("Input Pin: ")
pin = "".join(pin.split())

q_info = Mentifxxr.getInfo(pin)

q_type = Mentifxxr.getActiveQuestionType(q_info)
q_id = Mentifxxr.getActiveQuestionid(q_info)

while True:
    Mentifxxr.printInfo(q_info)

    try:
        input("Press enter to continue")
    except KeyboardInterrupt:
        print("\nInterrupt detected, exiting")
        exit(0)

    if q_type == "wordcloud":
        option_index = Picker(
            f"Question type is {q_type}. Choose an option", WORDCLOUD_PICKER_OPTIONS
        ).start()[1]

        word = str()
        if option_index == 0:
            # Send one big nubmer
            digits_count = int_input("Digits count: ")

            for x in range(digits_count):
                word += str(random.randint(0, 9))
            print(f"Your answer: {word}")

            times = int_input("Times: ")
            answers = [word] * times
            spam(q_info, answers)

        elif option_index == 1:
            # Send random numbers (from 1 to 10000)

            times = int_input("Times: ")
            answers = [str(random.randint(1, 10000)) for x in range(times)]
            spam(q_info, answers)

        elif option_index == 2:
            # Send random words

            times = int_input("Times: ")
            answers = [random.choice(RANDOM_WORDLIST) for x in range(times)]
            spam(q_info, answers)
        elif option_index == 3:
            # Send specific word
            word = input("Your word: ")

            times = int_input("Times: ")
            spam(q_info, [word] * times)

    elif q_type in ("choices", "choices_images", "winner", "ranking"):
        choices = Mentifxxr.listChoices(q_info)

        option_index = Picker(
            f"Question type is {q_type}. Choose an option", CHOICES_PICKER_OPTIONS
        ).start()[1]

        if option_index == 0:
            # Choose randomly

            times = int_input("Times: ")
            answers = [random.randint(1, len(choices)) for x in range(times)]
            spam(q_info, answers)

        elif option_index == 1:
            # Choose all

            times = int_input("Times: ")
            answers = [x % len(choices) + 1 for x in range(times)]
            spam(q_info, answers)

        elif option_index == 2:
            # Choose specific

            chosen_no = Picker(f"Choose specific answer", choices).start()[1] + 1
            times = int_input("Times: ")
            answers = [chosen_no] * times
            spam(q_info, answers)

    elif q_type == "open":
        option_index = Picker(
            f"Question type if {q_type}. Choose an option", OPEN_PICKER_OPTIONS
        ).start()[1]

        if option_index == 0:
            # Send 250 random digits

            message = "".join([str(random.randint(0, 9)) for x in range(250)])
            print(f"Your message: {message}")

        elif option_index == 1:
            # Send specific message

            message = input("Your message: ")
            if len(message) > 250:
                print("Your message is too long, slicing")
                message = message[:250]

        times = int_input("Times: ")
        answers = [message for x in range(times)]
        spam(q_info, answers)

    elif q_type == "scales":
        option_index = Picker(
            f"Question type if {q_type}. Choose an option", SCALES_PICKER_OPTIONS
        ).start()[1]

        answers = list()
        min_ans, max_ans = (
            Mentifxxr.getActiveQuestionMinMax(q_info)["min"],
            Mentifxxr.getActiveQuestionMinMax(q_info)["max"],
        )
        if option_index == 0:
            # Send random values

            while len(answers) < len(Mentifxxr.getActiveQuestion(q_info)):
                answers.append(random.randint(min_ans, max_ans))
        elif option_index == 1:
            # Send specific values

            val = int_input(f"Enter value from {min_ans} to {max_ans}: ")
            while True:
                if min_ans <= val <= max_ans:
                    answers.append(val)
                    break
                else:
                    print(f"Value must be between {min_ans} and {max_ans}")
                    continue

        formatted_answers = dict()
        for question in Mentifxxr.getActiveQuestion(q_info):
            for x in range(len(answers)):
                formatted_answers[question["id"]] = [answers[x], 1]

        times = int_input("Times: ")
        answers = [formatted_answers for x in range(times)]
        spam(q_info, answers)

    elif q_type == "qfa":
        # TODO
        pass
    else:
        print(f"Type 'f{q_type}' is not expected")
        break

# from madison import main_program
import madison
from timinator import CONGRATS
import random

def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success true")


def fail():
    print("TECHIO> success false")
    

if __name__ == "__main__":
    generate_madisons_projections()
    success()
    send_msg(f"{random.choice(CONGRATS)} 🌟", "You have given Madison a tremendous head start down her future path!!!")

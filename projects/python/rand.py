# im just learning, don't judge my shit script!
import random
import time

default_chance = 10

def readData():
    try:
        with open("score.txt", "r") as file:
            content = file.read().strip()
            if not content: # if filr is empty
                return default_chance
            return int(content)
    except (FileNotFoundError, ValueError): 
        # if file is missing or corrupted
        return default_chance

def writeData(value):
    with open("score.txt", "w") as file:
        file.write(str(value))
    return value

chance_max = readData()
wins = 0

def startGame(livez):
    global wins; global chance_max
    while wins < 5:
        roll = random.randint(1, int(chance_max))
        print(f"Rolling 1-{int(chance_max)}... Got: {roll}")

        if roll == 7:
            wins += 1
            print(f"WIN #{wins}!")
            chance_max *= 2
            
            if livez > 100:
                pass # learned something new here
            else:
                livez = 5
            
            writeData(chance_max) 
        else:
            livez -= 1
            print(f"{livez} lives left!")
            if livez <= 0:
                print("Game over!")
                break
        time.sleep(0.5)


print("Game Menu")
print("1. Start game.")
print("2. Start game with infinite lives.")
print("3. View Max score.")
print("4. Reset data.")
choice = input("I choose: ")

if choice == "1":
    print("Starting game!")
    time.sleep(1.0)
    startGame(5)

elif choice == "2":
    print("Starting game with INFINITE lives, you cheater.")
    time.sleep(1.0)
    startGame(999999)

elif choice == "3":
    print(f"Your current difficulty is: 1 in {chance_max}")

elif choice == "4":
    chance_max = writeData(default_chance)
    print("Data reset to the default chance (10)")

else:
    print("Choose a valid option!!")
    exit()

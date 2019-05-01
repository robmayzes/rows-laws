import random
import time

# Import laws from txt file

all_laws = open("Laws.txt")
str_laws = all_laws.read()
laws = str_laws.split('\n')
print(laws)
all_laws.close()

# Update parameters here

days = 5
total_laws = 47
sleep_time = 5

# laws = [Law1, Law2, Law3, Law4, Law5, Law6, Law7, Law8, Law9, Law10, Law11, Law12, Law13, Law14, Law15, Law16, Law17, Law18, Law19, Law20, Law21, Law22, Law23, Law24, Law25, Law26, Law27, Law28, Law29, Law30, Law31, Law32, Law33, Law34, Law35, Law36, Law37, Law38, Law38, Law40, Law41, Law42, Law43, Law44, Law45, Law46, Law47]

# Leave the rest as is

laws_per_day = total_laws/days
int_laws_per_day = int(laws_per_day)

for day in range(days-1):
    print("\nMorning Rob! Ready for your daily principles?")

    for today in range(int_laws_per_day):
        input("\n>>> Press enter to see the next law...\n")
        current_law = random.choice(laws)
        print(current_law)
        laws.remove(current_law)
        time.sleep(sleep_time)

    print("\nThat's it for today! Come back tomorrow, Rob.\n\n---------------------------------\n")
    time.sleep(600)

while len(laws) != 0:
	input("\n>>> Press enter to see the next law...\n")
	current_law = random.choice(laws)
	print(current_law)
	laws.remove(current_law)
	time.sleep(sleep_time)


print("\nThat's all of the laws. See you next week, Rob!\n")

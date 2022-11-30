import random

length = int(input("length [default 1000]: ") or "1000")
width = int(input("width [default 1000]: ") or "1000")
percentage = float(input("bomb_probability [default 0.5]: ") or "0.5")
with open("mine.txt", "w") as file:
    for _ in range(0, length + 1):
        file.write("".join(['*' if random.random() < percentage else "." for x in range(0, width + 1)]) + "\n")

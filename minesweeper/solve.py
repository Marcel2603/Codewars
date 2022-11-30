import re

neighbour_eight = [
    (-1, -1), (0, -1), (1, -1),
    (-1, 0), (1, 0),
    (-1, 1), (0, 1), (1, 1)
]

bomb_indices = {}
result = list()
lines = 0
with open("mine.txt", "rt") as file:
    for index, line in enumerate(file, 0):
        clean_line = line.strip()
        bombs = [m.start() for m in re.finditer("\*", clean_line)]
        if bombs:
            bomb_indices[index] = bombs
        result.append([0] * len(clean_line))
        lines = index
for line in bomb_indices:
    for bomb in bomb_indices[line]:
        result[line][bomb] = "*"
        for x, y in neighbour_eight:
            new_x = bomb + x
            new_y = line + y
            if 0 <= new_y <= lines and \
                    0 <= new_x < len(result[new_y]):
                neighbour = result[new_y][new_x]
                if not neighbour == "*":
                    result[new_y][new_x] += 1
result_formatted = "\n".join([f for f in ["".join([str(t) for t in x]) for x in result]])
with open("result.txt", "w") as result_file:
    result_file.writelines(result_formatted)
# print(result_formatted)

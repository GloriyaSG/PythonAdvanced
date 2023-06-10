#d yel blu e low redd
from collections import deque

string = deque(input().split())


def check_colors(first_word,sec_word):
    word = first_word + sec_word
    word_2 = sec_word + first_word
    if word in main_colors:
        colors.append(word)
    elif word_2 in main_colors:
        colors.append(word_2)
    elif secondary_colors.get(word):
        colors.append(word)
    elif secondary_colors.get(word_2):
        colors.append(word_2)
    else:
        for x in (first[:-1], second[:-1]):
            if x:
                string.insert(len(string) // 2, x)

main_colors = {"red","yellow","blue"}

#"orange","purple","green"

secondary_colors = {
    "orange": {"yellow", "red"},
    "purple": {"red", "blue"},
    "green": {"yellow", "blue"},
}

colors = []


while string:
    first = string.popleft()
    second = string.pop() if string else ""
    check_colors(first,second)


for color in set(secondary_colors.keys()).intersection(colors):
    if not secondary_colors[color].issubset(colors):
            colors.remove(color)


print(list(colors))

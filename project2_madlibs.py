with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = -1

target_start = "<"
target_end = ">"

for i, chat in enumerate(story):
    if chat == target_start:
        start_of_word = i

    if charr == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
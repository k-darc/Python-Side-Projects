with open("story.txt", "r") as f:
    story = f.read()

words = []
start_of_word = -1

for i, chat in enumerate(story):
    
file_path = "/home/frappe-pukat/Documents/Mini Python Project/story.txt"  


with open(file_path, "r") as f:
    story = f.read()

words = []
start_of_word = -1

target_start = "<"
target_ends = ">"

for i , char in enumerate(story):
    if char == target_start:
        start_of_word = i
    if char == target_ends and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.append(word)
        start_of_word = -1

answers = {}

for word in words:
    answer = input("Enter a word for " + word + ": ")
    answers[word] = answer

for word in words:
    story = story.replace(word, answers[word])

print(story)

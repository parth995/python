from urllib.request import urlopen
story = urlopen('http://sixty-north.com/c/t.txt')
story_words = []
for line in story:
    line_words = line.decode('utf-8').split()
   # \print(line_words)
    for word in line_words:
        story_words.append(word)
story.close()
print(story_words)

for word in story_words:
    print(word)
import re

# Filter out 5-letter words
open("5letter.txt","w").writelines([ word for word in open("words.txt") if len(word) == 6 and re.match("^[A-Za-z]*$", word)])

positions = [{},{},{},{},{}]
for pos in positions:
    for letter in "abcdefghijklmnopqrstuvwxyz":
        pos[letter] = 0

# Strip words
words = list(open("5letter.txt","r"))
for i in range(len(words)):
    words[i] = words[i].strip("\n").lower()
    
# Count letter occurrences per position
for word in words:
    pos = 0
    for letter in word:
        positions[pos][letter] += 1
        pos += 1

 
# Score words
wordscores = {}
for word in words:
    wordscores[word] = 0;
    pos = 0
    for letter in word:
        wordscores[word] += positions[pos][letter]
        pos += 1


# Sort by highest word scores
wordscores = list(sorted(wordscores.items(), key=lambda item: item[1]))

wordscores_all = wordscores

mostcommon = list(open("mostcommon5.txt", "r"))
for i in range(len(mostcommon)):
    mostcommon[i] = mostcommon[i].strip("\n")

def displaywords():
    # Print out top 20 words
    top = wordscores[len(wordscores)-20 if len(wordscores) > 20 else 0::]
    for word in top:
        if mostcommon.count(word[0]) < 1:
            mostcommon.append(word[0])
    top.sort(key=lambda word: mostcommon.index(word[0]))
    for i in range(len(top)-1, -1, -1):
            print(str(i+1) + ": " + top[i][0] + " at score " + str(top[i][1]))

while True:
    wordscores = wordscores_all.copy()
    while True:
        displaywords()
        wordled = input("Wordle'd: ")
        wordmask = input("Worked: ")
        if wordled.lower() == "!redo" or wordmask.lower() == "!redo":
            continue
        elif wordled.lower() == "!restart" or wordmask.lower() == "!restart":
            break
        else:
            letteroccurs = {}
            wordstripped = wordled
            rl = 0
            for i in range(len(wordled)):
                if wordmask[i] == "0":
                    wordstripped = wordstripped[:i-rl] + wordstripped[i-rl+1:]
                    rl += 1
            removed_words = 0
            for word in range(len(wordscores)):
                for mask in range(len(wordmask)):
                    letteroccurs[letter] = 1
                    checkword = wordscores[word - removed_words][0]
                    if wordmask[mask] == "0":
                        if checkword[mask] == wordled[mask]:
                            del(wordscores[word - removed_words])
                            removed_words += 1
                            break
                        elif checkword.count(wordled[mask]) > wordstripped.count(wordled[mask]):
                            del(wordscores[word - removed_words])
                            removed_words += 1
                            break
                            
                    elif wordmask[mask] == "1":
                        if checkword[mask] == wordled[mask] or checkword.count(wordled[mask]) < wordstripped.count(wordled[mask]):
                            del(wordscores[word - removed_words])
                            removed_words += 1
                            break
                    elif wordmask[mask] == "2":
                        if checkword[mask] != wordled[mask]:
                            del(wordscores[word - removed_words])
                            removed_words += 1
                            break

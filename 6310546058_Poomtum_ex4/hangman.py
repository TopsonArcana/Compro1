from random import randint
word_list = ['python', 'java', 'kotlin', 'javascript']
print(r"""                    
                            _____
|     |     /\     |\    | |       |\        /|     /\     |\    |
|     |    /  \    | \   | |       | \      / |    /  \    | \   |
|-----|   /----\   |  \  | | ____  |  \    /  |   /----\   |  \  |
|     |  /      \  |   \ | |     | |   \  /   |  /      \  |   \ |
|     | /        \ |    \| |_____| |    \/    | /        \ |    \|
""")
print("")
# List consisting each letter from randomed word
word = [str(i) for i in word_list[randint(0, 3)]]
# List of "-"" by the length of word to be replace later on
guess = ["-" for i in word]
check = []  # List to check if entered letter has duplicate
print("".join(guess))
lives = 8
while "-" in guess:  # GUESSING PART until - are all replaced
    letter = input("Input a letter: >")
    dindex = []  # List to contain index of duplicate
    for i in range(len(word)):  # Iterate through the alphabet in word
        if letter == word[i]:  # if letter is the same as any alphabet in word
            dindex.append(i)  # append all index of that alphabet
    # check if letter exist in word and no duplicate letter
    if letter in word and len(dindex) < 2:
        # replace - at the alphabet index with that letter
        guess[word.index(letter)] = letter
        print("".join(guess))
    # check letter exist but duplicate letter
    elif letter in word and len(dindex) == 2:
        # replace - at the first alphabet index with the letter
        guess[dindex[0]] = letter
        # replace - at the second alphabet index with the letter
        guess[dindex[1]] = letter
        print("".join(guess))
    else:  # Guess wrong
        lives -= 1 
        if letter in check:  # Check if the new input letter exist the check list
            print("No improvements")
        else:
            # if letter aren't alerady exist in check,append the wrong input into check list
            check.append(letter)
            print("No such letter in the word")
    if lives == 0:
        print("You are hanged")
        break
    elif "-" not in guess:
        print("You guessed the word!")
        print("You survived!")
        break

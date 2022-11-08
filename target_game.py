"""
target
"""
from typing import List
import random

def generate_grid() -> List[List[str]]:
    """
    Generates list of lists of letters - i.e. grid for the game.
    e.g. [['I', 'G', 'E'], ['P', 'I', 'S'], ['W', 'M', 'G']]
    """
    ans = []
    letters = "qwertyuiopasdfghjklzxcvbnm"
    for i in range(3):
        tmp = []
        for j in range(3):
            tmp.append(letters[random.randint(0,25)])
        ans.append(tmp)
    return ans



def get_words(f: str, letters: List[str]) -> List[str]:
    """
    Reads the file f. Checks the words with rules and returns a list of words.
    """
    
    arr = []
    data = []
    ans = []
    cent = letters[4]
    for l in letters:
        tpl = (l, letters.count(l))
        if tpl not in arr:
            arr.append(tpl)

    with open(f) as f:
        lines = f.readlines()
        for line in lines:
            data.append(line.lower().rstrip())
    tmp_ans = []
    for word in data:
        if (len(word) > 4) and (cent not in word):
            tmp_ans.append(word)
    for word in tmp_ans:
        tf = True
        for l in word:
            if l not in letters:
                tf = False
        if tf:
            ans.append(word)
    tmp = []
    for tpl in arr:
        for word in ans:
            if word.count(tpl[0]) > tpl[1]:
                tmp.append(word)
    ans = [word for word in ans if word not in tmp]
    return ans




def get_user_words() -> List[str]:
    """
    Gets words from user input and returns a list with these words.
    Usage: enter a word or press ctrl+d to finish for *nix or Ctrl-Z+Enter 
    for Windows.
    Note: the user presses the enter key after entering each word.
    """
    print("Enter your words:")
    ans = []
    try:
        while True:
            word = input()
            ans.append(word)
    except EOFError:
        pass
    except KeyboardInterrupt:
        pass
    return ans



def get_pure_user_words(user_words: List[str], letters: List[str], words_from_dict: List[str]) -> List[str]:
    """
    (list, list, list) -> list

    Checks user words with the rules and returns list of those words
    that are not in dictionary.
    """
    pass


def results():
    pass

print(get_words('en.txt', ['a','b','c','d','e','f','g','h','a']))
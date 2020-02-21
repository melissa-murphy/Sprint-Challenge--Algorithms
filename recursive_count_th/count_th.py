'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''

# Last time through I ended up using python's count -- which passed the tests, but did not use recursion. ¯\(°_o)/¯
# This time 👇 we have recursion :D

def count_th(word):

    # Find the length
    # Remove one letter per pass until len <= 1
    # Return the count of "th"

    count = 0

    if len(word) <= 1:
        return 0

    elif word[:2] == "th":
        count += 1
        count += count_th(word[1:])

    else:
        count += count_th(word[1:])

    return count

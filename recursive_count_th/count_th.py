'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0
    if 'th' in word:
        if word[0] + word[1] == 'th':
            count = 1
            return count + count_th(word[2:])
        else:
            return count + count_th(word[1:])ß
    else:
        return count


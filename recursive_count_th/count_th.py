'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # TBC
    count = 0
    # Check if 'th' exists in the word
    if 'th' in word:
        # Check if the first two letters are 'th'
        if word[0] + word[1] == 'th':
            # Add to the count, remove the first two letters, repeat and add the count
            count = 1
            return count + count_th(word[2:])
        else:
            # Remove the first letter, repeat and add the count
            return count + count_th(word[1:])
    else:
        # Return the current count
        return count


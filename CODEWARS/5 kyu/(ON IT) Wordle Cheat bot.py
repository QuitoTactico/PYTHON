# https://www.codewars.com/kata/6255e6f2c53cc9001e5ef629/train/python

# {"SHEEP", "KINKY", "SWEET", "MAUVE", "FLUNG", "SKEET", ... }  # wordlist
# [("SPOIL", "G----"), ("STEAD", "GYG--"), ("SEETH", "GYGY-")]  # guesses


from typing import List, Set, Tuple

# return a filtered set of words
def wordle(wordlist:Set[str], guesses:List[Tuple[str]]) -> Set[str]:
    word_len = len(guesses[0][1])
    word_final = {i:"" for i in range(word_len)}

    char_located = {}
    char_total = {}
    char_banned = set()

    for guess_word, guess_result in guesses():

        for i, guess_char in enumerate(guess_result):

            if guess_char == 'G':

                # new char!!!
                if word_final[i] != guess_word[i]:

                    word_final[i] = guess_word[i]

                    if guess_word[i] in char_located:
                        char_located[guess_word[i]] += 1
                    else:
                        char_located[guess_word[i]] = 1


            # is in the result, but not in the position
            elif guess_char == 'Y':
                if guess_word[i] in char_total:
                    char_total[guess_word[i]] += 1
                else:
                    char_total[guess_word[i]] = 1

            # this char isn't in the final result
            elif guess_char == '-':
                char_banned.add(guess_word[i])

                
        


    #return set()
# Game Rules
#
# Both players are given the same string, S.
# Both players have to make substrings using the letters of the string S.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
#
# Scoring
# A player gets +1 point for each occurrence of the substring in the string S.
#
# For Example:
# String  = BANANA
# Kevin's vowel beginning word = ANA
# Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
#
# Input Format
#
# A single line of input containing the string .
# Note: The string  will contain only uppercase letters: .
#
# Constraints
# 0 < len(S) <= 10^6
#
# Output Format
# Print one line: the name of the winner and their score separated by a space.
# If the game is a draw, print Draw.
# "Y" is not a vowel for this problem.


def minion_game(s):
    vowels = ['A', 'E', 'I', 'O', 'U']
    kevin = 0
    stuart = 0
    size = len(s)
    for i in range(size):
        if s[i] in vowels:
            kevin += (size - i)
        else:
            stuart += (size - i)
    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin < stuart:
        print("Stuart", stuart)
    else:
        print("Draw")


in_str = "BANANA"
minion_game(in_str)



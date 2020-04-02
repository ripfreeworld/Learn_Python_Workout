
word = input("Enter a word: ")

if word[0] in 'aeiou':
    print(f'{word}way')
else:
    print(f'{word[1:]}{word[0]}ay')

# congruent
# start_with_vowel = False
# for vowel in 'aeiou':
#     if word[0] == vowel:
#         start_with_vowel = True
#         break
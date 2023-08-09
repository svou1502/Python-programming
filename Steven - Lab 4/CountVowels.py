word = input("Enter a word: ")
vowel_count = 0  # Initialize the counter for vowels

for letter in word:
    if letter in 'aeiouAEIOU':
        vowel_count += 1

print("Number of vowels in the word:", vowel_count)


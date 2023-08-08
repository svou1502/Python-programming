word = input("Enter a word: ") # Ask user to input
vowel_count = 0

for char in word:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowel_count += 1

print(f"The word '{word}' contains {vowel_count} vowels.")


sentence = "This a sentence with words separated by spaces."
vowel_count = 0
for letter in sentence:
    if letter in "aeiou": # if letter is a vowel from "sentence"
        vowel_count += 1
print("There are", vowel_count, "vowels in the sentence.")

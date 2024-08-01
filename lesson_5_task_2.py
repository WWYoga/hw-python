vowels = "aeiou"

word = input("enter the word: ").lower()

vowel_count = 0
consonant_count = 0

vowel_dict = {vowel: 0 for vowel in vowels}

for letter in word:
    if letter in vowels:
        vowel_count += 1
        vowel_dict[letter] += 1
    elif letter.isalpha():
        consonant_count += 1

all_vowels_present = all(vowel_dict[vowel] > 0 for vowel in vowels)

print(f"number of vowel: {vowel_count}")
print(f"number of consonant: {consonant_count}")

for vowel, count in vowel_dict.items():
    print(f"number '{vowel}': {count}")

if all_vowels_present:
    print("True")
else:
    print("False")


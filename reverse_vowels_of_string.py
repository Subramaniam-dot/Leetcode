def reverseVowels(s):
    vowels = "aeiouAEIOU"
    vowel_list = [char for char in s if char in vowels]
    reversed_vowels = vowel_list[::-1]

    result = []
    reverse_index = 0

    for char in s:
        if char in vowels:
            result.append(reversed_vowels[reverse_index])
            reverse_index += 1

        else:
            result.append(char)

    final = "".join(result)

    return final


# Test the function
print(reverseVowels("Hello"))  # Expected output: "Holle"

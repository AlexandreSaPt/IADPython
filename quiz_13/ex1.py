#Write a function that, given a sentence, returns the number of words starting with a vowel.

def words_start_vowel(sentence):
    vowelList = ('a', 'e', 'i', 'o', 'u')

    count = 0
    sentence = sentence.lower()
    idx = 0
    for character in sentence:
        if (idx == 0 and character in vowelList):
            count += 1

        if character == ' ':
            if sentence[idx + 1] in vowelList:
                count += 1
        idx += 1
    return count


print(words_start_vowel('aoday I will go to the aovies'))

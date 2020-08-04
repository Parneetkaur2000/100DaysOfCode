Given a non-empty string of lowercase letters and a non-negative integer representing a key, Write a function that returns a new string obtained by shifting any
letter in the input string by k positions in the alphabet, where k is the key. Note that letters should "wrap" around the alphabet; in other words, the letter "z"
shifted by one returns the letter "a".

***************
def caesarCipherEncryptor(string, key):
    result = ''
    for i in range(len(string)):
        char = string[i]
        if (char.islower()):
            result += chr((ord(char)+key-97)%26 + 97)
        else:
            result += chr((ord(char) +key-65)%26 +65)
    return result

if __name__ == '__main__' :
    string = 'xyz'
    key = 2
    print(caesarCipherEncryptor(string,key))

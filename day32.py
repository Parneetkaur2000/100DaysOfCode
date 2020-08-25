Given a string, find all possible palindromic partitions of given string.

************************

def string_substring(input_string, palindrome_partion, temp, j, length):
    if j >= length:
        x = temp[:]
        palindrome_partion.append(x)
        return

    for i in range(j, length):
        
        if input_string[j:i:] == input_string[i:j:-1]: #check if the substring is a palindrome
            temp.append(input_string[j:i+1]) # append the palindrome string to the temp list
            string_substring(input_string, palindrome_partion, temp, i+1, length) #recursivly call the function 

            temp.pop()

def recursive_palindrome(input_string):
    palindrome_partion = [] #to store all the partions
    length = len(input_string)
    res = [] #to store the final result
    temp = []
    string_substring(input_string, palindrome_partion, temp, 0, length) 
    
    for i in range(0, len(palindrome_partion)):
        res.append(" ".join(palindrome_partion[i]))
    return res
if __name__ == "__main__":
  input_string = "nitin"
  print(recursive_palindrome(input_string))

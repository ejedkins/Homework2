#Elijah Jedkins PSID: 1786452

''' Type your code here. '''
user_input= input()
palindrome = reversed(user_input)
  
if list(user_input) == list(palindrome):
    print(user_input, "is a palindrome")
else:
    print(user_input, "is not a palindrome")
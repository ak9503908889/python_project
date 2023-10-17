'''palindrome no =
A palindrome is a word, phrase, number, or any other sequence of characters that reads the same forward
and backward. In other words, it('s a sequence that remains unchanged when its characters are reversed.'
 Palindromes can be found in various contexts)'''

given_value=input("Enter the value ")
Reversed_value=given_value[::-1]          # here slicing opration is perform for reverse the value
if given_value==Reversed_value:
    print("its a palindrome")
else:
    print("its not palindrome")
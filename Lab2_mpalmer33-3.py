"""
String Manipulator
Melissa Palmer,
The purpose of this program is to take user input and manipulate it to print it out backwards at the end.,
Any info about starter code (If used, where it came from, link, etc.),
1/25/26
 """
 
print("Hello there! This program will take your input and print out your orginal message as well as a backwards version.")

User= input("Enter a string message: ")

reversed_string = User[::-1]

print(f'Orginal message:{User}' f'\nreversed message:{reversed_string}')



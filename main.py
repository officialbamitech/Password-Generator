import random

upperCaseLetters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
lowerCaseLetters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
signs = ["^", "!", "§", "$", "%", "&", "/", "(", ")", "=", "?", "{", "[", "]", "}", "_", "-"]

def generateRandomPassword():
  passwordPart1 = random.choice(upperCaseLetters) + random.choice(lowerCaseLetters) + str(random.randint(0, 9)) + random.choice(signs)
    
  passwordPart2 = random.choice(upperCaseLetters) + random.choice(lowerCaseLetters) + str(random.randint(0, 9)) + random.choice(signs)
    
  newPassword = passwordPart1 + passwordPart2
  print('Your generated password is:', newPassword)
  
generateRandomPassword()
username = input("What\'s your username?")
password = input("What\'s your password?")
password = ('*' * len(password))
passwordlength = len(password) 

print(f'{username}, your password {password} is {passwordlength} characters long.')
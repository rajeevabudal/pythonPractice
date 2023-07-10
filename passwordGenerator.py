import random;

def shuffle(string):
    tempList = list(string);
    random.shuffle(tempList)
    return ''.join(tempList)

password1 = chr(random.randint(65,90));
password2 = chr(random.randint(65,90));

password = password1 + password2;
password = shuffle(password);
print(password);
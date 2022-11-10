print('Access verification')
user_age = int(input('Enter your age: '))
def access_verify(age):
    if age < 18:
        return "access not allowed"
    elif age > 100:
        return "Age not allowed"
    else:
        return "Access allowed"
19
print(access_verify(user_age))
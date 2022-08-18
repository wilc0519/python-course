print('Access verification')
print('Enter your age:')

user_age = int(input())
def access_verify(age):
    if age >= 18:
        return "Access allowed"
    else:
        return "Access denied"

print(access_verify(user_age))
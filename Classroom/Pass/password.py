def check_password(password):
    safety = True
    if password.isdigit() \
            or password.isalpha() \
            or password.lower == password \
            or password.upper == password \
            or len(password) < 10:
        safety = False
    return safety


print(check_password("Кукареку1234"))
print(check_password("Ямайкаааааа"))
print(check_password("qwerty123"))

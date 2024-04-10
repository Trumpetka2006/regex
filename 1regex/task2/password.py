import re

# Přijímá hesla o délce 8-16 znaků, obsahující alespoň jedno velké písmeno, jedno číslo a jeden speciální znak.
def validate_password(password):

    rules = [r'^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,16}$']
    status = False

    for reg in rules:
        if re.match(reg,password):
            status = True
        else:
            status = False
            break

    print(status)
    return status
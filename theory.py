"""Function with output"""
'''def my_function():
    # result = operation
    # Return the result'''


def format_name(f_name, l_name):
    return f"{f_name.title()} {l_name.title()}"


formated_name = format_name('GLENN', 'bonaventura')
print(formated_name)
print(format_name('glenn', 'BONAVENTURA'))

"""Function inside function"""


def echo_text(text):
    return text * 2


def format_text(text):
    return text.title()


print(format_text(echo_text('hElO')))
print(echo_text(format_text('hElO')))

"""Multiple output function"""


def format_name(f_name, l_name):
    if f_name == '' and l_name == '':
        return "Please insert the right value"
    return f"{f_name.title()} {l_name.title()}"


print(format_name(input('First Name:\t'), input('Last Name: \t')))

"""Leap year"""


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


is_leap_year(2024)

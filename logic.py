import math
import re

def evaluate_expression(expression):
        
    try:

        expression = re.sub(r'(\d+)%', r'(\1/100)', expression)

        result = eval(expression)

        return result
    
    except Exception:

        return "Error"
    
def calculate_sqrt(number):

    try:

        number = float(number)

        if number < 0:

            return "The number must not be negative!"
        
        result  = math.sqrt(number)

        return result
    
    except Exception:

        return "Error!"

def clear_expression():

    return ""
    
def format_number(number):

    try:
        
        number = float(number)

        if number.is_integer():

            return "{:,}".format(int(number))
        
        else:

            return "{:,}".format(number)
        
    except:
        
        return str(number)
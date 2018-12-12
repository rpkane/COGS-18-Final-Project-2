import string
import random

def remove_punctuation(input_string):
    out_string = ''
    for char in input_string:
        if char not in string.punctuation:
            out_string += char
        else:
            continue
    return out_string

def prepare_text(input_string):
    temp_string = input_string.lower()
    temp_string = remove_punctuation(temp_string)
    out_list = temp_string.split()
    return out_list 

def selector(input_list, check_list, return_list):
    output = None
    for item in input_list:
        if item in check_list:
            output = random.choice(return_list)
            continue
        else:
            output = None
    return output

def prepare_numbers(numbers):
    numb = []
    for item in numbers:
        numb.append(int(item))
    return numb

def calculate(numbers, operator):
    if operator == 'add':
        return add(prepare_numbers(numbers))
    elif operator == 'subtract':
        return subtract(prepare_numbers(numbers))
    elif operator == 'multiply':
        return multiply(prepare_numbers(numbers))
    elif operator == 'divide':
        return divide(prepare_numbers(numbers))
    elif operator == 'remainder':
        return remainder(prepare_numbers(numbers))
    elif operator == 'power':
        return power(prepare_numbers(numbers))

def end_chat(input_list):
    if str('quit') in input_list:
        output = True
        return output
    else:
        output = False
        return output

def encryption(msg):
    start_key = 123
    key_increment = 4
    string = []
    encoded = []
    key = start_key
    message = msg
    for c in range(0, len(message)):
        code = ord(message[c])
        change = code+key
        new = chr(change)
        string += new
        key += key_increment
    
    encoded = ''.join(string)
    return ('Encoded Message:\t' + encoded)

def decryption(msg):
    start_key = 123
    key_increment = 4
    string = []
    decoded = []
    key = start_key
    message = msg
    for c in range(0, len(message)):
        code = ord(message[c])
        change = code-key
        new = chr(change)
        string += new
        key += key_increment
    decoded = ''.join(string)
    return ('Decoded Message:\t' + decoded)

def add(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = n + result
    return result

def subtract(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = result - n
    return result

def multiply(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = n * result
    return result

def divide(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = result / n
    return result

def remainder(numbers):
    return numbers[0] % numbers[1]

def power(numbers):
    result = numbers[0]
    for n in numbers[1:]:
        result = result ** n
    return result

def wiri():

    chat = True
    print('Hello, I am Wiri. Choose either encrypt, add, subtract, multiply, divide, remainder, or power.')
    print('If using remainder, input only two numbers. For the calculator, input numbers separated by a space or comma.')
    print('If using encrypt please write encrypt then in the next messsage input the text to encrypt.')
    print("To exit the chatbot, please enter 'quit'")
    while chat:
        
        msg = input('Input :\t')
        out_msg = None

        msg = prepare_text(msg)

        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        if not end_chat(msg):
            outs = []
            
            if msg[0] == 'encrypt':
                message = input ('What message do you want to encrypt?')
                outs.append(encryption(message))
            elif msg[0] == 'decrypt':
                message = input ('What message do you want to decrypt?')
                outs.append(decryption(message))
            elif msg[0] == 'add' or msg[0] =='subtract' or msg[0] =='multiply' or msg[0] =='divide' or msg[0] =='remainder' or msg[0] =='power':
                message = input ('What numbers do you want to calculate?')
                outs.append(calculate(prepare_text(message), msg[0]))
            else:
                outs.append("Error please enter one of the options at the beginning of the chat")
                
            out_msg = outs[0]
            
        print('OUTPUT:', out_msg)
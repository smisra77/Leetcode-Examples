#!/usr/local/bin/python3
#pig latin

def string_convert(string):
    print('1')
    output_string = ''
    #len_string = len(input_string)
   # pair = string.split()
    for index,i in enumerate(string.split()):
        first = i[0].lower()

        if first in 'aeiou':
            new_word = i + 'ma'
            output_string += new_word + ' '
        else:
            new_word = i[1:] + first + 'ma' + 'a' * index
            output_string += new_word + ' '

    return output_string

input_string = 'I love latin very much and is awesome'
output = string_convert(input_string)
print('Input: ', input_string)
print('Output: ', output)

        
        
        

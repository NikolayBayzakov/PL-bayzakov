def reverse_string(input_string):
    words = input_string.split()
    reverse_words = words[::-1]
    res = ' '.join(reverse_words)
    return res 


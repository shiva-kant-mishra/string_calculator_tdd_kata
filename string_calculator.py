def add_string(string_numbers):
    if len(string_numbers)==0:
        return 0
    
    else:
        numbers_after_split = string_numbers.split(",")
        result = 0
        for number in numbers_after_split:
            newline_split_number = number.split('\n')
            if len(newline_split_number)>1:
                result += int(newline_split_number[0]) + int(newline_split_number[1])
            else:
                result += int(number)
        return result
def sort(numbers):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if compare_numbers(numbers[i], numbers[j]):
                numbers[i], numbers[j]=numbers[j], numbers[i]
    return numbers

def compare_numbers(num1, num2):
    str_num1=str(num1)
    str_num2=str(num2)
    len_num1=len(str(num1))
    len_num2=len(str(num2))
    min_len=min(len_num1, len_num2)
    for i in range(min_len):
        if str_num1[i]<str_num2[i]:
            return False
        elif str_num1[i]>str_num2[i]:
            return True
    if len_num1>len_num2:
        return compare_numbers(str_num1[min_len:], num2)
    elif len_num2>len_num1:
        return compare_numbers(num1, str_num2[min_len:])
    else:
        return False

numbers=[1, 2, 3, 11, 21, 111, 231]
sorted_numbers=sort(numbers)
print(sorted_numbers)
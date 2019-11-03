def mySum(*num_list):
    output = 0
    for each_num in num_list:
        output += each_num
    return output

# test

res = mySum(1, 2, 3)
print(res)

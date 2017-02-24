#Ergasia 5
#python 2.7.10
harshad_numbers = []
arithmoi = []
for n in range(1, 1001):
    if (n<10):
        harshad_numbers.append(n)
        arithmoi.append(n)
    elif (n<100):
        div = n//10
        mod = n%10
        dsum = div + mod
        dsum_2 = div * mod
        result = n%dsum
        if (result == 0):
            harshad_numbers.append(n)
        if (dsum_2 != 0):
            result_2 = n%dsum_2
            if (result_2 == 0):
                arithmoi.append(n)
    else:
        div = n//10
        mod = n%10
        div_2 = div//10
        mod_2 = div%10
        dsum = div_2 + mod_2 + mod
        dsum_2 = div_2 * mod_2 * mod
        result = n%dsum
        if (result == 0):
            harshad_numbers.append(n)
        if (dsum_2 != 0):
            result_2 = n%dsum_2
            if (result_2 == 0):
                arithmoi.append(n)


print "Oi aritmoi harshad einai: ", harshad_numbers
print "Oi alloi zitoumenoi arithmoi einai: ", arithmoi

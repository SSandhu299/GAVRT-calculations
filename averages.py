first_baseline = []
second_baseline = []

for x in range(5):
    first_baseline.append(float(input(" 1st Baseline? ")))

for x in range(5):
    second_baseline.append(float(input("2nd baseline? ")))

average_of_first = sum(first_baseline)/5
average_of_second = sum(second_baseline)/5

sum_of_both = average_of_first + average_of_second

average_of_both = sum_of_both/2

print( "Your first baseline is:" , average_of_first)

print( "Your second baseline is:", average_of_second)

print ("Your 1st and 2nd baseline average is", average_of_both )
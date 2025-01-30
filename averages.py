# Lists that will fit observations
first_baseline = []
second_baseline = []

# loops five times, asking for a baseline input and putting it into the selected lists
for x in range(5):
    first_baseline.append(float(input(" 1st Baseline? ")))

for x in range(5):
    second_baseline.append(float(input("2nd baseline? ")))

# takes the numbers within the list and finds their average (average =  sum / number of objects - 5 in this case)
average_of_first = sum(first_baseline)/5
average_of_second = sum(second_baseline)/5

# finds the sum of both 
sum_of_both = average_of_first + average_of_second

# finds average of both
average_of_both = sum_of_both/2

#returns average baseline values 
print( "Your first baseline is:" , average_of_first)

print( "Your second baseline is:", average_of_second)

print ("Your 1st and 2nd baseline average is", average_of_both )
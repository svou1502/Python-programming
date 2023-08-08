ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]

length_of_ages = len(ages)
print("The length of the ages list (line by line) are:", length_of_ages)

for age in ages:
    print(age)

for i in range(len(ages)):
    ages[i] = 1 + ages[i]

print("Ages after adding one year are:", ages)

#Part 4
# Create a list to store indices of ages to be removed

indices_to_remove = []  

for i in range(len(ages)):
    if ages[i] < 16 or ages[i] > 65:
        indices_to_remove.append(i)

print("These are all the ages that have been removed:", ages)

# Remove ages at the specified indices in reverse order to avoid index shifting
for index in reversed(indices_to_remove):
    del ages[index]

print("Ages after removing ages outside the range 16-65:", ages)

#Sorting ages

ages.sort()

print("Ages sorted in numerical order are:", ages)
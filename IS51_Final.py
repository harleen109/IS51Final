"""
The program will need to first read the data from the data file named Final.txt to diplay students score from the Final exam

the program will need to count count all the individual grades of all students

the program will need to output the class average from all the students scores

the program will need to output the class average percentage of students who scored above the average which should be 54.17%

count function will output data.split()
average function will output sum(data) / len(data)
above will output count = count + 54.17


"""

"""
file = open (D:\Final.txt, "rt")
data = file.read
count function = data.split 

print('number of grades ', len(function1))

average = []
with open("D:\Final.txt, "rt")
     for line in rt:
         fields = line.split()
         row data = map(str.format, fields)
         average.extend(rowdata)
print(total(average)/len(average))


Function3
test_list = open("D:\Final.txt, "rt")

k = should be 54.17%

print("the list:" +str(test_list))

"""




file = open(r"C:\Users\harle\Desktop\Work\IS51\IS51Final\Final.txt", "r")
count = 0
for line in file :
    parts = line.split()
    count += len(parts)

print("Number of Grades: ", (count))


average = []



with open(r"C:\Users\harle\Desktop\Work\IS51\IS51Final\Final.txt")as f:
     average = [float(line.rstrip()) for line in f]
big = min(average)
small = max(average)
(big - small)
print("Average Grades: ", sum(average)/len(average))



#above = [line.strip() for line in open("D:\Final.txt", 'r') ]

#lcount  = sum(map(lambda x: x > 54.17, above))

#print("percentage above 54.17%", lcount)
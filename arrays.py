# stores a lot of data

#data structures
#lists,set,tuple,dictionary

people =["jack","jane","ahmed","hussein","marriam"]
scores =[87,45,90,52,79,23,66,100]

print (people[0])
print(scores[0])
print(people[-1]) #last value

people.append("willis")
print(people)
scores.append(44)
print(scores)
people.clear()
people.sort()
scores.sort()
print(people)
print(scores)

print(scores[0],scores[-1])
print(sum(scores)/len(scores))
print (scores.count(88))

scores.sort()
#slicing
print(scores)
print(scores[-2:])
print(scores[:3])

print(scores[3:5]) #not inclusive of the last number

# set --to remove duplicates
numbers = {87,89,67,54,87}
print(numbers)

# tuple--immutable data
days =("mon","tue","fri")

# dictionary key amd value
person = {"name":"zillion","city":"marsabit","age":19}
print(person["name"])

# data structures + algorithms
print(sum(numbers))

watu =[{"name":"sila","age":22},
       {"name":"rose","age":21},
       {"name":"manu","age":14}]

print(watu[1]["name"])

# loops -- to print all the names















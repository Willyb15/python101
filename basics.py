# print "Robert Bunch"
print "Will Bryant"
# # Arrays... pysche. Lists.
animals = ['wolf', 'giraffe', 'hippo']
print animals 
# animals = ['wolf','giraffe','hippo']
# # print animals
print animals[0]
# # print animals[0]
print animals[2]

# # How do we push to the array/list? -- APPEND!!
animals.append('croc')
# animals.append("croc")
print animals 

# # What about deleting?
animals.remove('wolf')
# animals.remove("wolf")
print animals 
# # Error!
# animals.prepend("wolf")
# # We can insert at any position with ... insert
animals.insert(0, 'zebra')

animals.insert(0, 'dog')
print animals
# remove via del
del animals[0]
print animals

# # Pop, is just good old Pop
# dc_class = ['Summer', 'Jackson','Danny','Dave','JT','Eric','Paige','Brett','Danielle','Alex','Dan','Shirlette']
# # will sort, but not change the actual array
# # print sorted(dc_class)
# # print dc_class
# # will sort and change the list
# # dc_class.sort()
# # print dc_class
# # will reverse and change teh list - reverse meanign by indicie
# # dc_class.reverse()
# # print dc_class
# # len method, will work like .lenght in JS
# # print len(dc_class)

# # Indentation matters to Python!
# for student in dc_class:
# 	print student

# for i in range(1,10):
# 	print i

# for i in range(1,len(dc_class)):
# 	print i

# # a function is not called a funciton. It's defined by: def
# def sayHello():
# 	print "Hello"

# # will fail because wrong arguments
# # sayHello("Hi")

# def say_hello_with_name(name):
# 	print "Hello, " + name

# say_hello_with_name("Robert")

# # Make squares
# squares = []
# for i in range(1,11):
# 	# Two * is square
# 	square = i**2
# 	# Push that square onto the list
# 	squares.append(square)
# print squares

# # Random list of digits
# digits = [12,235,15,213,42,23,3215,245,342,1234,23,41234231,123,2]
# # Max and min
# print min(digits)
# print max(digits)
# print sum(digits)

# squares = [i**2 for i in range(1,11)]
# print squares

# # Step = the incrament
# print range(1,11,2)

# # slice in python is all about the :
# dc_team = ["Max","Jake","Rob","Toby","Natalie"]
# team_part = dc_team[1:3]
# print team_part
# team_part = dc_team[1:-1]
# print team_part
# team_part = dc_team[:1]
# print team_part
# team_part = dc_team[2:]
# print team_part
# # Will keep a connection so both will change when one does
# team_copy = dc_team
# print team_copy
# print dc_team
# # make a new list, independent.
# team_copy = list(dc_team)
# team_copy.append("DeAnn")
# print team_copy
# print dc_team

# team_copy = dc_team[:]
# team_copy.append("DeAnn")
# print team_copy
# print dc_team





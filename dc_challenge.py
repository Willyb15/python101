# 1) Declare two variables, a string and an integer 
# named "fullName" and "age". Set them equal to your name and age.

# Python is dynamic, so we don't need a var. Just make them
full_name = "Robert Bunch"
age = 38

# 2) Declare an empty array called "myArray". 
# Add the variables from #1 (fullName and age) to the empty array using the push method.
# Print to the console.

# No such thing as push, but who cards, there's no such thing as an array. 
# There are lists. And lists have: Append
my_list = []
my_list.append(full_name)
my_list.append(age)
print my_list

# 3) Write a simple function that takes no parameters called "sayHello". 
# Make it print "Hello!" to the console when called.
# Call the function.

def say_hello():
	print "Hello"
say_hello()


# 4) Declare a variable named splitName and set it equal to
# fullName split into two seperate objects in an array.
# (In other words, if the variable fullName is equal to "John Smith", then splitName should 
# equal ["John", "Smith"].)
# Print splitName to the console.
# HINT: Remember to research the methods and concepts listed in the instructions PDF.

# Easy Peasy...
split_name = full_name.split()
print split_name


# 5) Write another simple function that takes no parameters called "sayName".
# When called, this function should print "Hello, ____!" to the console, where the blank is 
# equal to the first value in the splitName array from #4.
# Call th

def say_name():
	# print "Hello, %r" % split_name[0]
	string = "Hello, {}. Welcome to {}"
	print string.format(split_name[0],'DigitalCrafts')
say_name()


# 6) Write another function named myAge.  This function should take one parameter: the year you 
# were born, and it should print the implied age to the console.
# Call the function, passing the year you were born as the argument/parameter.
# HINT: http://www.w3schools.com/js/js_functions.asp
import datetime
def my_age(birth_year):
	# now = datetime.datetime.now()
	# print now.year - birth_year
	print 2016 - birth_year
my_age(1921)


# 7) Using the basic function given below, add code so that sum_odd_numbers will print to the console the sum of all the odd numbers from 1 to 5000.  Don't forget to call the function!
# HINT: Consider using a 'for loop'.
def sum_odd_numbers():
	sum = 0
	for i in range(1,5000):
		if (i % 2 == 1):
			sum += i
	print sum
sum_odd_numbers()
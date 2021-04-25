# Code for concatenating 2 tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'learning')

# Concatenating above two
print(tuple1 + tuple2)

# Code for creating nested tuples

tuple1 = (0, 1, 2, 3)
tuple2 = ('python', 'learner')
tuple3 = (tuple1, tuple2)
print(tuple3)

# code to test slicing

tuple1 = (0 ,1, 2, 3)
print(tuple1[1:])
print(tuple1[::-1])
print(tuple1[2:4])
# Code for printing the length of a tuple

tuple2 = ('python', 'geek')
print(len(tuple2))
#python code for creating tuples in a loop

tup = ('geek',)
n = 5 #Number of time loop runs
for i in range(int(n)):
	tup = (tup,)
	print(tup)

"""
Stacks
    - a data structure that stores and retrieves items in a "last in first out" (LIFO)

2 operations 
pop && push
push
    - allows us to store a value on to the Stack
pop
    - it allows us to retrieve and removes a value from the stack
stack = []
"""

#push
stack.append(5) # equivalent to push(5), if push() another element it will be in index++
stack.append(10)
stack.append(25)
print(stack)
#bottom is the last element, top is the index++ as a there is an element in the previous index
stack.pop() #removes the previous index from top, no value inside pop()
print(stack)
stack.pop()
print(stack)

"""
other operations
isFull
	- a boolean operation needed for static stacks. Return true if the stack is full. Otherwise returns false.
isEmpty
	- a boolean operation needed for all stacks. Rerturns true if the stack is empty, Otherwise return false.
"""

class StaticStack:
	def __init__(self, capacity):
		self.stack = []
		self.capacity = capacity

	def isFull(self):
		#check the length of the stack to be equal to the predefined capacity 
		return len(self.stack) == self.capacity

#create a stack with a capacity of 5
stack = StaticStack(5)
stack.stack = [1, 2, 3, 4]

#boolean result
print(stack.isFull())

3 + (4*5) -> postfix 3 4 5 * +

"""
Static Stack
	- fixed size
	- can be implemented with an array
Dynamic Stack 
	- linklist
	- grow in size
	- can be implemented with linked list
		-- no need to specify the starting size of the stack.
			-- simply starts as an empty linked list and expands by one node each time a value is pushed
			-- will never be full as long as the system has enough memory
"""

"""
	Create a task manager python program with basic functionalities:
		(classes, methods, lists, loops, input-handling in python)
		- add tasks with a title and description
		- mark tasks as completed
		- display the list of tasks along with status
		- exit option to exit the manager
	push in your gitHub acount and paste the URL in our SB
		bcs21-stack-activity-caustria.py
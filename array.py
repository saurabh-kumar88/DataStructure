# Excercise on Array:

monthly_expences = [2200, 2350, 2600, 2130, 2190]
heros=['spider man','thor','hulk','iron man','captain america']

def createList():
	maxNumber = input("\n Enter a maximum integer number to create a list : ")
	
	try:
		number = int(maxNumber)
	except ValueError as err:
		print("\n  Error : you have entered ", maxNumber,  " which is not a integer !")
		exit()
	
	List = []
	for x in range(1, number):
		if (x % 2) == 0:
			pass
		else:
			List.append(x)
	return List
		
	

	


if __name__ == '__main__':
	# 1. In Feb, how many dollars you spent extra compare to January?
	print("\n extra expence in feb compare to Jan : ", monthly_expences[1] - monthly_expences[0])
	# 2. Find out your total expense in first quarter (first three months) of the year.
	print("\n Total expence of first quarter : ", monthly_expences[0] + monthly_expences[1] + monthly_expences[2])
	# 3. Find out if you spent exactly 2000 dollars in any month
	for x in range(len(monthly_expences)):
		if monthly_expences[x] == 2000:
			print("\n expence of 2000 dollar in ", x, " month")

	# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
	monthly_expences.append(1980)
	print(monthly_expences)

	#5. You returned an item that you bought in a month of April and
	#got a refund of 200$. Make a correction to your monthly expense list based on this.

	refund = monthly_expences[2] - 200
	monthly_expences.remove(monthly_expences[2])
	monthly_expences.insert(2, refund)
	print("\n After refund : ", monthly_expences)

	# 1. Length of the list
	print("\n Length of the list : ", len(heros))
	
	# 2. Add 'black panther' at the end of this list
	heros.append('black panther')
	print(heros)

	# 3. You realize that you need to add 'black panther' after 'hulk',
    # so remove it from the list first and then add it after 'hulk'
	
	heros.insert(5, 'hulk')
	print("\n : ", heros)

	# 4. Now you don't like thor and hulk because they get angry easily :)
    # So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
    # Do that with one line of code.
	heros[1:3] = ['doctor strange']
	print("\n Converted : ", heros)
	
	# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
	heros.sort()
	print("\n Sorted : ", heros)

	# Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function


	List = createList()
	print("\n List : ", List)
	
	

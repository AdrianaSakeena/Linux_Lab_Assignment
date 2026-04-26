import sys #import the sys library to use input from the command line

shift = int(sys.argv[1]) #use the shift specified by the user in the command line to encrypt the text
output ="" #the new message after encryption will be stored here

for input in sys.stdin:
	input = input.upper() #uppercase the input so ASCII form can be used
	
	for character in input:
		if character >= "A" and character <= "Z":
			val = ord(character) #converting the letter into ASCII form
 

			val = val +shift

			if val > ord("Z"):
				val = val -26 #so that the letters do not go beyond Z!
			output  = output +chr(val) #converting to character form and saving as output

i = 0
for character in output:
	print(character, end="")
	i = i+1
	#printing out output
	
	if i%5 == 0:
		print(" ", end="")

	if i%50 == 0:
		print() #create a new line so there are ten blocks per line


__author__ = 'Andrew'
# Tested using 3.x python

# User Input, in 3.x "input" is used, in 2.x "raw_input" is used.
# Set up input strings and initialize my int to 0 for loop
h = 0   # h is our integer for the height
l = 0   # l is our integer for the length
w = 0   # w is our integer for the width

box_count = 0       # Sets the count to 0
box_countmax = 4    # Sets the max to 4

# Create lists to store the relevant data
list1 = []
list2 = []
list3 = []

while box_count < box_countmax:                                 # For kicks, this lets us control the max condintional in case the value needs to be different than "4"
    box_count =  box_count + 1                                  # Conditional Loop incrementor, also used to display which box we are working on
    while (h == 0):                                             # Set up loop to prompt user to enter a valid number, 0 used since dimensions must exist.
        try:                                                    # If the user does not give a number we want to give them another chance
            print("Box ", box_count)                            # Gives us which box this is at the start of each loop
            boxHeight = input("Enter the Box Height: ")         # Takes user input from keyboard after prompt
            ht = float(boxHeight)                               # Turns our input string into a float number
            list1.append(ht)                                    # Appends into the list, stores each value separately
            break                                               # Stop error and go to except block instead if input is incorrect
        # This is our exception block
        except ValueError:
            # Print a friendly message and try again
            print("Sorry! You need to use only a number here. Please try again. ")
    # Repeated for Length and Width sections, nothing new to explain.
    while l == 0:
        try:
            boxLength = input("Enter the Box Length: ")
            lt = float(boxLength)
            list2.append(lt)
            break
        except ValueError:
            print("Sorry! You need to use only a number here. Please try again.")
    while w == 0:
        try:
            boxWidth = input("Enter the Box Width: ")
            wt = float(boxWidth)
            list3.append(wt)
            break
        except ValueError:
            print("Sorry! You need to use only a number here. Please try again.")




# Formula  length x width x height, using simple shorthand we calculate the final result, float allows for decimals.
# Each box is given a total value utilizing the lists.
boxVolume1 = float(list1[0]*list2[0]*list3[0])
boxVolume2 = float(list1[1]*list2[1]*list3[1])
boxVolume3 = float(list1[2]*list2[2]*list3[2])
boxVolume4 = float(list1[3]*list2[3]*list3[3])

# List display of each volume total
boxes = [boxVolume1, boxVolume2, boxVolume3, boxVolume4]
# Combining the totals for a complete total
totalofboxes = boxVolume1+boxVolume2+boxVolume3+boxVolume4

i = 1           # shorthand variable, used in many examples
while i < 5:    # Set our simple conditional
    print("Volume of Box ", i, "Height: ", list1[i-1], "Length: ", list2[i-1], "Width: ", list3[i-1])   # outputs dimensions
    print("Total volume of box ", i, "is ", boxes[i-1])                                                 # outputs total
    print("")                                                                                           # Easy newline method, keeps the output nicer to view
    i = i + 1                                                                                           # Increment i at the end of the loop

# We now display the value to show the calculation worked as expected.
print("Total volume of all boxes is: ", boxes, "or combined: ", totalofboxes)       # List and combination of volume
print("Volume of box 3 is: ", boxes[2])                                             # Asked for box 3 total volume

# End
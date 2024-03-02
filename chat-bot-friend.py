#Meet my Chatbot Friend Starter Code

#chatbot introduces themself
print("Hello! I'm Gabby the chatbot.")
# asign user input to our variable name
name = input("What's your name? ")
# use the print method to see output in the console.
print("Let's see if I can spell that:")

#Add Part 5 code here
# asign the list method and name input to variable name_list
name_list = list(name)
#now print that variable to see the name_list variable output in the console
print(name_list)

# create a for loop that iterates over each letter in our string and prints out those 'letters' to the console
for letter in name_list:
  print(letter)
# using the print method again to reuse the name variable again thats useful
print("Nice to meet you " + name)

#chatbot asks questions

# what method are we using here to 'print' to the console? what will we see? //
print("Can you tell me about yourself?")

#add Part 2 Step 2 code in this section
print("Where are you from?")
place = input("You are from... ")
print("I'd love to visit " + place + " one day!")

print("What are you passionate about?")
passion = input("You are passionate about... ")
print("Whoa, that's amazing! " + passion + " is so cool! :o")

print("What is your personal goal?")
goal = input("You hope to... ")
print("I really admire your goal to " + goal + ". I know you can do it! :D")

#chatbot tells their story
#add Part 4 code here
while True:
  topic = input("What would you like to know about me? - home, passion, goal, or none? ")

  #add Part 3 code here
  if topic.lower() == "home":
    print("I come from a chilly planet far away! :D")

  elif topic.lower() == "passion":
    print("I LOVE learning all kinds of things! *_*")

  elif topic.lower() == "goal":
    print("I hope to help people through coding! :)")

  elif topic.lower() == "none":
    print("Oh, okay! ^_^ ")
    break;
    
  else:
    print("Sorry, I didn't catch that. ")


print("Thanks for chatting with me! See you soon!")



#add triangle https://www.geeksforgeeks.org/programs-printing-pyramid-patterns-python/
# Function to demonstrate printing pattern triangle
def pryamid(numberOfSpaces):
     
    # number of spaces
    k = numberOfSpaces - 1
 
    # outer loop to handle number of rows
    for i in range(0, numberOfSpaces):
     
        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, k):
            print(end=" ")
     
        # decrementing k after each loop
        k = k - 1
     
        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0, i+1):
         
            # printing stars
            print("* ", end="")
     
        # ending line after each row
        print("\r")
 
# Driver Code
numberOfSpaces = 5
pryamid(numberOfSpaces)



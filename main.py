# Omar Diaa Abdelhaleem Abdullat
# Computer Science 30
# October 22, 2021
# RPG Simple menu
print("Welcome to Omar's very own game")
print('''Hello, welcome to my game, let's get started by completing one of the
following actions: Go hunting, Go fishing, Go swimming, Go sleep, or Quit.''')
while True:
 choice = input("Action:")
# The first choice starts here.
 if choice == "Go Hunting":
   print("You go hunting and you managed to hunt 2 deer.")
   (hunting) = input("Do you want to keep hunting or prepare the food: ")
   if hunting == "Keep Hunting":
    print("you we hunting again and managed to get another 3")
   elif hunting == "Prepare The Food":
    print("You prepared a nice meal with the deer you hunted.")
   elif choice == "Quit":
    print("Goodbye.")
    break
   else:
    print("Please input a valid answer.")
# The second choice starts here.
 elif choice == "Go Fishing":
   print("You go fishing and managed to get 3 fishes and some crabs.")
   (fishing) = input("Do you want to keep fishing or prepare the food: ")
   if fishing == "Keep Fishing":
    print("You went fishing and found a lobster.")
   elif fishing == "Prepare The Food":
    print("you prepared a Delicious meal with your fishes and crab.")
   elif choice == "Quit":
    print("Goodbye.")
    break
   else:
    print("Please input a valid answer.")
# The Third choice starts here.
 elif choice == "Go swimming":
   print("you go swimming and you were almost eaten by a shark.")
   swimming = input("Do you want to go back and swim or do you stop: ")
   if swimming == "Go Back And Swim":
    print("You go back swimming, luckily the shark went away.")
   elif swimming == "You Stop":
    print("You stopped swimming and you went back to your shleter.")
   elif choice == "Quit":
    print("Goodbye.")
    break
   else:
    print("Please input a valid answer.")
# The last choice starts here.
 elif choice == "Go Sleep":
   print("You go to sleep and wake up in the middle of the night.")
   sleeping = input("Do you want to go back to sleep or stay awake: ")
   if sleeping == "Go Back To Sleep":
     print("You went back to sleep.")
   elif sleeping == "Stay Awake":
     print("you stay awake.")
   elif choice == "Quit":
     print("Goodbye.")
     break
   else:
     print("Please input a valid answer.")
# Quit function.
 elif choice == "Quit":
   print("Goodbye.")
   break
# Invalid answer function.
 else:
   print("Please input a valid answer.")
# The End.

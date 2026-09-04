print("===================")
print("Hello")
print("===================")

username = input("Enter your username: ")
bio = "i'm a crumb"
followers = 100
age = input("Enter your age: ")
category = input("Enter your category: ")

print("\nInstagram Profile")
print("===================")
print ("Username: ", username)
print("Age: ", age)
print("Category: ", category)
print ("Bio: ", bio)
print ("Followers: ", followers)

followers += 50
print("Day 1:", followers)

followers += 20
print ("Day 2:", followers)

followers -= 10
print ("Day 3:", followers)

if age>60 and category=="Lifestyle":
    print("You are a senior lifestyle influencer!")

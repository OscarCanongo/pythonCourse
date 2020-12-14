the_count = [1,2,3,4,6]
stocks = ["AAPL", "GOOG", "TSLA"]
random_things = ["Puppies", 55, "Anthony Weiner", 1/2, ["Oh no", "A list inside a list"]]

#This for-loop goes through a list
for number in the_count:
    print("this is count", number)

#Same as above
for stock in stocks:
    print("Stock ticker:", stock)

#We can go through mixed lists too
# I called it i (short for item) since I don't know waht's in it
for i in random_things:
    print("Here is a random thing:", i)

# we can alse build lists, first let's start with a empty one
people = []

people.append("Oscar")
people.append("Oscar II")
people.append("Oscar III")

# now we can print them out too
print(people)

# and remove some
people.remove("Oscar II")
print(people)

for person in people:
    print("Person is:", person)


# Challenge print out the square of the numbers 1 to 10
for x in range(1,11):
  print("The square of ", x, "is", x*x)

# Here's how you acces elements of a list
animals = ["bear", "tiger", "penguin", "zebra"]
first_animal = animals[0]
print(first_animal)
third_animal = animals[2]
print(third_animal)

print("The are this many things:", len(random_things))
print("things is a:", type(random_things))

another_list = random_things[-1]
print(another_list)
print(type(another_list))
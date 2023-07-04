class cat:
    species = "mammal"
    def __init__(self, name , age):
        self.name = name
        self.age = age

    

cat1 = cat("Tom", 8)
cat2 = cat("Jerry", 5)
cat3 = cat("Dan", 10)

def OldestCat(*args):
        return max(args)

print(f"The oldest cat is {OldestCat(cat1.age, cat2.age, cat3.age)} years old. ")

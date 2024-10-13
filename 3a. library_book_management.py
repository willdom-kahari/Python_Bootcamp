# 1. Variables for book genres with quantity
fiction = 120
non_fiction = 80
science = 60
history = 40

# 2. Total number of books in the inventory
total_books = fiction + non_fiction + science + history

# 3. Add 10 more fiction books to the inventory
fiction += 10
total_books += 10

# 4. Is number of science books less than or equal to 50
is_less_or_equal_to_50 = science <= 50

# 5. Print inventory items
print("Fiction:", fiction)
print("Nonfiction:", non_fiction)
print("Science:", science)
print("History:", history)

print("Total number of books in the inventory:", total_books)
print("Science books are less or equal to 50:", is_less_or_equal_to_50)


from enum import Enum
import random

# Define an Enum to represent different flavors of chocolate, each with unique attributes.
class ChocolateFlavor(Enum):
    ALMOND = "Almond"
    PEANUT_BUTTER = "Peanut butter"
    MILK_CHOCOLATE = "Milk chocolate"
    WHITE_CHOCOLATE = "White chocolate"
    DARK_CHOCOLATE = "Dark chocolate"

# Define a class to represent a Chocolate, including its weight, price, flavor, and ID.
class Chocolate:
    def __init__(self, weight, price, flavor, id):
        self.weight = weight
        self.price = price
        self.flavor = flavor  # Uses the ChocolateFlavor Enum
        self.id = id

# Define a class to represent a Student, identified by an ID.
class Student:
    def __init__(self, id):
        self.id = id
        self.chocolate = None

# Function to generate chocolates for students based on the number of students.
def generate_chocolates_for_students(n):
    chocolates = []
    flavors = list(ChocolateFlavor)  # Convert ChocolateFlavor Enum to a list
    for i in range(n):
        flavor = flavors[i % len(flavors)]  # Cycle through flavors
        id = f"{i+1:03d}" #tjhs line formats the integer variable 'i' as a 3-digit string
        weight = round(random.uniform(1, 10)) # Random weight from 1 to 10, rounded to 1 decimal place
        price = round(random.uniform(1, 20)) # Random price from 1 to 10, rounded to 1 decimal place
        # Create a Chocolate instance with attributes based on the flavor
        chocolate = Chocolate(weight, price, flavor, id)
        chocolates.append(chocolate)  # Add the chocolate to the list
    return chocolates

def distribute_chocolates_iteratively(chocolates, students):
    distribution = {}  # Initialize an empty dictionary for distribution
    for student, chocolate in zip(students, chocolates):  # Pair each student with a chocolate
        # Assign the chocolate ID and flavor name to the corresponding student ID in the distribution dictionary
        distribution[student.id] = (chocolate.id, chocolate.flavor.name, chocolate.weight, chocolate.price)
        student.chocolate = chocolate
    return distribution  # Return the distribution dictionary

# Function to distribute chocolates to students iteratively.
def distribute_chocolates_recursively(chocolates, students, distribution=None, index=0):
    if distribution is None:
        distribution = {}  # Initialize distribution if not provided
    if index < len(students):  # Base case: check if there are more students
        student = students[index]  # Get the current student based on index
        chocolate = chocolates[index]  # Get the corresponding chocolate
        # Assign the chocolate ID and flavor name to the student in the distribution
        distribution[student.id] = (chocolate.id, chocolate.flavor.name, chocolate.weight, chocolate.price)
        student.chocolate = chocolate
        # Recursive call to distribute the next chocolate to the next student
        return distribute_chocolates_recursively(chocolates, students, distribution, index + 1)
    return distribution  # Return the completed distribution dictionary once all students have been assigned a chocolate


# Sorting the chocolates using merge sort algorithm based on a specific attribute

def merge_sort(chocolates, attribute):
    # If there is more than one chocolate, divide the list into two halves
    if len(chocolates) > 1:
        mid = len(chocolates) // 2
        L = chocolates[:mid]  # Left half
        R = chocolates[mid:]  # Right half

        # Recursively sort the left and right halves
        merge_sort(L, attribute)
        merge_sort(R, attribute)

        i = j = k = 0  # Initialize variables for merging
        while i < len(L) and j < len(R):
            # Compare the attribute of chocolates from the left and right halves
            if getattr(L[i], attribute) < getattr(R[j], attribute):
                chocolates[k] = L[i]
                i += 1
            else:
                chocolates[k] = R[j]
                j += 1
            k += 1

        # Check for remaining elements in the left half
        while i < len(L):
            chocolates[k] = L[i]
            i += 1
            k += 1

        # Check for remaining elements in the right half
        while j < len(R):
            chocolates[k] = R[j]
            j += 1
            k += 1


# Define a binary search function to find a student holding a chocolate with a specified attribute (price or weight).
def binary_search_students(students, target, attribute):
    left = 0
    right = len(students) - 1

    while left <= right:
        mid = (left + right) // 2
        # Access the attribute of the chocolate object, not the Student object
        current_attribute = getattr(students[mid].chocolate, attribute)

        if current_attribute == target:
            return students[mid]  # Return the found student
        elif current_attribute < target:
            left = mid + 1
        else:
            right = mid - 1

    return None  # Return None if the target is not found



# Example usage
# Example usage
n = 50  # Number of students

if n <= 0:
    print("No student available.")
else:
    # Initialize students and other operations here
    students = [Student(f"Student{i}") for i in range(1, n + 1)]
    chocolates = generate_chocolates_for_students(len(students))

    # Distribute chocolates iteratively and recursively
    distribution_iterative = distribute_chocolates_iteratively(chocolates, students)
    distribution_recursive = distribute_chocolates_recursively(chocolates, students)

    print("Iterative Distribution:")
    for student_id, (chocolate_id, flavor, weight, price) in distribution_iterative.items():
        print(f"Student: {student_id}, Chocolate ID: {chocolate_id}, Flavor: {flavor}, Weight: {weight} gm, Price: {price} AED")

    print("\nRecursive Distribution:")
    for student_id, (chocolate_id, flavor, weight, price) in distribution_recursive.items():
        print(f"Student: {student_id}, Chocolate ID: {chocolate_id}, Flavor: {flavor}, Weight: {weight} gm, Price: {price} AED")


    # Sort chocolates by weight
    chocolates_by_weight = chocolates.copy()
    merge_sort(chocolates_by_weight, 'weight')
    print("\nChocolates sorted by weight:")
    for chocolate in chocolates_by_weight:
        print(f"Flavor: {chocolate.flavor.name}, Weight: {chocolate.weight} gm")

    # Sort chocolates by price
    chocolates_by_price = chocolates.copy()
    merge_sort(chocolates_by_price, 'price')
    print("\nChocolates sorted by price:")
    for chocolate in chocolates_by_price:
        print(f"Flavor: {chocolate.flavor.name},  Price: {chocolate.price} aed")

        """binary APPORACH"""
        # Assuming ChocolateFlavor, Chocolate, and Student classes are defined as provided earlier.
        # Loop through the list of students and assign each a chocolate from the chocolates list.
    # Assigning chocolates to students
    for i in range(len(students)):
        students[i].chocolate = chocolates[i]

    # Defining target values and attributes for search
    target_price = 11  # The target price you're searching for
    attribute_price = 'price'  # Searching by 'price'

    target_weight = 8  # The target weight you're searching for
    attribute_weight = 'weight'  # Searching by 'weight'

    # Performing binary search for price and weight
    found_student_price = binary_search_students(students, target_price, attribute_price)
    found_student_weight = binary_search_students(students, target_weight, attribute_weight)

    # Printing results
    print("\n")
    if found_student_price:
        print(f"Found a student holding a chocolate with {attribute_price}: {target_price} AED:")
        print(f"Student: {found_student_price.id}, Chocolate ID: {found_student_price.chocolate.id}, "
              f"Flavor: {found_student_price.chocolate.flavor.name}, Price: {found_student_price.chocolate.price} AED")
    else:
        print(f"No student found holding a chocolate with {attribute_price} {target_price} AED.")

    if found_student_weight:
        print(f"Found a student holding a chocolate with {attribute_weight}: {target_weight} gm:")
        print(f"Student: {found_student_weight.id}, Chocolate ID: {found_student_weight.chocolate.id}, "
              f"Flavor: {found_student_weight.chocolate.flavor.name}, Weight: {found_student_weight.chocolate.weight} gm")
    else:
        print(f"No student found holding a chocolate with {attribute_weight} {target_weight} gm.")









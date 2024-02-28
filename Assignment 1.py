from enum import Enum #for enum
import random  #for random

# Define an Enum to represent different flavors of chocolate, each with unique attributes.
class ChocolateFlavor(Enum):
    ALMOND = "Almond"
    PEANUT_BUTTER = "Peanut butter"
    MILK_CHOCOLATE = "Milk chocolate"
    WHITE_CHOCOLATE = "White chocolate"
    DARK_CHOCOLATE = "Dark chocolate"

# Define a class to represent a Chocolate, including its weight, price, flavor, and ID.
class Chocolate:
""" class represnts chocloate"""
    def __init__(self, weight, price, flavor, id):
        self.weight = weight
        self.price = price
        self.flavor = flavor  # Uses the ChocolateFlavor Enum
        self.id = id

# Define a class to represent a Student, identified by an ID.
class Student:
    "class represent students"
    def __init__(self, id): #constructer used to  to initialize the attributes of the class.
        self.id = id
        self.chocolate = None # Initialize the chocolate attribute as None

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

# Assuming ChocolateFlavor, Chocolate, and Student classes are defined as provided earlier.
# Define a binary search function to find a student holding a chocolate with a specified attribute (price or weight).
def binary_search_students(students, target, attribute):
    left = 0 # Set the left and right pointers for binary search
    right = len(students) - 1
    # Perform binary search while the left pointer is less than or equal to the right pointer
    while left <= right:
        mid = (left + right) // 2 # Calculate the middle index
        # Access the attribute of the chocolate object, not the Student object
        current_attribute = getattr(students[mid].chocolate, attribute)

        if current_attribute == target: # Check if the current attribute matches the target
            return students[mid]  # Return the found student
        elif current_attribute < target:
            left = mid + 1 # Adjust the left pointer if the current attribute is less than the target
        else:
            right = mid - 1 # Adjust the right pointer if the current attribute is greater than the target

    return None  # Return None if the target is not found









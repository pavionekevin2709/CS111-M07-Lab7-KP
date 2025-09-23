#CS111 - M07 Lab7
#Lists and Tuples
#Author: Kevin Pavione
#Date: September 23, 2025

#Programming Assignment 6: Packing List Organizer

# Import necessary modules
import random

# Initialize empty list for packing items and tuple for packed items
packing_list = []
packed_items = ()

# Predefined lists for trip type suggestions
trip_suggestions = {
    "beach": ["sunscreen", "swimsuit", "towel", "sunglasses", "flip-flops"],
    "hiking": ["hiking boots", "water bottle", "backpack", "map", "compass"],
    "business": ["laptop", "business cards", "suit", "notebook", "pen"]
}

# Function to display the current packing list and packed items
def display_lists():
    print("\nCurrent Packing List (Unpacked):")
    if packing_list:
        for i, item in enumerate(packing_list, 1):
            print(f"{i}. {item}")
    else:
        print("No items in packing list.")
    
    print("\nPacked Items:")
    if packed_items:
        for i, item in enumerate(packed_items, 1):
            print(f"{i}. {item}")
    else:
        print("No items packed yet.")

# Function to add an item to the packing list
def add_item(item):
    packing_list.append(item)
    print(f"\n{item} added to packing list.")

# Function to remove an item from the packing list
def remove_item(item):
    if item in packing_list:
        packing_list.remove(item)
        print(f"\n{item} removed from packing list.")
    else:
        print(f"\n{item} not found in packing list.")

# Function to mark an item as packed (move from list to tuple)
def mark_packed(item):
    global packed_items
    if item in packing_list:
        packing_list.remove(item)
        packed_items = packed_items + (item,)
        print(f"\n{item} marked as packed.")
    else:
        print(f"\n{item} not found in packing list.")

# Function to suggest items based on trip type
def suggest_items(trip_type):
    trip_type = trip_type.lower()
    if trip_type in trip_suggestions:
        suggestions = trip_suggestions[trip_type]
        print(f"\nSuggested items for {trip_type} trip:")
        for item in suggestions:
            print(f"- {item}")
        # Add a random suggested item to packing list
        random_item = random.choice(suggestions)
        if random_item not in packing_list:
            add_item(random_item)
    else:
        print("\nInvalid trip type. Choose: beach, hiking, or business")

# Main program loop
def main():
    while True:
        print("\n=== Packing List Organizer ===")
        print("1. Add item")
        print("2. Remove item")
        print("3. View lists")
        print("4. Mark item as packed")
        print("5. Suggest items for trip")
        print("6. Exit")
        
        choice = input("\nEnter your choice (1-6): ")
        
        if choice == "1":
            item = input("Enter item to add: ")
            add_item(item)
        
        elif choice == "2":
            item = input("Enter item to remove: ")
            remove_item(item)
        
        elif choice == "3":
            display_lists()
        
        elif choice == "4":
            item = input("Enter item to mark as packed: ")
            mark_packed(item)
        
        elif choice == "5":
            trip_type = input("Enter trip type (beach, hiking, business): ")
            suggest_items(trip_type)
        
        elif choice == "6":
            print("\nGoodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()
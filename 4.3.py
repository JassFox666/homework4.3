import random

def generate_and_select_elements():
    random_list = [random.randint(1, 100) for _ in range(random.randint(3, 10))]
    selected_elements = [random_list[0], random_list[2], random_list[-2]]
    return random_list, selected_elements


original_list, new_list = generate_and_select_elements()
print(f"Original list: {original_list}")
print(f"New list: {new_list}")
def calculate_max_height(initial_velocity):
    acceleration_due_to_gravity = 32.2  # feet per second squared
    max_height = (initial_velocity ** 2) / (2 * acceleration_due_to_gravity)
    return max_height

# Main code
initial_velocity = 20  # feet per second
max_height = calculate_max_height(initial_velocity)
print(f"The maximum height of the ball is {max_height} feet.")

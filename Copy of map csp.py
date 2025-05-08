from constraint import Problem

# Create a CSP problem instance
problem = Problem()

# Define regions on the map
regions = ["A", "B", "C", "D", "E"]

# Define available colors
colors = ["Red", "Green", "Blue"]

# Add variables (each region can take any of the colors)
for region in regions:
    problem.addVariable(region, colors)

# Define adjacency constraints (neighboring regions should not have the same color)
adjacent_regions = [("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "E")]

for region1, region2 in adjacent_regions:
    problem.addConstraint(lambda c1, c2: c1 != c2, (region1, region2))

# Solve the CSP
solutions = problem.getSolutions()

# Print all possible solutions
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}: {solution}")

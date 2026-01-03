import random
import matplotlib.pyplot as plt

# Data
values = [10, 7, 12, 8, 15]     
weights = [2, 3, 4, 5, 7]       
capacity = 12               
num_items = len(values)

# Fitness function
def fitness(chrom):
    total_weight = 0
    total_value = 0
    for i in range(len(chrom)):
        total_weight += weights[i] * chrom[i]
        total_value += values[i] * chrom[i]
    if total_weight == 0 or total_weight > capacity:
        return 0
    return total_value / total_weight

# Create random chromosome
def create_chromosome():
    return [random.randint(0, 1) for _ in range(num_items)]

# Initialize population
population = [create_chromosome() for _ in range(4)]

# Calculate initial fitness
initial_fitness = [fitness(ch) for ch in population]
total_initial_fitness = sum(initial_fitness)


print("Initial Population and Fitness:")
print("Initial Population and Fitness:")
i = 1  # start counter
for ch in population:
    print(f"Ch {i}: {ch}, Fitness: {fitness(ch):.2f}")
    i += 1  # increment counter

print(f"total_initial_fitness: {total_initial_fitness:.2f}")

# Single-point crossover
def crossover(p1, p2):
    point = random.randint(1, num_items - 1)
    child1 = p1[:point] + p2[point:]
    child2 = p2[:point] + p1[point:]
    return child1, child2  

# Apply crossover
child1, child2 = crossover(population[0], population[1])  
child3, child4 = crossover(population[2], population[3]) 

children = [child1, child2, child3, child4]

# Mutation: flip 3rd bit
def mutate(ch):
    ch[2] = 1 - ch[2] 
    return ch

mutated_children = [mutate(ch.copy()) for ch in children]

# Calculate current fitness
current_fitness = [fitness(ch) for ch in mutated_children]
total_current_fitness = sum(current_fitness)

print("\nAfter Mutation:")
i = 1  # start counter
for ch in mutated_children:
    print(f"Mutated Child {i}: {ch}, Fitness: {fitness(ch):.2f}")
    i += 1


plt.figure(figsize=(6,5))
plt.bar(["Initial Fitness", "Current Fitness"], [total_initial_fitness, total_current_fitness], color=["brown","orange"])
plt.ylabel("Total Fitness")
plt.show()

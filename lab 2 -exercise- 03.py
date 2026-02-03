
total_soda = int(input('How many sodas do you have?')

fridge_cubes = total_sodas // 24
remaining_after_cubes = total_sodas % 24

six_packs = remaining_after_cubes // 6
singles = remaining_after_cubes % 6

print(f"Fridge Cubes: {fridge_cubes}")
print(f"Six-packs: {six_packs}")
print(f"Singles: {singles}")

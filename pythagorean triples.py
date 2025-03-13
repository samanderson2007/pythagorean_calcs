def find_pythagorean_triples(limit):
    triples = []
    for a in range(1, limit + 1):
        for b in range(a, limit + 1):  
            c_squared = a**2 + b**2
            c = int(c_squared ** 0.5)
            if c**2 == c_squared and c <= limit:
                a_squared = a**2
                b_squared = b**2
                c_squared = c**2
                triples.append((a, b, c, "The values are", a_squared, b_squared, c_squared))
    return triples


limit = int(input("Enter a limit: "))
triples = find_pythagorean_triples(limit)

print("All triples in the limit given are: ")
for triple in triples:
   print(triple)

print(f"Total Pythagorean triples found: {len(triples)}")

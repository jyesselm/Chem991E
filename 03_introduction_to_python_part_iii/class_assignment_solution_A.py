amino_acid_string = input("Enter your amino acid sequence: ")
amino_acid_count = {}
for amino_acid in amino_acid_string:
    if not amino_acid in amino_acid_count:
        amino_acid_count[amino_acid] = 0
    amino_acid_count[amino_acid] += 1
print(amino_acid_count)
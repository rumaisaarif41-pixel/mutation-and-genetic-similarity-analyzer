"""
This script analyzes Mutations and Genetic similarity between two DNA strings.
Author:[Rumaisa Arif]
"""
# DNA sequences to compare
dna_a='ATGC'
dna_b='ATAC'
mutations=0
# Comparison loop
for i in range(4):
    base1=dna_a[i]
    base2=dna_b[i]
    if base1 != base2:
        print('Mutation found in locker:'+str(i+1))
# Calculate Similarity
dna_length=4
mutations=1
matches=dna_length-mutations
percentage=matches/dna_length*100
print(('Similarity:')+str(percentage)+'%')
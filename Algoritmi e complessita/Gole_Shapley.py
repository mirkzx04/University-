A = {
   'a_1': ['b_3', 'b_2', 'b_4', 'b_1'],
    'a_2': ['b_1', 'b_4', 'b_2', 'b_3'],
    'a_3': ['b_4', 'b_1', 'b_3', 'b_2'],
    'a_4': ['b_2', 'b_3', 'b_1', 'b_4'],
}

B = {
    'b_1': ['a_4', 'a_2', 'a_1', 'a_3'],
    'b_2': ['a_2', 'a_3', 'a_4', 'a_1'],
    'b_3': ['a_1', 'a_4', 'a_3', 'a_2'],
    'b_4': ['a_3', 'a_1', 'a_2', 'a_4']
}

metches = {}
free_a = [a for a in A.keys()]

for a in free_a:

    prefer_a = A[a]

    for b in prefer_a:
        if b not in list(metches.keys()):
            metches[b] = a

            if a in free_a:
                free_a.remove(a)

        elif b in list(metches.keys()):
            current_match = metches[b]
            
            if B[b].index(current_match) > B[b].index(a):
                
                metches[b] = a
                if a not in free_a:
                    free_a.remove(a)

                free_a.append(current_match)
            
print(metches)
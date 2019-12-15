from itertools import product
import csv

# comb = combinations_with_replacement([0,1,2,3,4,5,6,7,8,9,10],2)

# comb = combinations([0,1,2,3,4,5,6,7,8,9,10],2)

# perm = permutations((0,1,2,3,4,5),2)

single_a = [0,1,2,3,4,5,6,7,8,9,10]
single_a_vol = 22
single_b = [0,1,2,3,4,5,6,7,8,9,10]
single_b_vol = 24
single_c = [0,1,2,3,4,5,6,7,8,9,10]
single_c_vol = 26
bdouble_a = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_a_vol = 32
bdouble_b = [0,1,2,3,4,5,6,7,8,9,10]
bdouble_b_vol = 34
#bdouble_c = [0,1,2,3,4,5,6,7,8,9,10]
#bdouble_c_vol = 36
#rigid_a = [0,1,2,3,4,5,6,7,8,9,10]
#rigid_a_vol = 6
#rigid_b = [0,1,2,3,4,5,6,7,8,9,10]
#rigid_b_vol = 8
standalone = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
standalone_vol = 1

#truckcombinations = product(single_a,single_b,single_c,bdouble_a,bdouble_b,bdouble_c,rigid_a,rigid_b,standalone)
truckcombinations = product(single_a,single_b,single_c,bdouble_a,bdouble_b,standalone)
length_combinations = len(list(truckcombinations))

truckcombinations = product(single_a,single_b,single_c,bdouble_a,bdouble_b,standalone) #for some reason truckcombinations reset when I call its length, so need to call it again

relevant_combinations = [["single_a","single_b","single_c","bdouble_a","bdouble_b","standalone","total_pallets"]]

min_pallets = 200
max_pallets = min_pallets + 20

print(length_combinations)
count = 0

for item in list(truckcombinations):
    pallets = item[0]*single_a_vol + item[1]*single_b_vol + item[2]*single_c_vol + item[3]*bdouble_a_vol + \
              item[4]*bdouble_b_vol + item[5]*standalone_vol
    if pallets > min_pallets and pallets < max_pallets:
        combination_match = []
        for a in item:
            combination_match.append(a)
        combination_match.append(pallets)
        relevant_combinations.append(combination_match)
    count += 1
    status = count/length_combinations
    print(status)


def save_to_csv(relevant_combinations):
    with open('test.csv', 'w', errors='replace', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(relevant_combinations)
    csvFile.close()

save_to_csv(relevant_combinations)
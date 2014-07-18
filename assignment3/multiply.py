import MapReduce
import sys

"""
Multiply
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

# Dimensions (A - L X M, B - M X N
L = 5
M = 5
N = 5

def mapper(record):
    # key: document identifier
    # dna: document contents
    key = record[0]
    row = record[1]
    col = record[2]
    val = record[3]
        
    # for each element (i,j) of A, emit((i,k), (j, A[i,j])) for k in 1..N
    if key == "a":
    	for k in range(N):
    		mr.emit_intermediate((row, k), [col, val])
    else:
    	# for each element (j,k) of B, emit((i,k), (j, B[j,k])) for i in 1..L
    	for i in range(L):
    		mr.emit_intermediate((i, col), [row, val])

def reducer(key, list_of_values):
    
    # Initialize a list of length N
    val_list = [None]*N;
    
    # Initialize each of those lists as empty list
    for i in range(N):
    	val_list[i] = list()
    
    # Populate the lists with values from the mapper
    for v in list_of_values:
    	val_list[v[0]].append(v[1])	
    	
    # start calculating the sum
    sum = 0
    for i in range(N):
    	# if the length is not 2, it means that one of the elements is 0, so can exclude
    	if (len(val_list[i]) == 2):
    		sum += val_list[i][0]*val_list[i][1]
    key_val = list(key)
    key_val.append(sum)
    mr.emit(tuple(key_val))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

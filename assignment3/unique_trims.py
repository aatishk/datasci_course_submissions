import MapReduce
import sys

"""
Inverted Index
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # dna: document contents
    key = record[0]
    dna = record[1]
    
    # emit generic key and trimmed dna
    mr.emit_intermediate("generic", dna[:-10])

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence documents
    # AK: initialize the list of doc_id's to be empty set
    total = set()
    for v in list_of_values:
    	# AK: Add to the set.. does not add duplicates
    	total.add(v)
    	
    for dna in total:
    	mr.emit(dna)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

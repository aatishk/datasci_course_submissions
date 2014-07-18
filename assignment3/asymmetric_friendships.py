import MapReduce
import sys

"""
Friend Count
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
	person1 = record[0]
	person2 = record[1]
	mr.emit_intermediate(person1, record)
	mr.emit_intermediate(person2, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence documents
    
	forward = list()
	reverse = list()
	
	for val in list_of_values:
		if key == val[0]:
			forward.append(val[1])
		else:
			reverse.append(val[0])
	#print key, forward, reverse, list_of_values,"\n"
	
	for friend in forward:
		if friend not in reverse:
			mr.emit((key, friend))
			mr.emit((friend, key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

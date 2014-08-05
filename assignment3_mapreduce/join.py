import MapReduce
import sys

"""
Join
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    order_id = record[1]
    
    # Emit as (order_id, record)
    mr.emit_intermediate(order_id, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence documents
    # AK: initialize the list of doc_id's to be empty set
    # Before final emit, cast the set as list
    #print key, list_of_values,"\n"
    # AK: First item is order_item, rest are line_items
    order_item = list_of_values[0]
    for i in range(1,len(list_of_values)):
    	# use "+" operator to merge lists 
    	mr.emit(order_item + list_of_values[i])

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)

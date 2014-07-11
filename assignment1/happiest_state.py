import sys
import json
import re
import string

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
    
    #sent_file.seek(0)
    #tweet_file.seek(0)
    
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }
    
    states_happiness = {}
    states_counts = {}
	
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character
    	scores[term] = int(score)  # Convert the score to an integer.
    
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    for line in tweet_file:
    	tweet_json = json.loads(line)
    	#print tweet_json.keys()
    	if 'text' in tweet_json.keys() and tweet_json['lang'] == 'en':
    		tweet_txt = tweet_json['text']
    		tweet_txt_encoded = tweet_txt.encode('utf-8')
    		tweet_location = tweet_json['user']['location']
    		tweet_location_encoded = tweet_location.encode('utf-8')
    		#print tweet_location_encoded
    		   		
    		#print count, tweet_txt_encoded
    		#print count, tweet_txt_encoded.split()
    		score = 0
    		for word in tweet_txt_encoded.split():
    			#print word
    			word = re.sub("[\W\d_]", "", word.strip())
    			#print unicode(word, errors='ignore')
    			#print word
    			if word in scores.keys():
    				#print word, scores[word]
    				score += scores[word] 
    		#print score
    		
    		for key in states.keys():
    			if key in tweet_location_encoded or states[key] in tweet_location_encoded:
    				if key in states_happiness.keys():
    					states_happiness[key] += score
    					states_counts[key] += 1
    				else:
    					states_happiness[key] = score
    					states_counts[key] = 1
    					
    happiness_max = -100
    happy_state = None
    for key in states_happiness.keys():
    	happiness = 1.0*states_happiness[key]/states_counts[key]
    	#print happiness
    	if happiness > happiness_max:
    		happy_state = key
    
    print happy_state
    	
    sent_file.close()
    tweet_file.close()
    
if __name__ == '__main__':
    main()

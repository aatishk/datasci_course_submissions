import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])
    
    counts = {} # initialize an empty dictionary
    global_count = 0
	
    for line in tweet_file:
    	tweet_json = json.loads(line)

    	if 'text' in tweet_json.keys() and tweet_json['lang'] == 'en':
    		tweet_txt = tweet_json['text']
    		tweet_txt_encoded = tweet_txt.encode('utf-8')

    		for word in tweet_txt_encoded.split():
    			word = re.sub("[\W\d_]", "", word.strip())
    			word = word.lower()
    			global_count += 1
    			if word in counts.keys():
    				counts[word] += 1
    			else:
    				counts[word] = 1
    				   
    for key in counts.keys():
    	print key, 1.0*counts[key]/global_count	
    
    tweet_file.close()
    
if __name__ == '__main__':
    main()


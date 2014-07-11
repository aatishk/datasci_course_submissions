import sys
import json
import re

def main():
    tweet_file = open(sys.argv[1])
    
    counts = {} # initialize an empty dictionary
	
    for line in tweet_file:
    	tweet_json = json.loads(line)

    	if 'entities' in tweet_json.keys():
    		tweet_hashtags = tweet_json['entities']['hashtags']
    		
    		for hashtag in tweet_hashtags:
    			hashtag_text = hashtag['text']
    			hashtag_text= hashtag_text.encode('utf-8')
    			hashtag_text= hashtag_text.lower()
    			
    			if hashtag_text in counts.keys():
    				counts[hashtag_text] += 1
    			else:
    				counts[hashtag_text] = 1
    
    total_count = 0 				   
    for key in counts.keys():
    	total_count += counts[key]
    
    for key in counts.keys():
    	counts[key] = 1.0*counts[key]/total_count
    
    count = 0
    for w in sorted(counts, key=counts.get, reverse=True):
    	count += 1
    	print w, counts[w]*total_count
    	if count > 9:
    		break
    
    tweet_file.close()

if __name__ == '__main__':
    main()


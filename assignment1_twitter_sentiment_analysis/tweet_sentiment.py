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
    
    scores = {} # initialize an empty dictionary
    for line in sent_file:
    	term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character
    	scores[term] = int(score)  # Convert the score to an integer.
    
    #print scores.items() # Print every (term, score) pair in the dictionary
    
    count = 0
    for line in tweet_file:
    	tweet_json = json.loads(line)
    	#print tweet_json.keys()
    	count += 1
    	if 'text' in tweet_json.keys() and tweet_json['lang'] == 'en':
    		tweet_txt = tweet_json['text']
    		tweet_txt_encoded = tweet_txt.encode('utf-8')
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
    		print score
    	else:
    		print 0
    	
    sent_file.close()
    tweet_file.close()
    
if __name__ == '__main__':
    main()

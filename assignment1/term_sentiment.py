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
    scores_new = {}
    counts_new = {}
    for line in tweet_file:
    	tweet_json = json.loads(line)
    	#print tweet_json.keys()
    	count += 1
    	if 'text' in tweet_json.keys():
    		tweet_txt = tweet_json['text']
    		tweet_txt_encoded = tweet_txt.encode('utf-8')
    		#print count, tweet_txt_encoded
    		#print count, tweet_txt_encoded.split()
    		score = 0
    		new_words = []
    		for word in tweet_txt_encoded.split():
    			#print word
    			word = re.sub("[\W\d_]", "", word.strip())
    			word = word.lower()
    			#print unicode(word, errors='ignore')
    			#print word
    			if word in scores.keys():
    				#print word, scores[word]
    				score += scores[word]
    			else:
    				new_words.append(word)
    		#print score	
    		for word in new_words:
    			if word in scores_new.keys():
    				scores_new [word] += score
    				counts_new [word] += 1
    			else:
    				scores_new [word] = score
    				counts_new [word] = 1
    
    for key in scores_new.keys():
    	if key != "":
    		print key, 1.0*scores_new[key]/counts_new[key]
    		#print key, "{:0.3f}".format(1.0*scores_new[key]/counts_new[key])	
    
    sent_file.close()
    tweet_file.close()
    
if __name__ == '__main__':
    main()


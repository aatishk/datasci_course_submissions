SELECT a.docid, b.docid, sum(a.count*b.count)  
	FROM frequency a
	JOIN frequency b 
	ON a.term = b.term
	WHERE a.docid = '10080_txt_crude' AND b.docid = '17035_txt_earn'
	GROUP BY b.docid;

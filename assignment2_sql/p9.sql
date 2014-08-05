CREATE VIEW frequencyNew AS
	SELECT * FROM frequency
	UNION
	SELECT 'q' AS docid, 'washington' AS term, 1 AS count 
	UNION
	SELECT 'q' AS docid, 'taxes' AS term, 1 AS count 
	UNION
	SELECT 'q' AS docid, 'treasury' AS term, 1 AS count;

SELECT MAX(score) FROM(
	SELECT SUM(a.count*b.count) AS score  
		FROM frequencyNew a
		JOIN frequencyNew b 
		ON a.term = b.term
		WHERE a.docid = 'q'
		GROUP BY b.docid
		ORDER BY score DESC)x;

DROP VIEW frequencyNew;


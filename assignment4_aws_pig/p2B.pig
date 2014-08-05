-- register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
register ./myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
-- raw = LOAD './cse344-test-file' USING TextLoader as (line:chararray);

-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 
raw = LOAD './btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the objects out (because group by produces a tuple of each object
-- in the first column, and we want each object ot be a string, not a tuple),
-- and count the number of tuples associated with each object
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

--group the counts by count column
count_by_counts = group count_by_subject by (count)  PARALLEL 50;

-- store the histogram
histogram_count = foreach count_by_counts generate flatten($0) as x, COUNT($1) as y PARALLEL 50;

-- store the results in the folder /user/hadoop/example-results
-- fs -mkdir /user/hadoop
-- store count_by_subject_ordered into '/user/hadoop/results-2B' using PigStorage();
store histogram_count into './results-2B' using PigStorage();

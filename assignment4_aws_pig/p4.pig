register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar

-- load the test file into Pig
raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-*' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = foreach raw generate FLATTEN(myudfs.RDFSplit3(line)) as (subject:chararray,predicate:chararray,object:chararray);

--group the n-triples by subject column
subjects = group ntriples by (subject) PARALLEL 50;

-- flatten the subjects out (because group by produces a tuple of each subject
-- in the first column, and we want each subject ot be a string, not a tuple),
-- and count the number of tuples associated with each subject
count_by_subject = foreach subjects generate flatten($0), COUNT($1) as count PARALLEL 50;

--group the counts by count column
count_by_counts = group count_by_subject by (count)  PARALLEL 50;

-- store the histogram
histogram_count = foreach count_by_counts generate flatten($0) as x, COUNT($1) as y PARALLEL 50;

-- store the results in the folder /user/hadoop/results-4
fs -mkdir /user/hadoop
store histogram_count into '/user/hadoop/results-4' using PigStorage();

-- move the files to local directory
fs -copyToLocal /user/hadoop/results-4 results-4

-- merge results into a single file
fs -getmerge  /user/hadoop/results-4 results-4-output

-- register s3n://uw-cse-344-oregon.aws.amazon.com/myudfs.jar
register ./myudfs.jar

-- load the test file into Pig
-- raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/cse344-test-file' USING TextLoader as (line:chararray);
raw = LOAD './cse344-test-file' USING TextLoader as (line:chararray);

-- later you will load to other files, example:
--raw = LOAD 's3n://uw-cse-344-oregon.aws.amazon.com/btc-2010-chunk-000' USING TextLoader as (line:chararray); 
--raw = LOAD './btc-2010-chunk-000' USING TextLoader as (line:chararray); 

-- parse each line into ntriples
ntriples = FOREACH raw GENERATE FLATTEN(myudfs.RDFSplit3(line)) AS (subject:chararray,predicate:chararray,object:chararray);

---
good_subjects =  FILTER ntriples BY (subject MATCHES '.*business.*')  PARALLEL 50;
good_subjects2 = FOREACH good_subjects GENERATE subject as subject2, predicate as predicate2, object as object2;

---
joined = JOIN good_subjects BY subject, good_subjects2 BY subject2;

-- get distinct joined
joined2 = DISTINCT joined;

-- store the results in the folder /user/hadoop/example-results
-- fs -mkdir /user/hadoop
-- store joined2 into '/user/hadoop/results-3A' using PigStorage();
STORE joined2 INTO './results-3A' USING PigStorage();

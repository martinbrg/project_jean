# Project Jean - Leyla's SCL90 Survey
-------------------------------------

The goal of this project is to automate the SCL90 surveys. While patients won't care so much if they fill in a survey on paper or on a tablet, the evaluation is currently all manual, with pencil and paper.
Hence, the idea is to automate the part of summing up the scores and derive the actual diagnosis.

## Basic Algorithm
-------------------

1. Sort the survey answers into individual scales, for example "these questions relate to _anxiety_
2. Find "Basic Values"
   a. Sum up each scale
   b. Average
   c. Look for values >0
   d. Sum of sums
   e. 2 more which I can't currently remember
3. Find "T-Values" (T for _transformed_), by looking up the basic values in reference tables
   a. Depending on age, gender
   b. Each basic value has its own lookup table
4. Use the T-Values to form a verdict
   a. For example, >60 means "slightly above average"
 

## What the files do
---------------------

* survey.ps --> Generate "Basic Results" (i.e. just summing up the survey response)
* t_values.ps --> Lookup the "Basic Results" in the tables under "data". The lookup values depend on age and gender
* tests ... well....they test
* Main --> Contains the function which generates the verdict

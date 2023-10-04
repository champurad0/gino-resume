# Gino's Cloud Resume

## Why 

This is going to be my walkthrough on the AWS Cloud Resume Challenge. I am using this challenge to walkthrough several AWS offering and to get some hands on experince. 

## AWS Offerings Used

Here are some of the key resources I used. 

 - S3: I created a bucket where I uploaded my website folder.
 - Cloudfront: I created a distribution and linked the S3 bucket with the provided JSON Policy
 - Route 53: I ordered a domain through Route 53 and used that to create an SSL certificate. This also linked to my website.
 - DynamoDB: Created a table to store view counter data
 - AWS Lambda: Wrote python script to pull data from DDB and then write new data to table aswell
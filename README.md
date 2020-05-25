# The Evaluator : Predict an applicant's decision to CSH
## What is CSH? 
CSH, or [Computer Science House](https://www.csh.rit.edu/), is a fantastic 
community at RIT that I am fortunate enough to be a member of. We all have a 
passion for learning and teaching in regards to anything we're passionate about. 
We try to help each other develop as professionals and individuals with whatever we do. 

## What is our intro process?
In order to join the organization, a prospective member goes through our intro
process and attempts to meet the requirements we set out for them. They are as
follows:
1. Obtain a certain percentage of signatures from our current upperclassmen,
which implies that they have spoken to you and think you would be a good fit
for the organization.
2. Attend a certain number of our House Meetings or general meetings, where we 
go over important updates and discussions for the organization
3. Attend a certain number of our Directorship Meetings, where we discuss
updates for each of our executive board positions
4. Attend a certain number of our Technical Seminars, where we provide
information on some topic, ranging from programming tips to AI math
5. Attend a certain number of our social events, where we just get together
and do something social 

Once the Introductory Evaluations meeting occurs, each voting member uses these
metrics to inform their decision on whether or not to welcome the applicant into
the organization. I thought it would be a cool idea to create something that
could predict how the organization would end up voting, so I did. The name that
we came up with for it is, The Evaluator.

## What is The Evaluator, how does it work?
### What it is, generally
It is simply a tertiary classification model which takes in an applicant's intro 
data, which are the numerical representations of the requirements described 
above, and says whether or not CSH is more likely to pass, fail, or conditional 
that applicant. 

### How it was made
1. A copy of the CSH databases was acquired in the form of a raw NoSQL dump. A
local SQL database was created from that dump. Various SQL queries were made to
get the appropriate features and results. 
2. The model itself is a logistic regression model which 

### Usage
Want to see whether or not you'd make it into CSH? Follow these steps 
1. Go ahead and download ai\_vote.py. 
2. Make sure you have numpy and scipy installed in your working directory. 
3. Now run the program! You can do this in one of two ways : 
    1. File mode : Simply run the file with '-f' and then the filename afterwards
       - Ex : python ai\_vote.py -f dylan\_info.csv 
       - For convenience sake, make your file a .csv with the below format. In this way, you can try multiple people!
     name,signatures_missed,house_meetings_missed,directorship_meetings_attended,technical_seminars_attended,socials
     where socials is just a 1 or 0 for if you did or did not do any social events.
    2. Command line mode : Supply all of the conditional data through command line argument in the below format
       - Ex : python ai\_vote.py s_m h_m d_a t_a s
          - s_m : number of signatures missed
          - h_m : number of house meetings missed
          - d_a : number of directorship meetings attended
          - t_a : number of technical seminars attended
          - s : whether or not you attended social events. Put 1 if you attended more 0 events, put 0 otherwise.

# The Evaluator : Predict an applicant's decision to CSH
## What is CSH? 
CSH, or [Computer Science House](https://www.csh.rit.edu/), is a fantastic 
community at RIT that I am fortunate enough to be a member of. We all have a 
passion for learning and teaching, and we try to help each other develop as 
professionals and individuals.  

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
### What it is
It is simply a tertiary classification model which takes in an applicant's intro 
data, which are the numerical representations of the requirements described 
above, and says whether or not CSH is more likely to pass, fail, or conditional 
that applicant. 

## TODO Items
1. Regularized vs. non regularized

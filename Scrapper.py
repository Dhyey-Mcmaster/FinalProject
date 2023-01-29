
import praw


#scrapper info
user_agent = "Scraper 1.0"
reddit = praw.Reddit(
    client_id="2YNF6cMmsZ7NByyk5fhARg",
    client_secret="Vv6CoQu8-jOmktbxqMgCsAoL_aNESQ",
    user_agent=user_agent,
    )

for submission in reddit.subreddit('wallstreetbets').hot(limit=None): #checking each submission. can be hot/new/top
    headlines=[]
    if (submission.id not in headlines): #avoiding duplicates
        print(submission.title)
        print(submission.score) #amount of upvotes vs downvotes
        print(submission.id)
        headlines.append(submission.id) # ID will be unique 
        
                

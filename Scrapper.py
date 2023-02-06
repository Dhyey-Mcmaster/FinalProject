import praw
headlines=[]
posts = []

postsFile = open("RedditPosts.txt", "a", encoding='utf-8')


#scrapper info
user_agent = "Scraper 1.0"
reddit = praw.Reddit(
    client_id="2YNF6cMmsZ7NByyk5fhARg",
    client_secret="Vv6CoQu8-jOmktbxqMgCsAoL_aNESQ",
    user_agent=user_agent,
    )

for submission in reddit.subreddit('wallstreetbets').hot(limit=None): #checking each submission. can be hot/new/top
    if (submission.id not in headlines): #avoiding duplicates 
        postsFile.write(submission.title)     
        postsFile.write('\n')
        postsFile.write(str(submission.score))
        postsFile.write('\n')        
        headlines.append(submission.id) # ID will be unique
postsFile.close()

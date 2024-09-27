import praw  # Import the PRAW library

# Create a Reddit instance using the credentials and configuration specified in 'bot1' in the praw.ini file
reddit = praw.Reddit('bot1')

# Select the 'learnpython' subreddit
subreddit = reddit.subreddit("learnpython")

#initializing count variable
count=0

# Iterate through the top 5 hot posts in the 'learnpython' subreddit
for submission in subreddit.hot(limit=5):
    #checking if upvotes are more than 10
    if submission.score > 9:
        count=1
        # Print the title of the submission
        print("Title: ", submission.title)
        
        # Print the text content of the submission (selftext is empty for link posts)
        print("Text: ", submission.selftext)
        
        # Print the score (number of upvotes minus downvotes) of the submission
        print("Score: ", submission.score)
        
        # Print a separator line
        print("---------------------------------\n")

if count==0:
    print("No Hot posts with more than 10 upvotes")
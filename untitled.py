import tweepy
import credential
import csv #Import csv

auth = tweepy.OAuthHandler(credential.consumer_key, credential.consumer_secret)
auth.set_access_token(credential.access_token, credential.access_token_secret)

api = tweepy.API(auth)

# Open/create a file to append data to
csvFile = open('01-03-2019 - 12-03-2019 #2019 Ganti Presiden.csv', 'a', encoding='utf-8')

#Use csv writer
csvWriter = csv.writer(csvFile, delimiter=' ',lineterminator='\r')
rows = 0

for tweet in tweepy.Cursor(api.search,
                           q="#2019GantiPresiden",
                           since="2019-02-01",
                           until="2019-03-12",
                           lang="id").items():
        # Write a row to the CSV file. I use encode UTF-8
    csvWriter.writerow([tweet.created_at, tweet.text ])
    rows += 1

print(rows)
csvFile.close()
import numpy as np
import tweepy as tw
import pandas as pd 
import re
from textblob import TextBlob

auth = tw.OAuthHandler("WD65CYntmlMTxZrGu0I1RdZ62", "c2FRWC5XHRTVJ9jGgSf6Z5SpBZjyz9lRpELqnhhrs631L71llL")
auth.set_access_token("127336982-2cD3rqvnqVky3wnBCb9dAV5BP6KQjxfOYno5X1FM", "3XtPOV3CFszk6epS9Ku3uBWrQeXzPHJwRNUG5tEtKFf9o")
api = tw.API(auth)

query_search = "Cyberbullyng" + "-filter:retweets"
public_tweets = tw.Cursor(api.search, q=query_search).items(3000)

analysis = None
tweets = []

Positivo = 0
Negativo = 0
Neutro = 0

def analise(pol):
    if pol < 0:
        return 'Negativo'
    elif pol == 0:
        return 'Neutro'
    else:
        return 'Positivo'
    
for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    if tweet.lang == 'en':
        print(analysis)
        polarity = analysis.sentiment.polarity
        tweets.append(polarity)
        print (analise(polarity) + ", " + str(polarity))
        
        if analise(polarity) == 'Positivo':
            Positivo += 1
        elif analise(polarity) == 'Negativo':
            Negativo +=1
        else:
            Neutro +=1
            
df = pd.DataFrame({'Polarity': [Positivo, Negativo, Neutro]
                 },
                index=['Positivo','Negativo', 'Neutro'])

dff = pd.DataFrame({'Polarity': [Positivo, Negativo]
                  },
                 index=['Positivo', 'Negativo'])

plot = df.plot.pie(y='Polarity', figsize=(5,5), autopct='%1.1f%%', legend=False)
plot = dff.plot.pie(y='Polarity', figsize=(5,5), autopct='%1.1f%%', legend=False)

print('MÉDIA DE SENTIMENTO: ' +str(np.mean(tweets)))

print(f'Positivo: {Positivo}\nNegativo: {Negativo}\nNeutro: {Neutro}')

    
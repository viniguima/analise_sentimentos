{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e4e1c81c",
   "metadata": {},
   "outputs": [
    {
     "ename": "TweepError",
     "evalue": "Twitter error response: status code = 429",
     "output_type": "error",
     "traceback": [
      "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[0;31mTweepError\u001b[0m                                Traceback (most recent call last)",
      "\u001b[0;32m<ipython-input-1-2617564d7e52>\u001b[0m in \u001b[0;36m<module>\u001b[0;34m\u001b[0m\n\u001b[1;32m     27\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0;34m'Positivo'\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     28\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 29\u001b[0;31m \u001b[0;32mfor\u001b[0m \u001b[0mtweet\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mpublic_tweets\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     30\u001b[0m     \u001b[0manalysis\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mTextBlob\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mtext\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     31\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0mtweet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlang\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m'en'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/tweepy/cursor.py\u001b[0m in \u001b[0;36m__next__\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m     49\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     50\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0m__next__\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 51\u001b[0;31m         \u001b[0;32mreturn\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     52\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     53\u001b[0m     \u001b[0;32mdef\u001b[0m \u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/tweepy/cursor.py\u001b[0m in \u001b[0;36mnext\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    241\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m \u001b[0;32mor\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_index\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    242\u001b[0m             \u001b[0;31m# Reached end of current page, get the next page...\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 243\u001b[0;31m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_iterator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    244\u001b[0m             \u001b[0;32mwhile\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;36m0\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    245\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mcurrent_page\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mpage_iterator\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mnext\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/tweepy/cursor.py\u001b[0m in \u001b[0;36mnext\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    130\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    131\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mindex\u001b[0m \u001b[0;34m>=\u001b[0m \u001b[0mlen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mresults\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m-\u001b[0m \u001b[0;36m1\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 132\u001b[0;31m             \u001b[0mdata\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmax_id\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmax_id\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mparser\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mRawParser\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    133\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    134\u001b[0m             \u001b[0;32mif\u001b[0m \u001b[0mhasattr\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmethod\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'__self__'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/tweepy/binder.py\u001b[0m in \u001b[0;36m_call\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    251\u001b[0m                 \u001b[0;32mreturn\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    252\u001b[0m             \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 253\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mmethod\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mexecute\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    254\u001b[0m         \u001b[0;32mfinally\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    255\u001b[0m             \u001b[0mmethod\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msession\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mclose\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;32m~/opt/anaconda3/lib/python3.8/site-packages/tweepy/binder.py\u001b[0m in \u001b[0;36mexecute\u001b[0;34m(self)\u001b[0m\n\u001b[1;32m    232\u001b[0m                     \u001b[0;32mraise\u001b[0m \u001b[0mRateLimitError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merror_msg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    233\u001b[0m                 \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 234\u001b[0;31m                     \u001b[0;32mraise\u001b[0m \u001b[0mTweepError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0merror_msg\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mresp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mapi_code\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mapi_error_code\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    235\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    236\u001b[0m             \u001b[0;31m# Parse the response payload\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
      "\u001b[0;31mTweepError\u001b[0m: Twitter error response: status code = 429"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "import tweepy as tw\n",
    "import pandas as pd \n",
    "import re\n",
    "from textblob import TextBlob\n",
    "\n",
    "auth = tw.OAuthHandler(\"WD65CYntmlMTxZrGu0I1RdZ62\", \"c2FRWC5XHRTVJ9jGgSf6Z5SpBZjyz9lRpELqnhhrs631L71llL\")\n",
    "auth.set_access_token(\"127336982-2cD3rqvnqVky3wnBCb9dAV5BP6KQjxfOYno5X1FM\", \"3XtPOV3CFszk6epS9Ku3uBWrQeXzPHJwRNUG5tEtKFf9o\")\n",
    "api = tw.API(auth)\n",
    "\n",
    "query_search = \"Cyberbullyng\" + \"-filter:retweets\"\n",
    "public_tweets = tw.Cursor(api.search, q=query_search).items(3000)\n",
    "\n",
    "analysis = None\n",
    "tweets = []\n",
    "\n",
    "Positivo = 0\n",
    "Negativo = 0\n",
    "Neutro = 0\n",
    "\n",
    "def analise(pol):\n",
    "    if pol < 0:\n",
    "        return 'Negativo'\n",
    "    elif pol == 0:\n",
    "        return 'Neutro'\n",
    "    else:\n",
    "        return 'Positivo'\n",
    "    \n",
    "for tweet in public_tweets:\n",
    "    analysis = TextBlob(tweet.text)\n",
    "    if tweet.lang == 'en':\n",
    "        print(analysis)\n",
    "        polarity = analysis.sentiment.polarity\n",
    "        tweets.append(polarity)\n",
    "        print (analise(polarity) + \", \" + str(polarity))\n",
    "        \n",
    "        if analise(polarity) == 'Positivo':\n",
    "            Positivo += 1\n",
    "        elif analise(polarity) == 'Negativo':\n",
    "            Negativo +=1\n",
    "        else:\n",
    "            Neutro +=1\n",
    "            \n",
    "df = pd.DataFrame({'Polarity': [Positivo, Negativo, Neutro]\n",
    "                 },\n",
    "                index=['Positivo','Negativo', 'Neutro'])\n",
    "\n",
    "dff = pd.DataFrame({'Polarity': [Positivo, Negativo]\n",
    "                  },\n",
    "                 index=['Positivo', 'Negativo'])\n",
    "\n",
    "plot = df.plot.pie(y='Polarity', figsize=(5,5), autopct='%1.1f%%', legend=False)\n",
    "plot = dff.plot.pie(y='Polarity', figsize=(5,5), autopct='%1.1f%%', legend=False)\n",
    "\n",
    "print('MÉDIA DE SENTIMENTO: ' +str(np.mean(tweets)))\n",
    "\n",
    "print(f'Positivo: {Positivo}\\nNegativo: {Negativo}\\nNeutro: {Neutro}')\n",
    "\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b68d9ce",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

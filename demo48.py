def build_username_to_mention_count(tweet_list):
    """ (list of str) -> dict of {str: int}

        Return a dictionary where each key is a username mentioned in tweet_list
        and each value is the total number of times this username was mentioned in
        all of the tweets in tweet_list.

        >>> tweets = ['hi @me and @you', '@me yesterday', 'i saw @you', '@yo @you there']
        >>> d = build_username_to_mention_count(tweets)
        >>> d == {'yo': 1, 'me': 2, 'you': 3}
        True
    """
    d = {}
    for sentence in tweet_list:
        words = sentence.split()
        for word in words:
            if word.startswith('@'):
                username = word[1:]
                if username in d:
                    d[username] = d[username] + 1
                else:
                    d[username] = 1
    
    return d 

def most_mentioned_username(tweet_list):
    """ (list of str) -> str

    Preconditions:
    - at least one of the strings in tweet_list will include a mention
    - each username mentioned in tweet_list will have a unique total number
    of mentions in tweet_list (i.e., no ties for the number of mentions)

    Return the username with the most mentions in tweet_list.

    >>> tweets = ['hi @you there', '@me yesterday', 'saw @you']
    >>> most_mentioned_username(tweets)
    'you'
    """

    d = build_username_to_mention_count(tweet_list)

    biggest_users = []
    biggest_value = 0
    for k, v in d.items():
        if v > biggest_value:
            del biggest_users[:]
            biggest_users.append((k, v))
            biggest_value = v
        elif v == biggest_value:
            biggest_users.append((k, v))

    users = []
    for x in biggest_users:
        users.append(x[0])
        
    return users

if __name__ == '__main__':
    tweets = ['hi @me and @you', '@me yesterday', 'i saw @you', '@yo there']

    print most_mentioned_username(tweets)

        

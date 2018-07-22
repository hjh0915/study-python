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

def invert_dictionary(d):
    """ dict of {str: int} -> dict of {int: str}
        Precondition: the values in d's key/value pairs are all different
        Return a new dictionary that is the inverse of d. (See example below.)
        >>> d = invert_dictionary({'me': 2, 'yo': 1, 'you': 3})
        >>> d == {2: 'me', 1: 'yo', 3: 'you'}
        True
    """
    d2 = {}
    for a,b in d.items():
        d2[b] = a 
    
    return d2 

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
    d1 = build_username_to_mention_count(tweet_list)
    d2 = invert_dictionary(d1)
    
    return d2[max(d2.keys())]


if __name__ == '__main__':
    tweets = ['hi @you there', '@me yesterday', 'saw @you']

    print most_mentioned_username(tweets)
    
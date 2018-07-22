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
        # y = ['hi', '@me', 'and', '@you']
        for word in words:
            if word.startswith('@'):
                username = word[1:]
                if username in d:
                    d[username] = d[username] + 1
                else:
                    d[username] = 1

    return d

if __name__ == '__main__':
    tweets = ['hi @me and @you', '@me yesterday', 'i saw @you', '@yo @you there']
    print build_username_to_mention_count(tweets)

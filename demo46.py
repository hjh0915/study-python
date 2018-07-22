# -*- coding: utf8 -*-
class Review:
    """ A review of a restaurant. """
    def __init__(self, reviewer_name, review_comments, is_recommended):
        """ (Review, str, str, bool) -> NoneType

        Record the reviewer's name reviewer_name, the reviewer's comments
        review_comments, and the reviewer's recommendation is_recommended.

        >>> review = Review('Lynn Crawford', 'Delicious food!', True)
        >>> review.reviewer
        'Lynn Crawford'
        >>> review.comments
        'Delicious food!'
        >>> review.recommend
        True
        """
        
        self.reviewer = reviewer_name 
        self.comments = review_comments 
        self.recommend = is_recommended 

    def change_comments(self, new_comments):
        """ (Review, str) -> NoneType

        Update the comments for this review to new_comments.

        >>> review = Review('Lynn Crawford', 'So terrible!', False)
        >>> review.change_comments('Please change a dish!')
        >>> review.comments
        'Please change a dish!'
        """

        self.comments = new_comments 

    def __str__(self):
        """ (Review) -> str

        Return a string representation of this review.

        >>> review = Review('Susur Lee', 'Excellent!', True)
        >>> str(review)
        'recommended by Susur Lee: Excellent!'
        >>> review = Review('Mark McEwan', 'Room for improvement.', False)
        >>> str(review)
        'not recommended by Mark McEwan: Room for improvement.'
        """
        if self.recommend:
            review = 'recommended by {}: {}'.format(self.reviewer, self.comments)
        else:
            review = 'not recommended by {}: {}'.format(self.reviewer, self.comments)

        return review

class Restaurant:
    """ Information about a particular restaurant including its name,
    price range, the types of cuisines it serves, and reviews."""

    def __init__(self, name, price_range, cuisine_list):
        """ (Restaurant, str, str, list of str) -> NoneType

        Record the restaurant's name name, price range price_range, and types of cuisines
        cuisines_list. There are initially no reviews of this restaurant.

        >>> rest = Restaurant('Dumplings R Us', '$$', ['Chinese', 'Japanese'])
        >>> rest.name
        'Dumplings R Us'
        >>> rest.price_range
        '$$'
        >>> rest.cuisine_list
        ['Chinese', 'Japanese']
        >>> rest.reviews
        []
        """
        # Assume this method body has been correctly implemented.
        self.name = name 
        self.price_range = price_range 
        self.cuisine_list = cuisine_list
        self.reviews = []
 
    def add_review(self, review):
        """ (Restaurant, Review) -> NoneType

        >>> rest = Restaurant('Mexican Grill', '$$$', ['Mexican'])
        >>> rest.reviews
        []
        >>> review = Review('Susur Lee', 'Excellent!', True)
        >>> rest.add_review(review)
        >>> str(rest.reviews[0])
        'recommended by Susur Lee: Excellent!'
        """
        # Assume this method body has been correctly implemented.
        self.reviews.append(review)

    def __eq__(self, other):
        """ (Restaurant, Restaurant) -> bool

        Return whether this restaurant has the same name and price_range
        as other.

        >>> r1 = Restaurant('Dumplings R Us', '$$', ['Chinese', 'Japanese'])
        >>> r2 = Restaurant('Dumplings R Us', '$$', ['Chinese', 'Japanese'])
        >>> r3 = Restaurant('Deep Fried Everything', '$', ['Canadian'])
        >>> r1 == r2
        True
        >>> r2 == r3
        False
        """

        return self.name == other.name and self.price_range == other.price_range 

    def recommended_percentage(self):
        """ (Restaurant) -> number

        Precondition: this restaurant has at least one review

        Return the percentage of reviews that recommend this restaurant.

        >>> rest = Restaurant('Mexican Grill', '$$$', ['Mexican'])
        >>> rest.add_review(Review('Susur Lee', 'Excellent!', True))
        >>> rest.add_review(Review('Mark McEwan', 'Room for improvement.', False))
        >>> rest.recommended_percentage()
        50.0
        """
        good_review = 0
        bad_review = 0
        for review in self.reviews:
            if review.recommend:
                good_review = good_review + 1
            else:    
                bad_review = bad_review + 1 
        
        x = (good_review * 1.0) / (good_review + bad_review) * 100 
        return round(x, 2)

if __name__=='__main__':
    #import doctest
    #doctest.testmod()

    rest = Restaurant('余干菜馆', 'RMB', ['中国'] )

    r1 = Review('胡俊华', '辣椒小炒肉很好吃', True)
    rest.add_review(r1)

    r2 = Review('胡志刚', '都不错', True)
    rest.add_review(r2)

    r3 = Review('小华', '不好吃', False)
    rest.add_review(r3)
    
    x = rest.recommended_percentage()
    print '{}%'.format(x)



    
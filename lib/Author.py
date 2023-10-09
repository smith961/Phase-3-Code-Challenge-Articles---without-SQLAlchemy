class Author:
    def __init__(self, name):
        self.name = name


Author.articles()
#Return a list of Article instances the author has written

Author.magazines()
#Return a **unique** list of Magazine instances for which the author has 
#contributed to

Author.add_article(magazine, title)
# - Given a magazine (as Magazine instance) and a title (as a string), creates a new Article instance and associates it with that author and that magazine.

Author.topic_areas()
#Returns a **unique** list of strings with the categories of the magazines the author has contributed to

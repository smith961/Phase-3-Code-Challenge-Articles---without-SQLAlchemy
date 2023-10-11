from Article import *
from Magazine import *


class Author:
    all_articles = []
    def __init__(self, name=""):
        self._name = name
        print (self._name)
    
    def get_name(self):
        return self._name
    
    def get_all_aritcles(self):
        pass
    
    def get_all_magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass
    
    def __repr__(self):
        return f"Author : '{self._name}'"
    
    
        



author1 = Author("Albert Smith")
author2 = Author("Empress Rukky")


# print(author1.get_name())

# print(author2.name)


# Author.articles()
# #Return a list of Article instances the author has written

# Author.magazines()
# #Return a **unique** list of Magazine instances for which the author has 
# #contributed to

# # Author.add_article(magazine, title)
# # - Given a magazine (as Magazine instance) and a title (as a string), creates a new Article instance and associates it with that author and that magazine.

# Author.topic_areas()
# #Returns a **unique** list of strings with the categories of the magazines the author has contributed to

from Magazine import *
from Author import *

class Article:
    def __init__(self, Author, Magazine, title ):
        self.author = Author
        self.magazine = Magazine
        self.title = title
        self.all = []
        
        

    def get_all(self,name):
        self.all.append(self.name) #- Returns a list of all Article instances
        print (self.all)
        

    def get_author(self):
        return self.author
        
    
    pass

article1 = Article(author1 , magazine1 ,"War Comes to Israel")
article2 = Article(author2 , magazine2, "The Trump Boys Can't Recall a Thing")

print(article1.title)

print(article1.get_all)

# Article.author()  - Returns the author for that given article
print(article1.author) 


# Article.magazine() -#Returns the magazine for that given article
print(article1.magazine)
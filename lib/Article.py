from Magazine import *
from Author import *

class Article:
    all = []
    def __init__(self,  author = Author, magazine = Magazine, title="" ):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
    
    def get_title(self): #- Returns the title for that given article
        return self.title
    
    def get_author(self):
        return self.author
    
    def get_magazine(self):
        return self.magazine
    
    def __repr__(self):
        return f"{self.title}"
        pass
        
    
    pass

article1 = Article(author1 , magazine1 ,"War Comes to Israel")
article2 = Article(author2 , magazine2, "The Trump Boys Can't Recall a Thing")



print(article1.get_title())

print(Article.all)

print(article1.get_author())

print(article1.get_magazine())


# print(article1.get_all("edrk"))

# Article.author()  - Returns the author for that given article
# print(article1.get_author(author1)) 



# Article.magazine() -#Returns the magazine for that given article
# print(article1.magazine)
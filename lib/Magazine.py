class Magazine:
    all = []
    def __init__(self, name="", category=""):
        self.name = name
        self.category = category
        self.articles = []
        Magazine.all.append(self)
    
    def get_name(self): #Returns the name of this magazine
         return self.name
    
    def get_category(self): # - Returns the category of this magazine
        return self.category
    
    def contributors(self):
        pass
    
    @classmethod
    def find_by_name(cls):
        pass
    
    @classmethod
    def article_titles(cls): #  - Returns a list of Author instances who have written for this magazine
        pass
    
    def contributing_authors(self):  #Returns a list of authors who have written more than 2 articles for the magazine
        #for loop
        pass
    
    def __repr__(self):
        return f"Magazine('{self.name}' , '{self.category}')"
        

magazine1 = Magazine("VanityFair" ,"Fashion")
magazine2 = Magazine("Time" ,"New York City")
magazine3 = Magazine("Forbes" , "Business")

print(magazine1.get_name()) #Returns the name of this magazine

print(magazine1.get_category()) # - Returns the category of this magazine

print(Magazine.all) # Returns a list of all Magazine instances






# Magazine.contributors()
# #Returns a list of Author instances who have written for this magazine

# Magazine.find_by_name
# # - Given a string of magazine's name, this method returns the first magazine object that matches

# Magazine.article_titles()
# # - Returns an list strings of the titles of all articles written for that magazine


# Magazine.contributing_authors()
# # - Returns a list of authors who have written more than 2 articles for the magazine


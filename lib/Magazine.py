class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all = []
    
    def get_all(self):
        self.all.append(self.name) #Returns a list of all Magazine instances
        return self.all
        pass

    def topic_areas(self):
        pass

    @classmethod
    def find_by_name(cls):
        pass

    @classmethod
    def article_titles(cls):
        pass

    def contributing_authors(self): #  - Returns a list of Author instances who have written for this magazine
        pass

magazine1 = Magazine("VanityFair" ,"Fashion")
magazine2 = Magazine("Time" ,"New York City")
magazine1.name = "Vgs"
magazine= [magazine1,magazine2]
print(magazine2.get_all())


# print(magazine1.name)

# Magazine.contributors()
# #Returns a list of Author instances who have written for this magazine

# Magazine.find_by_name
# # - Given a string of magazine's name, this method returns the first magazine object that matches

# Magazine.article_titles()
# # - Returns an list strings of the titles of all articles written for that magazine


# Magazine.contributing_authors()
# # - Returns a list of authors who have written more than 2 articles for the magazine
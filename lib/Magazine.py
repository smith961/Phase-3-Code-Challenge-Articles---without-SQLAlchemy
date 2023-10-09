class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self.all = []
    
    def get_all(self):
        self.all.append(self.name)
        pass

    def topic_areas(self):
        pass

    @classmethod
    def find_by_name(self):
        pass

    @classmethod
    def article_titles(self):
        pass

    def contributing_authors(self):
        pass


Magazine.contributors()
#Returns a list of Author instances who have written for this magazine

Magazine.find_by_name
# - Given a string of magazine's name, this method returns the first magazine object that matches

Magazine.article_titles()
# - Returns an list strings of the titles of all articles written for that magazine


Magazine.contributing_authors()
# - Returns a list of authors who have written more than 2 articles for the magazine
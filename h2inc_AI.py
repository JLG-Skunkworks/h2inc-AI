
class H2INC_AI:
    def __init__(self, name):
        self.name = name
        self.Version = "0.0.2"
        self.Copyright = "Copyright (c) 2023"
        self.Author = "Jan Lerking"
        self.Contact = "github.com/Lerking"
        
    def getVersion(self):
        return self.Version
    
    def getAuthor(self):
        return self.Author
    
    def getContact(self):
        return self.Contact
    
    def getCopyright(self):
        return self.Copyright

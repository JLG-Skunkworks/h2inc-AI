
class H2incAi:
    """_summary_
    """
    def __init__(self, name):
        self.name = name
        self.ai_version = "0.0.4"
        self.ai_copyright = "Copyright (c) 2023"
        self.ai_author = "Jan Lerking"
        self.ai_contact = "github.com/Lerking"
        
    def get_version(self):
        """_summary_"""
        return self.ai_version
    
    def get_author(self):
        """_summary_"""
        return self.ai_author
    
    def get_contact(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        return self.ai_contact
    
    def get_copyright(self):
        """_summary_"""
        return self.ai_copyright

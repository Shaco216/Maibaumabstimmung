

class HTML_SearchEngine:
    _multipleValues = False
    _tag = {"class_" : 1,"ID" : 2, "a" : 3}
    _Html_Code = ""

    def __init__(self,Html_Code, MultipleValues):
        self._Html_Code = Html_Code
        self._multipleValues = MultipleValues

    def choose_Tag(self, Tag):
        return self._tag.value(Tag)

    def search_for(self,What_do_you_search):
        if(self._multipleValues == True):
            for item in self._Html_Code.findAll(class_="col-12 col-md-8 px-2 flex-column"):
                
        else:
            pass
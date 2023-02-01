

class HTML_SearchEngine:
    _multipleValues = False
    _tag = { 1 : "class_", 2 : "ID", 3 : "a"}
    _Html_Code = ""
    _chosen_Tag = 0
    _results = None
    _filtered_results = None

    def __init__(self,Html_Code = "", MultipleValues = False):
        self._Html_Code = Html_Code
        self._multipleValues = MultipleValues

    def choose_Tag(self, Tag):
        self._chosen_Tag = self._tag.get(Tag)

    def search_for(self,What_do_you_search):
        Result_List = []
        if self._multipleValues == True:
            if self._chosen_Tag == 1 or self._chosen_Tag == "class_":
                for item in self._Html_Code.findAll(class_=What_do_you_search):
                    Result_List.append(item)
            elif self._chosen_Tag == 2 or self._chosen_Tag == "ID":
                for item in self._Html_Code.findAll(ID=What_do_you_search):
                    Result_List.append(item)
            elif self._chosen_Tag == 3 or self._chosen_Tag == "a":
                for item in self._Html_Code.findAll(a=What_do_you_search):
                    Result_List.append(item)
            self._results = Result_List
            return Result_List
        else:
            if self._chosen_Tag == 1 or self._chosen_Tag == "class_":
                self._results = self._Html_Code.find(class_=What_do_you_search)
                return self._Html_Code.find(class_=What_do_you_search)
            elif self._chosen_Tag == 2 or self._chosen_Tag == "ID":
                self._results = self._Html_Code.find(class_=What_do_you_search)
                return self._Html_Code.find(class_=What_do_you_search)
            elif self._chosen_Tag == 3 or self._chosen_Tag == "a":
                self._results = self._Html_Code.find(class_=What_do_you_search)
                return self._Html_Code.find(class_=What_do_you_search)

    def set_HTML_Code(self,Html_Code):
        self._Html_Code = Html_Code

    def show_current_results(self):
        if len(self._results) > 0 and self._filtered_results is None:
            print(self._results)
        else:
            print(self._filtered_results)

    def filter_to_only_text(self):
        if type(self._results) is list:
            self._filtered_results = []
            for item in self._results:
                self._filtered_results.append(item.text)
        else:
            self._results = self._results.text

    def change_multiple_values(self, trueORfalse):
        self._multipleValues = trueORfalse

    def get_current_results(self):
        if len(self._results) > 0 and self._filtered_results is None:
            return self._results
        else:
            return self._filtered_results
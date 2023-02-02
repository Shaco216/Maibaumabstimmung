

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

    def show_filtered_results(self):
        return self._filtered_results
    def show_unfiltered_results(self):
        return self._results

    #What_do_you_search können auch gemeinsame merkmale sein zb href mit /wiki/[unterschiedliche namen]
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
                templist = []
                for item in self._Html_Code.findAll('a'):
                    templist.append(item.get('href'))
                Result_List = [item for item in templist if What_do_you_search in str(item)] #get substring What_do_you_search from items
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

    def filter_all_hrefs(self, words_to_filter_for):
        #Creating a negative list
        Result_List = []
        Final_result = []
        #Removing words by checking item by item inside list
        if len(self._results) > 0 and self._filtered_results is None:
            Result_List = self._results
            for word in words_to_filter_for:
                counter = 0
                for item in self._results:
                    if word in str(item):
                        Result_List[counter] = "0"
                    counter = counter + 1
            #Hinzufügen aller items die nicht 0 als wert haben
            for res in Result_List:
                if res != "0":
                    Final_result.append(res)
        else:
            Result_List = self._filtered_results
            for word in words_to_filter_for:
                counter = 0
                for item in self._filtered_results:
                    if word in str(item):
                        Result_List[counter] = "0"
                    counter = counter + 1
            #Hinzufügen aller items die nicht 0 als wert haben
            for res in Result_List:
                if res != "0":
                    Final_result.append(res)
        self._filtered_results = Final_result

    def set_filtered_results(self, filtered_results):
        self._filtered_results = filtered_results

    def set_results(self, results):
        self._results = results

    def replacing_all_targeted_characters_in_hrefs_with_one_desired_character(self, character_or_words_list, desired_character_or_word):
        Result_list = []
        if len(self._results) > 0 and self._filtered_results is None:
            for item in self._results:
                for word in character_or_words_list:
                    if word in str(item):
                        Result_list.append(item.replace(word,desired_character_or_word))
        else:
            for item in self._filtered_results:
                for word in character_or_words_list:
                    if word in str(item):
                        Result_list.append(item.replace(word,desired_character_or_word))
        self._filtered_results = Result_list




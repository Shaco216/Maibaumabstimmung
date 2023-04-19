import csv

class CSV_Creator:
    _source = {}
    _path = ""
    _filename = ""
    _list = False
    _dict = False
    _fieldnames = []

    def __init__(self, path=""):
        self._path = path

    def load_source_as_list(self, sourceAsList):
        parentlist = []
        testlist = []
        for i in sourceAsList:
            testlist.append(i)
            parentlist.append(testlist)
            #testlist.remove(i)
        self._source = parentlist
        #print(self._source)
        self._list = True
        self._dict = False


    def set_fieldnames(self, fieldnames):
        self._fieldnames = fieldnames

    def load_source_as_dict(self, sourceasDict):
        #self._source = {}
        self._source = sourceasDict
        self._dict = True
        self._list = False

    def change_path(self,path):
        self._path = path

    def set_filename(self, filename):
        self._filename = filename + ".csv"

    def build_csv_file(self):
        with open(self._path+self._filename, 'a', newline='') as file:
            if self._list == True and self._dict == False:
                writer = csv.writer(file,delimiter=';')
                #writer.writerows(self._source)
                for row in self._source:
                    writer.writerow(row)
            elif self._list == False and self._dict == True:
                #recreate dict
                old_keys = [str(self._fieldnames[0])]
                old_values = [str(self._fieldnames[1])]
                for key in self._source:
                    old_keys.append(key)
                    old_values.append(self._source[key])
                newdict = dict(zip(old_keys,old_values))
                #{self._fieldnames[0]:str(old_keys),self._fieldnames[1]:str(old_values)}
                print(old_keys)
                print(newdict)

                writer = csv.DictWriter(file, newdict.keys(),delimiter=';')
                writer.writeheader()
                #for data in newdict:
                #    writer.writerows(data)
                writer.writerow(newdict)

                #writer = csv.writer(file)
                #for key, value in self._source.items():
                    #writer.writerow([key, value])
                #for data in self._source:
                #    writer.writerow(data)
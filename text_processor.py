class TextProcessor(object):

    def get_clean_string(self, text):
        str = ''
        for element in text:
            if self.__is_punktiantian(element):
                next
            else:
                str = str + element
        return str
    
    def __is_punktiantian(self, element):
        result = False
        if element in [',', ':', '.', '!', ' ']: result = True
        return result

    
class TextLoader(object):

    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = ''
    
    def set_clean_text(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def show_result(self):
        print(self.__clean_string)

    
class DataInterface(object):
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, rows_list):
        for row in rows_list:
            self.__text_loader.set_clean_text(row)
            self.__text_loader.show_result


a = DataInterface()
a.process_texts([
    'askjdakjdshkjhn , sdkchbkhb ! dsncmnsdc. ',
    'asdasd: sdcdsc, asd, asf, asd'
])

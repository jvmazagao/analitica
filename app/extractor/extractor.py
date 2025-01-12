from parsers.parser import SingleLineParser, DoubleLineParser, FourLineParser, SixLineParser

class Extractor:
    def __init__(self, data = {}):
        self.data = data
        self.parsers = [SingleLineParser(), DoubleLineParser(), FourLineParser(), SixLineParser()]
    
    def extract(self, elements):
        for parser in self.parsers:
            if parser.is_valid(elements):
                return parser.parse(elements, self.data)
        
        return self.data
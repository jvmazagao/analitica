from abc import ABC, abstractmethod

class Parser(ABC):
    def __init__(self, size):
        self.size = size
    
    @abstractmethod
    def parse(self, data):
        pass
    
    def is_valid(self, elements):
        return len(elements) == self.size
    
    def clean_key(self, key):
        return key.lstrip('?')
    
class SingleLineParser(Parser):
    def __init__(self):
        super().__init__(1)
        
    def parse(self, keys, data: dict):
        key = self.clean_key(keys.pop())
        data.update({key: {}})
        return data
    
class DoubleLineParser(Parser):
    def __init__(self):
        super().__init__(2)
    
    def parse(self, elements, data: dict):
        key_1, key_2 = [self.clean_key(x) for x in elements]
        if key_1 == 'Últimos 12 meses':
            data['Dados demonstrativos de resultados'][key_1] = {}
            data['Dados demonstrativos de resultados'][key_2] = {}
        else: 
            data[key_1] = {}
            data[key_2] = {}
        return data
    
class FourLineParser(Parser):
    def __init__(self):
        super().__init__(4)
    
    def parse(self, elements, data: dict):
        for i in range(0, 4, 2):
            key, value = self.clean_key(elements[i]), elements[i+1]
            if 'Dados demonstrativos de resultados' in data:
                if i == 0:
                    data['Dados demonstrativos de resultados']['Últimos 12 meses'][key] = value
                else: 
                    data['Dados demonstrativos de resultados']['Últimos 3 meses'][key] = value
            if 'Dados Balanço Patrimonial' in data:
                data['Dados Balanço Patrimonial'][key] = value
            else:
                data[key] = value
        return data

class SixLineParser(Parser):
    def __init__(self):
        super().__init__(6)
    
    def parse(self, elements, data: dict):
        for i in range(0, 6, 2):
            key, value = self.clean_key(elements[i]), elements[i+1]
            if i == 0:
                data['Oscilações'][key] = value
            else:
                data['Indicadores fundamentalistas'][key] = value
        return data

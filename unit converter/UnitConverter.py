from msilib.schema import Class
class UnitConverter:
    def __init__(self, unit_from, unit_to, value_from):
        self.unit_from = unit_from
        self.unit_to = unit_to
        self.value_from = value_from


    # methon for convert Centimeter to other
    def __centimeter_converter(self):
        if self.unit_to == 'Centimeter':
            return self.value_from
        elif self.unit_to == 'Kilometer':
            return (self.value_from / 100) / 1000
        elif self.unit_to == 'Meter':
            return self.value_from / 100

    # methon for convert Meter to other
    def __meter_converter(self):
        if self.unit_to == 'Centimeter':
            return self.value_from * 100
        elif self.unit_to == 'Kilometer':
            return self.value_from  / 1000
        elif self.unit_to == 'Meter':
            return self.value_from
    
    # methon for convert Kilometer to other
    def __kilometer_converter(self):
        if self.unit_to == 'Centimeter':
            return (self.value_from * 1000) * 100
        elif self.unit_to == 'Kilometer':
            return self.value_from
        elif self.unit_to == 'Meter':
            return self.value_from * 1000

    # method for convert
    def convertor(self):
        if self.unit_from == 'Centimeter':
            return self.__centimeter_converter()
        elif self.unit_from == 'Meter':
            return self.__meter_converter()
        elif self.unit_from == 'Kilometer':
            return self.__kilometer_converter()
        
        
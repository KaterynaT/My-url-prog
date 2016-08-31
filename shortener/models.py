from django.db import models
import string

abc = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def index_to_char(sequence):
    return "".join([abc[x] for x in sequence])
    
class Tableurl(models.Model):
    link = models.URLField()
    shortlink = models.URLField(default='')
    
    
     
    def get_short_id(self):
        _id = self.id
        digits = []       
        while _id > 0:
            rem = _id % len(abc)
            digits.append(rem)
            _id = _id//len(abc)
        digits.reverse()
        return index_to_char(digits)
        
    @staticmethod
    def decode_id(string):
        strlen = len(string)
        i = 0
        idx = 0
        for c in string:
            power = (strlen - (idx + 1))
            i += abc.index(c) * (len(abc) ** power)
            idx += 1
        return i



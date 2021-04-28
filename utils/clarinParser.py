from entities.clarinEntity import ClarinEntity
from utils.arrayUtils import checkArrayIndex

def parseText(value, separator):
    parsedValue = value.split(separator)
    entity = ClarinEntity()
    entity.header =  parsedValue[1] if checkArrayIndex(1, parsedValue) else ""
    entity.contents =  parsedValue[2] if checkArrayIndex(2, parsedValue) else ""
    
    return entity
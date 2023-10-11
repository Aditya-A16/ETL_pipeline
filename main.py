import extractor
import transform
import load

#driver function
if __name__ == 'main':
    extractor.extract()
    transform.transform()
    load.load()

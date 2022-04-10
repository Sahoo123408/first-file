import re
from collections import Counter
text = """We test coders. Give us a try? Most welcome coder and having fun!this is really fun fun fun .Beautiful, is;better*than\nugly"""

sentences = re.split(r' *[\.\;\n\?!][\'"\)\]]* *',text)

for stuff in sentences:
    
    d = stuff.split()
    s = set(d)
    
    def repeated_words(stuff):
        words = stuff.split(' ')
        dict = Counter(words)
        
        for key in words:            
            if dict[key]>0:               
                print(stuff+"|"+str((len(s)))+"|"+str(d.count(key)))
                return      
    if __name__== "__main__":
        repeated_words(stuff)

    

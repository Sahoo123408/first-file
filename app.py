import re

String = """We test coders. Give us a try? Most welcome coder and having fun!this is really fun fun fun .Beautiful, is;better*than\nugly"""

def Parse_paragraph(String):
    for k in re.split('\.|\?|!|;|\n',String):
        temp_dict = {}
        for word in k.split():
            if word in temp_dict:
                temp_dict[word] +=1
            else:
                temp_dict[word] = 1
                
        if len(temp_dict) > 0 :
            max_val = max(temp_dict.values())
            line = k.strip()+'|'+str(len(temp_dict))+'|'+str(max_val)
            print(line)

def main():
    Parse_paragraph(String)

if __name__== "__main__":
    main()

#modified version

    

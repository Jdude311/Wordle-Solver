import re
open("mostcommon5.txt","w").writelines([ word.lower() for word in open("mostcommon.txt") if len(word) == 6 and re.match("^[A-Za-z]*$", word)])
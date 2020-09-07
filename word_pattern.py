class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        str_list = str.split(" ");

        if(len(pattern) != len(str_list)):
           return False;
        patdic , strdic = {},{};
        for pat,st in zip(pattern,str_list) :
          if(pat not in patdic):
             patdic[pat] = st;
          if(st not in strdic):
             strdic[st] = pat;
          if(patdic[pat]!=st or strdic[st]!=pat):
             return False;    
        return True;    
        
 

class ascOps():
    '''def_init_(self):
        pass'''
    self.return=None
    def asc(self,string):
        
        try:
            dict_={}
            for i in string:
                dict_.update({i:ord(i)})
            return dict_    
        except Exception as e:
            return (e,None)
        pass
    def upper_():
        pass

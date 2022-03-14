class Process:
    def __init__(self):
        self._get_table = {}
        self._post_table = {}
        self.cache = {}
    
    def get(self,request):
        try:
            return self.cache[request]
        except KeyError:
            self.cache[request] = self._get_table[request]()
            return self.cache[request]   
    
    def post(self,request,*args):
        return self.post_args_transfom( self._post_table[request] , args)
    
    def post_args_transfom(self,method,args):
        raise NotImplementedError 

    def add_get(self,name,method):
        self._get_table[name] = method
    
    def add_post(self,name,method):
        self._post_table[name] = method
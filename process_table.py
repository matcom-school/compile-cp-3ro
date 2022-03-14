from process_library import LL1_Process,FAF_Process
class ProcessTable:
    def __init__(self):
        self.table ={
                        "LL1" : LL1_Process.new_istance,
                        "FAF" : FAF_Process.new_istance
                    }
    
    def get_new_process(self,name,process):
        pass

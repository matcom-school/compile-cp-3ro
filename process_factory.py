from process_table import ProcessTable

class ProcessFactory(ProcessTable):
    def __init__(self):
        ProcessTable.__init__(self)

    def __call__(self,process):
        assert type(process) == type(str()), "ProcessFactory need a string"
        return self.table[process]



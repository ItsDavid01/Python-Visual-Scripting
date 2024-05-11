class On_Start():
    def __init__(self):
        self.i_flow = True
        self.o_flow = self.i_flow
    
class On_Update():
    def __init__(self):
        self.o_flow = True
        
class cycle():
    def __init__(self):
        self.i_flow = True
        self.o_flow = self.i_flow

class float_literal():
    def __init__(self):
        self.o_value = 0.0
        
class string_literal():
    def __init__(self):
        self.o_value = ""
        
class print():
    
    def __init__(self):
        self.i_value = None
        
class branch():
    def execute(self):
        while self.i_flow == False:
            pass
        if self.i_condition == True:
            self.o_true_flow == True
            self.o_false_flow == False
        else:
            self.o_true_flow == False
            self.o_false_flow == True
            
    def __init__(self):
        self.i_flow = False
        self.o_true_flow = False
        self.o_false_flow = False
        self.i_condition = None
        
        
    
        
        
    
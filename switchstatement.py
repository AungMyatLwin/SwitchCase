class SwitchStatement:
    #default constructors
    def __init__(self):
        self.dics={}

    # declaring or creating number of index in dict
    def case_number(self,num):
        self.dics={x:'' for x in range(num)}
        print(self.dics)
    
    #conditions to put in case 
    def case(self,index,cond):
        # try if eval(cond) is integer
        try:
            if isinstance(eval(cond), int):
                self.dics[index]=eval(cond)
                print(self.dics)

        # except if return string      
        except:
            self.dics[index]=cond
            print(self.dics)

           
    # get both keys and values to check datas
    def getKeys(self):
        for k,v in self.dics.items():
            print(k," : ",v)
    
    # switch(condition)
    def switch(self,num):
        s=''
        if num in self.dics.values():
            print(num)
            s=num
        else:
            s=self.dics.get("default")
            print(s)
        return s

    def default(self,condition):
        self.dics["default"]=condition
    # clearing dictionary 
    def clearingClear(self):
        self.dics.clear()
        print(self.dics)
                


# s is the instance of SwitchStatement
s=SwitchStatement()
# switch(conditions)
s.switch("2+3")

s.getKeys()
#adding cases
s.case("+","2+3")
s.case("/","2-2")
# default : statement break;
s.default("help")


s.getKeys()


s.switch("a")
s.switch(0)



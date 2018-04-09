import json

class reportingModule:
    #test tuple to create JSON object
    #box num, class, num, accuracy
    def __init__(self, tuples):
        self.results = []
        for frame in tuples:
            temp = {}
            temp["num_Bugs"] = frame[0]
            temp["accuracy"] = frame[1]
            temp["class"] = frame[2]
            self.results.append(temp)
        
 

def main():
    test = [(4, 92, 3),(5,85,3),(6,82,3)] 
    print(reportingModule(test).results) 

main()

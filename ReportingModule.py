import json

class reportingModule:
    #test tuple to create JSON object
    #box num, class, num, accuracy
    def __init__(self, tuples): 
        self.results = {}
        for i in range(len(tuples)): #puts the data dictionary (temp) into the dictionary (results)
            temp = {}
            temp["num_Bugs"] = tuples[i][0]
            temp["accuracy"] = tuples[i][1]
            temp["class"] = tuples[i][2]
            self.results[i] = temp
        
 
    def convert2Json(self): # changes key of overall dictionary to string
        return (json.dumps(self.results))
    
    def trashMan(self): # deletes any tuples(Frames) that are irrelevent   
        for i in range(len(self.results)):
            # thow out guesses not the frame
            if self.results[i]["accuracy"] < 60: 
                del self.results[i]
            # checks to see if any bugs were detected on screen 
            elif self.results[i]["num_Bugs"] < 1:
                del self.results[i]
            
def main():
    # classification = classify()   toHTML(classification)
    test = [(4, 92, 3),(5,50,3),(6,82,3),(0,0,0)]
    report = reportingModule(test)
    report.trashMan()
    print(report.convert2Json())

main()

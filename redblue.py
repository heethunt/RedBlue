"""
Expected Value Exercise

Simulation to support my mathematical answer to expected value question posed on linkedin. 

q: given an urn filled with 3 balls (2 red and 1 blue to start), if you were to pick a ball at random and replace it with a blue ball blindly, how many draws could you expect to make before all balls in the urn are blue

mathematical answer = expected draws at start condition = 3 
expected draws to reach r-1 = (r+b)/r = 3/2 = 1.5
3+1.5 = 4.5

if correct, simulation will show a geometric distribution with an arithmetic mean(expected value) of ~4.5 for large runs. 

change log
---------------
JUNE 27 2024: original authorship by Heather Hunt
"""
import matplotlib.pyplot as plt
import statistics as st
import numpy as np

runs= 100000
red= 0 
blue= 1

neededDraws = []

count = 0 
#perform x iterations as stored in runs var - store number of draws needed to turn entire urn blue in the neededDraws array for graphing 
for _ in range(runs): 
    #starting state of urn is always 2 r 1 b. array may be expanded or altered for different use cases. if altering colors or adding colors, ensure the while loop condition is updated along with the setting urn value internal to urn. additional color values may be added to top var declarations for readability
    urn = np.array([red,red,blue])
    
    #check if urn contains any red. If red exists, we continue
    while (red in urn): 
        #generate a random number between 0-2. This will be the index of the ball drawn in urn.Replace with blue
        urn[np.random.randint(3, size=1)[0]] = blue
        #add to count
        count+= 1
 
    #save count to neededDraws and reset 
    neededDraws.append(count)
    count = 0
    
#convert result list to np array formplots and calculations
results= np.array(neededDraws)    

#plot results
unique, frequency = np.unique(results, 
                              return_counts = True)
                                                          

plt.bar(unique,frequency)
plt.title("Draws needed to turn all in urn blue")
plt.xlabel("draws needed")
plt.ylabel("frequency")
plt.xticks(np.arange(min(unique), max(unique)+1, 2))

plt.show()

print("Mean (aka expected value):" , np.mean(results))
print("Median:", np.median(results))
print("Mode:", st.mode(results) )
print("Runs performed:", runs)




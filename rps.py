from random import randint
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
n=1
cw1=0
tie=0
cw2=0

# Model 1
h1=[1,2,2,3,1]
input_data1=[[1,1,1,1,1],[2,2,2,2,2],[3,3,3,3,3]]
output_data1=[1,2,3]
model1=SVC()
model1.fit(input_data1,output_data1)

# Model 2
h2=[1]
input_data2=[[1],[2],[3]]
output_data2=[1,2,3]
model2=PassiveAggressiveClassifier()
model2.fit(input_data2,output_data2)


try:
    while True:
        print(f'Game {n}')
        n+=1
        c1=((model1.predict([[h1[-5],h1[-4],h1[-3],h1[-2],h1[-1]]])[0])%3)+1
        c2=((model2.predict([[h2[-1]]])[0])%3)+1
        if c1==c2:
            print('Tie')
            tie+=1
        elif (c1,c2)==(3,2) or (c1,c2)==(2,1) or (c1,c2)==(1,3):
            print('Computer 1 wins')
            cw1+=1
        else:
            print('Computer 2 wins')
            cw2+=1
        h1.append(c2)
        h2.append(c1)
        input_data1.append([h1[-6],h1[-5],h1[-4],h1[-3],h1[-2]])
        output_data1.append(h1[-1])
        input_data2.append([h2[-2]])
        output_data2.append(h2[-1])
        model1.fit(input_data1,output_data1)
        model2.fit(input_data2,output_data2)
except KeyboardInterrupt:
        print()
        print(f'Total: {cw1+cw2+tie}')
        print(f'Computer 1: {cw1}') 
        print(f'Computer 2: {cw2}') 
        print(f'Ties: {tie}') 
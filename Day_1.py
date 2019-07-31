# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print (8)
print(5*2)
print(5/2)
print(5**2)
print(8/9*3)
5-2
5*2
8/9*3

def multiply (a,b):
    multiply = a*b 
    
    print(multiply)
    
multiply(4,5)


def add(a,b,c):
    add = a+b+c
    
    print(add)
    

add(9,8,9)

def triangle(base,height):
    triangle = 1/2 * base * height
   
    print("The area of the triangle with", base ,"and", height ,"is", triangle)
    
triangle(12,5)

def caburybox(a,b):
    caburybox=a+b
    
    print(caburybox)
  
caburybox(15,5)

a = "Milk Chocolate"
b = "Dark Chocolate"
c = "White Chocolate"
    
print(a,b,c)
  
print ("Hello Kaya")  

a = "Kaya"
print("Hello",a)

name = input("please enter your name")
print("Your name is", name)

age = input("please enter your age")
print("Thanks.", "You enetered", age)

ageint = int(age)
ageint

ageint = float(age)

import math

dir (math)

math.pi

math.pow(6,15)

def cuberoot(a):
    print("The cubic root of",a, "is", math.pow(a,(1/3)))
    
    cuberoot(16)
    
    import math
    a=int(input("Enter a value"))
    
    def cadbury (a):
        cadbury= math.pow(a,1/3)
        print("The cubic root of", a, "is", cadbury)
        
        cadbury(a)
        
        DarkChoc = 5
        WhiteChoc = 8
        MilkChoc = 6
        
        print("There is", DarkChoc, "dark choclates", WhiteChoc, "white choclates", "and", MilkChoc, "milk choclates.")

studentage={"Steve":32,"Lia":28,"Vin":45,"Katie":48}
studentage

studentlist=[['steve',32, 'M'] ,["lia",28,"F"],["vin",45,"M"], ["Katie",38, "F"]]
studentlist

import pandas    
dir(pandas)    
    
studentdf=pandas.DataFrame(studentlist,columns=("Name","Age","Gender"))
studentdf

studentdf["Name"]
studentdf["Age"]
studentdf["Gender"]

import pandas
dir(pandas)

chocbox=[["milk",5],["dark",6],["white",8]]

chocboxdf= pandas.DataFrame(chocbox,columns=("Choclate","Quantity"))
print (chocboxdf)

chocboxdf["Choclate"]
chocboxdf["Quantity"]

studentlist = [["steve",32,"m"],["lia",28,"f"], ["vin",45,"m"], ["katie",38,"f"]]
studentlist

import pandas

studentdf = pandas.DataFrame(studentlist,columns=("name", "age", "gender"))
studentdf

studentdf2= pandas.DataFrame(studentlist,columns=("name", "age", "gender"),index=["1","2","3","4"])
studentdf2

import plotly
dir(plotly)
from plotly.offline import plot
import plotly.graph_objs as go  

studentbar=go.Bar(x=studentdf["name"],y=studentdf["age"]) 
plot([studentbar])

import plotly
from plotly.offline import plot
import plotly.ggraph_objs as go

chocbar =go.Bar(x=chocboxdf["Choclate"],y=chocboxdf["Quantity"])
plot([chocbar])

titles = go.Layout(title = "Number of Choclates by type")

chocbar =go.Bar(x=chocboxdf["Choclate"],y=chocboxdf["Quantity"])

fig = go.Figure(data=[chocbar], layout=titles)
plot(fig)

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 15:40:02 2020

@author: smitha
"""
import random;
from sys import exit;

list1=open("fruit.txt", 'r').readlines();
list2=open("animals.txt", 'r').readlines();
list3=open("weather.txt", 'r').readlines();
list4=open("countries.txt", 'r').readlines();
list5=open("olympicsports.txt", 'r').readlines();
Dict = {1:list1 , 2:list2, 3:list3, 4:list4, 5:list5};
visited=[];
score = 0;
print("\nWELCOME TO HANGMAN! CHOOSE YOUR CATEGORY :");
cat=0;
def main(list):
    global score, visited;
    word = random.choice(list);
    word=word.lower().rstrip();
    ans="";
    count = 7;
    cor = 0;
    for i in range(0,len(word),1):
       ans = ans + " _";
    if " " in word:
        a = word.find(" ");
        a=a*2+1;
        ans = ans[:a]+" "+ans[a+1:];
        cor = cor+1;
    print("Your word: " + ans + "\n");
    visited.clear();
    while count>0 and cor < len(word):
        print("No of lives remaining: "+ str(count) + "\nYour word : " + ans);
        c = input("Guess a letter :");
        if c.isalpha():
            c = c.lower();
            if c in visited :
                print("This letter has already used\n")
                continue;
            visited.append(c);
            if c in word and c not in ans:
                for i in range(0,len(word),1):
                    if word[i] == c:
                        i=i*2+1;
                        ans = ans[:i]+c+ans[i+1:];
                        cor = cor +1;
                print(ans.strip()+"\n");
            else : 
                print(c + " not found\n");
                count = count-1;
        else:
            print("Input an alphabet");
    if count <= 0:
        print("\nGame over. The word was "+word+"\nYour total score : " + str(score) + "\n");
        score=0;
        x1=int(input('Press:\n 1. Start game \n 2. Exit\n'));
        if x1 == 1 :
            categ();
        else :
            exit();
    else :
         score = score +1;
         print("Correct!\nYour score : " + str(score));
                
def categ() :       
    global cat;
    cat=int(input("Pick a category: \n1.Fruits and Vegetables\n2.Animals and Birds\n3.Weather\n4.Countries\n5.Olympic sports\n6.Exit\n"));
    if cat>6:
        print("Enter the correct choice");
    else:
        for i in range(1,6,1):
            if cat == i : 
                main(Dict[i]);
            if cat==6 :
                    exit();
   
categ();

while(1):
    x = int(input('Press:\n 1. Continue existing game \n 2. Change Category\n 3. Exit\n'));
    if x == 1:
     for i in range(1,6,1):
        if cat == i : 
            main(Dict[i]);
    elif x == 2:
        categ();
    elif x == 3: 
        exit();
    else :
        print('Enter the correct choice.\n');

 
        
        



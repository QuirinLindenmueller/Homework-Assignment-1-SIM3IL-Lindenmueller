# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 17:53:17 2020

@author: Quirin
"""

#Funktion zur Berechnung des größten gemeinsamen Teilers

def ggt(a,b):
    while a != b:
           if a<b:
               a,b=b,a
           a=a-b
    return a

#Funktion zur Addition zweier Brüche

def add_frac(Zaehler1,Nenner1,Zaehler2,Nenner2):
   
   if type(Zaehler1)!= int or type(Zaehler2)!= int or type(Nenner1)!= int or type(Nenner2) != int:
       print("Bitte für Zähler und Nenner nur ganze Zahlen angeben")
   if Nenner1 is 0 or Nenner2 is 0:
       print("Division durch 0 nicht möglich")
   
   else:
       #Variablen neu definieren zur für weniger Schreibarbeit
       z1=Zaehler1
       n1=Nenner1
       z2=Zaehler2
       n2=Nenner2
       #Beide Brüche auf gleichen Nenner bringen
       new_n1=n1*n2
       new_z1=z1*n2
       new_n2=n2*n1
       new_z2=z2*n1
       #Addition der Brüche
       new_z=new_z1+new_z2
       new_n=new_n1
       #Bestimmen des größten gemeinsamen Teilers
       a=ggt(new_z,new_n)
       #Küzen des Bruches
       new_z=int(new_z/a)
       new_n=int(new_n/a)
       print("Der Ergebnis-Bruch ist: ", new_z, "/", new_n)
       
       # return values as tuples
       return (new_z, new_n)

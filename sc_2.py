from __future__ import division
import winsound
import time
import math

def notesTofreq(a,length,factor=1):
   print "Notes function called"
   if len(a)<1:
      return False
   a=a.replace("|","")
   a=list(a)
   length=int(length)
   factor=float(factor)
   print "Now playing"
   if length>50:
      j=0
      while j<len(a):
         toPass=0

         reali=a[j]
         a[j]=a[j].lower()
               
         if a[j]=="a#":
            toPass=103.83
               
         if a[j]=="a":
            toPass=110.00
            
         if a[j]=="b#":
            toPass=123.47
            
         if a[j]=="b":
            toPass=116.54

         if a[j]=="c":
            toPass=130.81
            
         if a[j]=="c#":
            toPass=138.59
               
         if a[j]=="d":
            toPass=146.83
               
         if a[j]=="d#":
            toPass=155.56
               
         if a[j]=="e":
            toPass=164.81
            
         if a[j]=="e":
            toPass=164.81
            
         if a[j]=="f":
            toPass=174.61
               
         if a[j]=="f#":
            toPass=185.00
               
         if a[j]=="g":
            toPass=196.00
               
         if a[j]=="g#":
            toPass=207.65

         toPass=toPass*factor

         if reali!=a[j]:
            toPass=toPass*3

         if a[j]==" ":
            redudant=0
            time.sleep(float(float(str(length/1000))/3))
         elif a[j]!="p":

            
            if int(toPass)<37:
               print "Too low!"
            elif int(toPass)>32767:
               print "Too high!"
            else:
               print "Key: "+str(reali)+"\tFreq:"+str(int(toPass))
               winsound.Beep(int(toPass),length)
         else:
            print "zzzZZz.. Waiting for "+str(length/1000)+"s"
            time.sleep(float(str(length/1000)))
         j=j+1

def los():
   print "Commands:"
   cosd=raw_input("[['m' (merry christmas tune) or 'o' (sine wave) or 'l' (levels tune)]\ne.g: o\n\nor\n[Frequency (37-32767)|Duration (in milliseconds)|['s' or 'l' (as in lowercase 'L')]]\ne.g: 400|1000|l\n\nor\n['n'|Notes|SingleLength|Factor]]:\ne.g: n|aaa|250|1\n\n\nEnter Command here: ")
   j=0

   if cosd=="m":
         merry="1318|1396|1396|1396|1567|1760|1760|1760|1760|1567|1760|1975|1318|1567|1396|1046|1046|1760|1174|1046|1046|1975|1975|1975|1975|1567|1046|1975|1975|1760|1760|1318|1396|1396|1396|1567|1760|1760|1760|1760|1567|1760|1975|1318|1567|1396"
         k=0
         
         while k<2:
            j=0
            while j<len(merry.split("|")):
               winsound.Beep(int(merry.split("|")[j]),300)
               j=j+1
            k=k+1


            
   elif cosd=="o":
         j=0
         while j<100:
            sed=(math.sin(j^2)+2)*100
            if sed<37:
               sed=37
            elif sed>32767:
               sed=32767
               
            winsound.Beep(int(sed),100)
            j=j+1
            
            
   elif cosd=="l":

         notesTofreq("c# b e# f# e e e e e e e e d# d# ee",200,7)
         time.sleep(0.5)
         notesTofreq("c# b g# f# e e e e e e e e c# c# bb",200,7)         

   elif cosd.split("|")[0]=="n":
      fact=1
      if len(cosd.split("|"))>3:
         fact=cosd.split("|")[3]
      notesTofreq(cosd.split("|")[1],cosd.split("|")[2],fact)
            
   elif len(cosd.split("|"))<3 or cosd.split("|")[2]=="l":
         winsound.Beep(int(cosd.split("|")[0]),int(cosd.split("|")[1]))
            
   elif cosd.split("|")[2]=="s":
         while j<10:
            winsound.Beep(int(int(cosd.split("|")[0])/10*(j+1)),int(int(cosd.split("|")[1])/(j+1)))
            j=j+1

         while j>0:
            winsound.Beep(int(int(cosd.split("|")[0])/10*(j+1)),int(int(cosd.split("|")[1])/(j+1)))
            j=j-1

   los()
los()
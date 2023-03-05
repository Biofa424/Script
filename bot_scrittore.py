import os

try:
   os.remove("risultato.vbs")
except IOError:
    print("errore")

#primo parametro nome secondo come lo apri 
f=open("risultato.vbs","w")

#leggo i dati dal file da cui voglio prendere 
fdata=open("dati.txt","r")

f.write("set wshshell= wscript.createobject(\"wscript.shell\")\nwshshell.run \"notepad\"\n")
for x in fdata:

     for y in x:
         #controllo se c'è l'invio
         f.write("wscript.sleep 100\nwshshell.sendkeys \"") 
         if(y=="\n"):
             f.write("{ENTER}\"\n")
         else:
             f.write(y+"\"\n")

f.close()
fdata.close()


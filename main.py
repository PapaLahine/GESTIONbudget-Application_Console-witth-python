''' application console de Gestion de budget
1) enregistrer ses dépenses
3) enregistrer ses revenus
3) voir l'écart qui est entre ses dépenses et ses revenus
4) une dépense peut etre dans une catégorie(Loyer, Manger, Transport etc...)
5) une revenus peut etre dans une catégorie(Salaire, Business etc...)
6) utilisez un dictionnaire 
'''

import sqlite3 

with sqlite3.connect("Gestionbudget.db") as connection :
    cursor = connection.cursor()
    
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS revenu (id INTEGER PRIMARY KEY AUTOINCREMENT,salaire INT,business INT)"
        
        
        
    )
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS depense (id INTEGER PRIMARY KEY AUTOINCREMENT,loyer INT,manger INT,transport INT)"
    )





class Budget:
    def __init__(self):
        print("Application de Gestion de Budget ")

    def revenu(self):
        salaire=int
        business=int
        
        rev=""
        print('-----Choisissez le revenu-----')
        print('----- 1)Entrer votre salaire  -----')
        print('----- 2)Entrer votre Business  -----')
        rev=input("Que voulez vous entrer? \n")
        sal=cursor.execute(
            "INSERT INTO revenu (salaire,business) VALUES (?,false)", (salaire,)
            )
        connection.commit()
        connection.close()
        
        bus =cursor.execute(
            "INSERT INTO revenu (salaire,business) VALUES (false,?)", (business,)
            )
        connection.commit()
        connection.close()
        
        if rev=="1":
    
             print("Inserer votre salaire "+ sal)
        elif rev=="2":
              
              bus() 
              print("Inserer votre bussiness" + bus)
              
        else :
            print("veuillez entrer une valeur normale")  
            exit()      
               
    def depense(self) :
        loyer=int
        manger=int
        transport=int
        
        ly=cursor.execute(
            "INSERT INTO depense (loyer,manger,transport) VALUES (?,false,false)", (loyer,))
        connection.commit()
        mg=cursor.execute(
            "INSERT INTO depense (loyer,manger,transport) VALUES (false,?,false)", (manger,))
        connection.commit()
        
        tr=cursor.execute(
            "INSERT INTO depense (loyer,manger,transport) VALUES (false,false,?)", (transport,))
        connection.commit()
        choose=""
        print('-----Choisissez le nom du depense -----')
        print('----- 1)Entrer votre loyer  -----')
        print('----- 2)Entrer votre manger  -----')
        print('----- 3)Entrer votre transport  -----')
        choose=input("Que voulez vous entrer? \n")
        
        if choose=="1":
         loyer=input("entrer votre loyer")
         ly()
         print("operationn effectuee")
        elif choose=="2":
            manger=input("Entrer votre manger")
            mg()
            print("operationn effectuee")
            
        elif choose=="3":
            transport=input("Entrer votre transport")
            tr() 
            print("operationn effectuee")
        else :
            print("veuillez entrer une valeur normale")  
            exit()
            
    def Afficher_revenu(self) :
        cursor.execute (
            "SELECT * FROM revenu")
        
        rows=cursor.fetchall
        print(rows) 
        
        
    def Afficher_depense(self) :
        cursor.execute (
            "SELECT * FROM depense")
        
        rows=cursor.fetchall
        print(rows)     
          
          
        
               
                  
        
    def menu(self):
        choix=""
        print("_________ BIENVENU DANS VOTRE APPLICATION DE GESTION DE BUDGET ____________") 
        print("______ *** Choisissez l'operation que vous voulez faire***") 
        print( " 1) Entrer vos revenus ")
        print( " 2) Entrer vos depenses ") 
        print( " 3) Afficher les depenses ") 
        print( " 4) Afficher les revenus ") 
        print("  5) Quitter l'application ")
        choix=input('Entrer votre choix\n')
        
        if choix=="1":
            self.revenu()
        elif choix=="2":
            self.depense()
        elif choix== "3": 
            self.Afficher_depense() 
        elif choix=="4":
            self.Afficher_revenu()
        elif choix=="5":
            exit() 
            
        else:
            print("choix non reconnu")
            exit()     

app=Budget()
app.menu()                        
        
           
        
        
        
       
        
       
            
        
        
            
        
        
    
    

# # # ##1 VARIABLE
# # #  # # #prix=int(input("quel est le prix?"))
# # # #nb=int(input("combien d'articles avez vous?"))
# # # # #TVA=(prix*nb)*0.2
# # # # #print (TVA)
# # # # #total=(prix*nb)
# # # # # total=total+TVA
# # # # #print("le prix de votre article est de",prix,"€","vous en avez:",nb,"ce qui vous fait",total,"€","dont",TVA,"€ de TVA")

# # # # # # # # # # # # # # # # # # # # # # # # # # liste = [1,2,3,4,5,"lucas","test"]
# # # # # # # # # # # # # # # # # # # # # # # # # # print(liste)
# # # # # # # # # # # # # # # # # # # # # # # # # # print(liste[0])
# # # # # # # # # # # # # # # # # # # # # # # # # # print(type(liste[6]))

# # # # # # # # # # # # # # # # # # # # # # # # # x=[1,2,3,4]
# # # # # # # # # # # # # # # # # # # # # # # # # y=[5,6,7,8]
# # # # # # # # # # # # # # # # # # # # # # # # # z=[x+y]
# # # # # # # # # # # # # # # # # # # # # # # # # print(z)

# # # # # # # # # # # # # # # # # # # # # # # # x=[0,1,2,3,4,5,6,7,8,9]
# # # # # # # # # # # # # # # # # # # # # # # # print(x[3])
# # # # # # # # # # # # # # # # # # # # # # # # print(x[2:8:2])
# # # # # # # # # # # # # # # # # # # # # # # # print(len(x))
# # # # # # # # # # # # # # # # # # # # # # # # print(min(x))
# # # # # # # # # # # # # # # # # # # # # # # # print(max(x))
# # # # # # # # # # # # # # # # # # # # # # # # print(sum(x))
# # # # # # # # # # # # # # # # # # # # # # # # del(x[3:5])
# # # # # # # # # # # # # # # # # # # # # # # # print(x)

# # # # # # # # # # # # # # # # # # # # # # # x=["ok",4,2,78,"bonjour"]
# # # # # # # # # # # # # # # # # # # # # # # print(x[3])
# # # # # # # # # # # # # # # # # # # # # # # x[1]= "toto"
# # # # # # # # # # # # # # # # # # # # # # # print(x)

# # # # # # # # # # # # # # # # # # # # # # x=[0,1,2,3,4,5]

# # # # # # # # # # # # # # # # # # # # x = ["l","y","u","j"]
# # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # (x).append('a')
# # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # x.insert(5,'b')
# # # # # # # # # # # # # # # # # # # # print(x)



# # # # # # # # # # # # # # # # # # # # y= [1,2,3]
# # # # # # # # # # # # # # # # # # # # x.insert(6,y)
# # # # # # # # # # # # # # # # # # # # print(x)

# # # # # # # # # # # # # # # # # # # # x.insert(3,2)
# # # # # # # # # # # # # # # # # # # # print(x)

# # # # # # # # # # # # # # # # # # # # x.pop(3)
# # # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # # print(y)
# # # # # # # # # # # # # # # # # # # # z=(y)
# # # # # # # # # # # # # # # # # # # # print(z)
# # # # # # # # # # # # # # # # # # # # print(y)
# # # # # # # # # # # # # # # # # # # # #y.clear()
# # # # # # # # # # # # # # # # # # # # #print(y)
# # # # # # # # # # # # # # # # # # # # y.remove(1)
# # # # # # # # # # # # # # # # # # # # y.remove(2)
# # # # # # # # # # # # # # # # # # # # y.remove(3)
# # # # # # # # # # # # # # # # # # # # print(y)




# # # ###2 TESTS
# # # # # # # # # # # # # # # # # # # nb1=input("1er nombre:")
# # # # # # # # # # # # # # # # # # # print(nb1)
# # # # # # # # # # # # # # # # # # # nb2=input("2ème nombre:")
# # # # # # # # # # # # # # # # # # # print(nb2)
# # # # # # # # # # # # # # # # # # # x= int(nb1)+int(nb2)
# # # # # # # # # # # # # # # # # # # print(x)
# # # # # # # # # # # # # # # # # # # if x<0:print("le produit est négatif")
# # # # # # # # # # # # # # # # # # # elif x>0:print("le produit est positif")
# # # # # # # # # # # # # # # # # # # else:print("le produit est nul")

# # # # # # # # # # # # # # # # # # age=input("quel age avez vous?")
# # # # # # # # # # # # # # # # # # print(age)
# # # # # # # # # # # # # # # # # # if age>="18":print("vous etes majeur")
# # # # # # # # # # # # # # # # # # else:print("vous n'etes pas majeur")


# # # # # # # # # # # # # # # # # nb1=input("ecrivez un nombre:")
# # # # # # # # # # # # # # # # # print(nb1)
# # # # # # # # # # # # # # # # # if nb1>"5" or nb1<"10" :print("vrai")
# # # # # # # # # # # # # # # # # else:print("faux")



# # # ##3BOUCLES
# # # # # # # # # # # # # # # # for a in[0,1,2,3,4,5]:
# # # # # # # # # # # # # # # #     print(a)

# # # # # # # # # # # # # # # a=["lucas","test","oui"]
# # # # # # # # # # # # # # # for x in a:
# # # # # # # # # # # # # # #     print(x)
# # # # # # # # # # # # # # #     print(len(x))
    

# # # # # # # # # # # # # # x="anticonstitutionnelement"
# # # # # # # # # # # # # # for a in x:
# # # # # # # # # # # # # #     print(a)


# # # # # # # # # # # # # x=[[1,2,3],[4,5,6],[7,8,9]]
# # # # # # # # # # # # # for a in x:
# # # # # # # # # # # # #     print(a)
# # # # # # # # # # # # # print(x)

# # # # # # # # # # # # x=[1,10,20,30,40,50]
# # # # # # # # # # # # print(sum(x))

# # # # # # # # # # # x=[1,10,20,30,40,50]
# # # # # # # # # # # total=0
# # # # # # # # # # # for i in x:
# # # # # # # # # # #     total=total+i
# # # # # # # # # # # print(total)

# # # # # # # # # # liste=[0,1,2,3,4,5]
# # # # # # # # # # for i in range(5,0,-1):
# # # # # # # # # #     print(i)
    
# # # # # # # # # liste=[1,2,3,4,5,6,7,8,9,10]
# # # # # # # # # c=4
# # # # # # # # # for i in range(1,10):
# # # # # # # # #     if i==c:
# # # # # # # # #         break
# # # # # # # # #     print(i)

# # # # # # # # liste =[1,2,3,4,5,6,7,8,9]
# # # # # # # # for elem in range(1,10):
# # # # # # # #     if elem==3:
# # # # # # # #       liste.remove(elem)
# # # # # # # # print(liste)


# # # # # # # ordi=["apple","asus","dell","samsung"]
# # # # # # # i=0
# # # # # # # while i<1:
# # # # # # #     print(ordi)
# # # # # # #     i=i+1

# # # # # # text=input("saisissez du texte:")
# # # # # # print(text)
# # # # # # while text!="exit":
# # # # # #     text=input("saisissez du texte:")
# # # # # #     print(text)

# # # # # i=0
# # # # # while i<=100:
# # # # #     print(i)
# # # # #     i=i+5


# # # ## 4 FONCTIONS 
# # # # def compteur (stop):
# # # #     i=(stop*5)
# # # #     print(i)

# # # # compteur(5) 

# # # def extract(L):
# # #     pair=[]
# # #     for x in L:
# # #         if(x%2==0):
# # #             pair.append(x)
# # #     print("tout les nombres pairs sont:",(pair))
# # # L=[12,5,25,30,14,62,85,42]
# # # print(extract(L))

# nb=input("saisissez un nombre")
# print(nb)
# def fib(n):
#     if n == 1 or n == 2:
#         return 1
#     else:
#         p = 1
#         c = 1
#         for i in range(n - 2):
#             s = p + c
#             p = c
#             c = s
#         return c
# for i in range(1,21):
#     if i<="nb":
#         break
    
#     print(fib(i))





# ###5 CLASSES
# # class Carre:
# #   count = 0
# #     def __init__(self, nb_cote, taille_cote):
# #         self.nb_cote = nb_cote
# #         self.taille_cote = taille_cote

# #     def calculate_perimeter(self):
# #       return self.nb_cote * self.taille_cote
    
# #     def calculate_area(self):
# #       return self.taille_cote * self.taille_cote

# #     def factor(self):
# #       return (self.nb_cote * self.taille_cote) * multi

# #     def count(self):
# #       return type(self)ct = count
# #         count += 1
    
# # 

# #     def int(self):
# #       return (self.nb_cote)

# #     def Comp(self):
# #       if self.taille_cote > C2.taille_cote2:
# #         print("True")
# #       else:
# #         print("False")
# # 

# # if __name__ == "__main__":

# #     a = int(input("Entrer Nombre de coter : "))
# #     b = int(input("Entrer Tailler des coter : "))
# #     d = int(input("Entrer Tailler des coter : "))

# #     C = Carre(a, b)
# #     C2 = Carre(a, d) 

# #     multi = int(input("Entrer : "))
# # #   multi2 = int(input("Entrer : "))

# #     print(C.nb_cote)
# #     print(C.taille_cote)
# #     print(C.calculate_perimeter())
# #     print(C.calculate_area())

# #     print(C2.nb_cote)
# #     print(C2.taille_cote)
# #     print(C2.calculate_perimeter())
# #     print(C2.calculate_area())
# #     print(C.count())

# #     print("Le carré n°1 est", multi, "fois plus grand, soit", C.factor(), "cm")
# #     print("Les cotés du carré ont une longueur de", C.taille_cote,"cm, une aire de", C.calculate_area(),"cm², et un périmètre de", C.calculate_perimeter(),"cm.")

# # 
# # class Carre2:
   
# #   def __init__(self, nb_cote2, taille_cote2):
# #     self.nb_cote2 = nb_cote2
# #     self.taille_cote2 = taille_cote2

# #   def calculate_perimeter2(self):
# #     return self.nb_cote2 * self.taille_cote2
  
# #   def calculate_area2(self):
# #     return self.taille_cote2 * self.taille_cote2

# #   def factor2(self):
# #     return (self.nb_cote2 * self.taille_cote2) * multi2
# #   print(C2.nb_cote2)
# #   print(C2.taille_cote2)
# #   print(C2.calculate_perimeter2())
# #   print(C2.calculate_area2())
# #   print(C.int())
# #   print(C.Comp())


# #   print("Le carré n°2 est", multi2, "fois plus grand, soit", C2.factor2(), "cm")
# #   print("Les cotés du carré ont une longueur de", C2.taille_cote2,"cm, une aire de", C2.calculate_area2(),"cm², et un périmètre de", C2.calculate_perimeter2(),"cm.")
  

# #   print("Les deux carré additionnés ont un périmètre de", C.calculate_perimeter() + C2.calculate_perimeter2(),"cm")
# #   print("Les deux carré soustrait ont un périmètre de", C.calculate_perimeter() - C2.calculate_perimeter2(),"cm")
# # 


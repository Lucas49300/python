
# # # # # # # # # # # # # # # # # # #prix=int(input("quel est le prix?"))
# # # # # # # # # # # # # # # # # # #nb=int(input("combien d'articles avez vous?"))
# # # # # # # # # # # # # # # # # # #TVA=(prix*nb)*0.2
# # # # # # # # # # # # # # # # # # #print (TVA)
# # # # # # # # # # # # # # # # # # #total=(prix*nb)
# # # # # # # # # # # # # # # # # # #total=total+TVA
# # # # # # # # # # # # # # # # # # #print("le prix de votre article est de",prix,"€","vous en avez:",nb,"ce qui vous fait",total,"€","dont",TVA,"€ de TVA")

# # # # # # # # # # # # # # # # # # liste = [1,2,3,4,5,"lucas","test"]
# # # # # # # # # # # # # # # # # # print(liste)
# # # # # # # # # # # # # # # # # # print(liste[0])
# # # # # # # # # # # # # # # # # # print(type(liste[6]))

# # # # # # # # # # # # # # # # # x=[1,2,3,4]
# # # # # # # # # # # # # # # # # y=[5,6,7,8]
# # # # # # # # # # # # # # # # # z=[x+y]
# # # # # # # # # # # # # # # # # print(z)

# # # # # # # # # # # # # # # # x=[0,1,2,3,4,5,6,7,8,9]
# # # # # # # # # # # # # # # # print(x[3])
# # # # # # # # # # # # # # # # print(x[2:8:2])
# # # # # # # # # # # # # # # # print(len(x))
# # # # # # # # # # # # # # # # print(min(x))
# # # # # # # # # # # # # # # # print(max(x))
# # # # # # # # # # # # # # # # print(sum(x))
# # # # # # # # # # # # # # # # del(x[3:5])
# # # # # # # # # # # # # # # # print(x)

# # # # # # # # # # # # # # # x=["ok",4,2,78,"bonjour"]
# # # # # # # # # # # # # # # print(x[3])
# # # # # # # # # # # # # # # x[1]= "toto"
# # # # # # # # # # # # # # # print(x)

# # # # # # # # # # # # # # x=[0,1,2,3,4,5]

# # # # # # # # # # # # x = ["l","y","u","j"]
# # # # # # # # # # # # print(x)
# # # # # # # # # # # # (x).append('a')
# # # # # # # # # # # # print(x)
# # # # # # # # # # # # x.insert(5,'b')
# # # # # # # # # # # # print(x)



# # # # # # # # # # # # y= [1,2,3]
# # # # # # # # # # # # x.insert(6,y)
# # # # # # # # # # # # print(x)

# # # # # # # # # # # # x.insert(3,2)
# # # # # # # # # # # # print(x)

# # # # # # # # # # # # x.pop(3)
# # # # # # # # # # # # print(x)
# # # # # # # # # # # # print(y)
# # # # # # # # # # # # z=(y)
# # # # # # # # # # # # print(z)
# # # # # # # # # # # # print(y)
# # # # # # # # # # # # #y.clear()
# # # # # # # # # # # # #print(y)
# # # # # # # # # # # # y.remove(1)
# # # # # # # # # # # # y.remove(2)
# # # # # # # # # # # # y.remove(3)
# # # # # # # # # # # # print(y)

# # # # # # # # # # # nb1=input("1er nombre:")
# # # # # # # # # # # print(nb1)
# # # # # # # # # # # nb2=input("2ème nombre:")
# # # # # # # # # # # print(nb2)
# # # # # # # # # # # x= int(nb1)+int(nb2)
# # # # # # # # # # # print(x)
# # # # # # # # # # # if x<0:print("le produit est négatif")
# # # # # # # # # # # elif x>0:print("le produit est positif")
# # # # # # # # # # # else:print("le produit est nul")

# # # # # # # # # # age=input("quel age avez vous?")
# # # # # # # # # # print(age)
# # # # # # # # # # if age>="18":print("vous etes majeur")
# # # # # # # # # # else:print("vous n'etes pas majeur")


# # # # # # # # # nb1=input("ecrivez un nombre:")
# # # # # # # # # print(nb1)
# # # # # # # # # if nb1>"5" or nb1<"10" :print("vrai")
# # # # # # # # # else:print("faux")

# # # # # # # # for a in[0,1,2,3,4,5]:
# # # # # # # #     print(a)

# # # # # # # a=["lucas","test","oui"]
# # # # # # # for x in a:
# # # # # # #     print(x)
# # # # # # #     print(len(x))
    

# # # # # # x="anticonstitutionnelement"
# # # # # # for a in x:
# # # # # #     print(a)


# # # # # x=[[1,2,3],[4,5,6],[7,8,9]]
# # # # # for a in x:
# # # # #     print(a)
# # # # # print(x)

# # # # x=[1,10,20,30,40,50]
# # # # print(sum(x))

# # # x=[1,10,20,30,40,50]
# # # total=0
# # # for i in x:
# # #     total=total+i
# # # print(total)

# # liste=[0,1,2,3,4,5]
# # for i in range(5,0,-1):
# #     print(i)
    
# liste=[1,2,3,4,5,6,7,8,9,10]
# c=4
# for i in range(1,10):
#     if i==c:
#         break
#     print(i)

liste=[1,2,3,4,5,6,7,8,9]
c=3
for i in range(1,10):
  if c==3:
     del(c) 
  print(i)


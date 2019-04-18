from random import randint
import math
shop1={"молоко":(7,40),"хлеб":(7,12),"сыр":(40,240),"колбаса":(30,40),"яблоко":(20,50),"слива":(25,30),"йогурт":(30,5),"вода":(7,1000),"мясо":(140,5),"картошка":(14,140)}
shop2=shop1.copy()
print(shop1)
shop2.pop("молоко")
shop2["пиво"]=(30,50)
shop2["вино"]=(250,450)
for i in shop2:
   shop2[i]=(randint(2,20),randint(10,80))
print(shop2)
input_list=input("Список покупок (через пробел):").split()
name_of_shop = "Маруся"
def health_buying(list):
   dict_to_return={}
   for i in input_list:
       if i in shop1.keys():
           shop1_product=shop1[i][1]
       else:
           shop1_product=0
       if i in shop2.keys():
           shop2_product=shop2[i][1]
       else:
           shop2_product=0
       if i not in shop1.keys() and i not in shop2.keys():
           dict_to_return[i]=("no","no")
       else:
           d=""
           shop=""
           if shop1_product>shop2_product:
               d=shop1[i]
               shop="shop1"
           else:
               d=shop2[i]
               shop="shop2"
           dict_to_return[i]=(shop,d)
       shop2_product=shop2[i][1]
   for i in dict_to_return:
       print(str(i).center(8),str(dict_to_return[i][1]).center(20),"     ",dict_to_return[i][0])
def cheaper_buying(list):
   dict_to_return={}
   for i in input_list:
       if i in shop1.keys():
           shop1_product=shop1[i][1]
       else:
           shop1_product=999
       if i in shop2.keys():
           shop2_product=shop2[i][0]
       else:
           shop2_product=999
       if i not in shop1.keys() and i not in shop2.keys():
           dict_to_return[i]=("no","no")
       else:
           d=""
           shop=""
           if shop1_product<shop2_product:
               d=shop1[i]
               shop="shop1"
           else:
               d=shop2[i]
               shop="shop2"
           dict_to_return[i]=(shop,d)
       shop2_product=shop2[i][1]
   for i in dict_to_return:
       print(str(i).center(8),str(dict_to_return[i][1]).center(20),"     ",dict_to_return[i][0])
health_buying(input_list)
print()
cheaper_buying(input_list)      
 
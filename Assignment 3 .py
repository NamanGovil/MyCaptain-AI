#Accessing Elements from a Tuple
tup1 = (1, 2, 3, 4, 5, 6, 7 )
print (tup1)
i = int(input("Which element you want to access?"))
print ("Requested Element - ", tup1[i])

#Deleting Dictionary Elements
test_dict = {"Arushi" : 22, "Anuradha" : 21, "Mani" : 21, "Haritha" : 21}
print ("The dictionary before performing remove is : " + str(test_dict))
del test_dict["Arushi"]
print ("The dictionary after remove is : ", test_dict)

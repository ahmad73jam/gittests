varaible1='string'
varaible2="first line \nsecound line"
print(varaible2)
varaible3="""line1
line2
line3
line4"""
print(varaible3)
address=r'c:\new\desktop'
print(address)
test1='persian'
test2='iran'
test3=test1+test2
print(test3)
number1=1000
number2=925
if number1 >= number2:
    print(number1)
    braket="python"
    print(braket[0])
    print(braket[-1])
    #marbut be tozihat ke dar nazar gerefte nemishavad
    new=braket[-6] + braket[-5] + "thon"
    print(new)
    braket1=braket[0:6]#az addade sevvom ham mishe estefade kard be shekle zir [0:10:2]ke inja 2 be manzure in ast ke reshtaro 1 dar miyan dar nazar begor ya age be jaye 2 ,1 bashe be manzure bar aks kardane reshtas
    print(braket1)#mige az paye sefr ta 5 ro benevis
    halge = 1
while halge < 5:
        print(halge**2)
        halge = halge + 1
index = 0
while index < 6:
    print("mohsen"[index])
    index = index + 1
name = "ahmad"
index1 = 0
while index1 < len(name):#len inja tedade huruf ra khodesh mishmare
        print(name[index1])
        index1 = index1 + 1
name1 = "iliya"
adad = -1
while adad >= -(len(name1)):
    print(name1[adad])
    adad= adad - 1
    if adad == -4:
        break #age sharte break faraham she dar in surat halge motavagef mishe

name2 = "1m4o5623hs*e-**-n"
name3 =""
index2 = 0
while index2 < len(name2):
    character = name2[index2]
    if character in "abcdefghijklmnpqrsduvwxvzo":#manzur az in ineke character dakhele in huruf bashe
        name3 = name3 + character
    index2 = index2 + 1
print(name3)


#html = "<html><body>@persianDevelopers</body></html>"
#index3 = 0
#data = ""
#in_tag = false
#while index3 < len(html):
    #char = html[index3]
    #if char == "<":
    #    start_index =index3
    #    in_tag = true
    #    if len(data) != 0:
    #        print(data)
    #        data = ""
    #elif char == ">":
    #    print(html[start_index:index3+1])
    #    in_tag = false
#    elif in_tag == false:
#        data = data + char
#    index3 = index3+1

name4 = "M..o...h..s..e..n"
new_name = ""
index4 = 0
while index4 < len(name4):
    char = name4[index4]
    if char == ".":
        index4 = index4+1
        continue#manzur az continue yani edame mide in halgaro yani mane az ejraye khate bade halge mishe yani paresh mikone be ebtedaye halge
    new_name = new_name + char
    index4 = index4+1
print(new_name)

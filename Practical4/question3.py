hourrate35 =40
hourrate60 =60
hourrate60above =80

workinghour = float(input("Enter Working hours:"))

if workinghour >=0 and workinghour<=35:
    print("Total salary   : RM",workinghour * hourrate35)
    print("Regular Pay    : RM",workinghour*hourrate35)
    print("Overtime pay   : Rm 0000.0")
elif workinghour>35 and workinghour<=60:
     print("Total salary   : RM",(35* hourrate35)+(workinghour-35)*hourrate60)
     print("Regular Pay    : RM",35*hourrate35)
     print("Overtime pay   : RM",(workinghour-35)* hourrate60 )
elif workinghour>60:
     print("Total salary   : RM",(35* hourrate35)+((workinghour-35)*hourrate60)+(workinghour-60)*hourrate60above)
     print("Regular Pay    : RM",35*hourrate35)
     print("Overtime pay   : RM",((workinghour-35)*hourrate60)+(workinghour-60)*hourrate60above)
else:
     print("Pls enter more than 0")
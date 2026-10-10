list_component = [("sandvistan", 1,23,"military", "high") , ("neuralhence", 2,10, "all", "mid") ]

load = 0
status = int(input("next"))

while status != 4:
  if status == 1:
    component = input("what to install")
    for item in list_component:
      if item[0] == component:
        load += item[2]
        print(f"{component}installed")
        status = int(input("continue?"))
        break
    else:
        print("component not found")
        status = int(input("continue?"))
  else:
      print("not coded yet")
print(f"workload: {load}")
  

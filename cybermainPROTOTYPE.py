#ntah saja buat alang ii free. ni byk pakai untuk show report
def make_bar(value):
  value = round(value/100*20)
  filledHash = value
  emptyHash = 20-value
  return f"[{filledHash*"#"}{emptyHash*"-"}]"
#ni pakai sekali je, and buat function sepatutnya untuk divide task, tapi aku alang ii
def get_status(hi, score):
  if hi >= 70:
    status = "Stable"
  elif hi >= 40: 
    status = "Warning"
  elif hi >= 20:
    status = "Cyberpsychosis Risk"
  else:
    status = "Critical"
    
  if score > 75 and (status == "Warning" or status == "Stable"):
    status = "Cyberpsychosis"
  return status

#ni nak mintak logic roles buat
  

HIbar= make_bar(50)
#btw jgn run lagi, sbb ada function yang aku  belum define recommend dll
#and ni aku hardcode can dia punya value
def show_report():
  print(f"+{20*"-"} SAFETY REPORT {20*"-"}")
  print(f'|{" HUMANITY INDEX":<20}{HIbar}')
  print(f'|{" POWER LOAD":<20}{make_bar(40)}')
  print(f'|{" SLOT CLASHES":<20} 2 (nervous,arm) -> penalty 50')
  print(f'|{" OVERLOAD RISK":<20}{make_bar(70)}')
  print(f"+{55*'-'}")
  print(f'|{" STATUS":<20}>>{get_status(50, 80)}<<')
  print(f'|{" DAMPENER ADVISORY":<20}')
  print(f'|{" RECOMMENDATION":<20}')
  print(f'|{" MALFUNCTION CHECK":<20}')
  
  
component_list = (["Optical Scanner", "Eyes", 5, 10, "Civilian",1],["Subdermal Armor", "Skin", 10, 20, "Civilian",2],["Load-Lifter Arm", "Arm", 12, 40, "Industrial",3],["Kerenzikov", "Nervous", 18, 35, "Combat",4],["Mantis Blades", "Arm", 18, 35, "Combat",5])
locked_list = []
installed_component = []
allowed_list = []

print(54*"-")
for index, component in enumerate(component_list, 1):
  print(f"{index}|{component[0]:<20}|{component[1]:<10}|{component[2]:<3}|{component[3]:<3}|{component[4]:<11}|")

def choose_user_type():
  user_type = ""
  while user_type not in ["citizen", "worker", "military", "disabled"]:
    user_type = input("Select user type.....").lower()
  if user_type == "citizen":
    capacity = 100
    modifier = 1.0
    allowed = ["Civilian"]
  elif user_type == "worker":
    capacity = 150
    modifier = 1.0
    allowed = ["Civilian", "Industrial"]
  elif user_type == "military":
    capacity = 250
    modifier = 0.8
    allowed = ["Civilian", "Industrial", "Combat"]
  elif user_type == "disabled":
    capacity = 100
    modifier = 1.0
    allowed = ["Civilian", "Medical"]
  return user_type, capacity, modifier, allowed
  
#btw aku buat terus yang bawah ni sbb klu tak, value tak keluar dari function

def allowing_component():
  for part in component_list:
    if part[4] in allowed:
      allowed_list.append(part[0])
  return allowed_list

def ask_number(question, low, high):
    user_input = input(question)
    while not user_input.isdigit() or not low <= int(user_input) <= high:
        print(f"input is out of range, please input between {low} to {high}")
        user_input = input(question)
    return int(user_input)


def install_component(component_list, installed_component, allowed):
  user_input = ''
  while user_input != 0:
    user_input = ask_number("select cybernetics....", 0, 5)
    if user_input == 0:
        break
    for part in component_list:
      if user_input == part[5] and part[0] in allowed_list:
        if part[0] in installed_component:
          print("component has already been installed")
          break
        else:
          installed_component.append(part[0])
          print(f"{part[0]} installed")
        break
      elif user_input == part[5] and part[0] not in allowed_list:
        print("component locked")
        break
    else:
      print("component not found")
        
user_type, capacity, modifier, allowed = choose_user_type()
allowed_list = allowing_component()
print(allowed_list)
install_component(component_list, installed_component, allowed)
show_report()
  
  
  




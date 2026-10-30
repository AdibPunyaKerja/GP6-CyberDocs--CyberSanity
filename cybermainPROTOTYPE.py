#ntah saja buat alang ii free. ni byk pakai untuk show report
def make_bar(value):
  value = round(value/100*20)
  filledHash = value
  emptyHash = 20-value
  return f'[{filledHash*"#"}{emptyHash*"-"}]'
#ni pakai sekali je, and buat function sepatutnya untuk divide task, tapi aku alang ii


def ask_number(question, low, high):
    user_input = input(question)
    while not user_input.isdigit() or not low <= int(user_input) <= high:
        print(f"input is out of range, please input between {low} to {high}")
        user_input = input(question)
    return int(user_input)

#ni nak mintak logic roles buat

#im mking new function bruh

def calc_power(installed_component):
  total_power = 0
  for part in (installed_component):
    total_power += part[3]
  return total_power 

def calc_humanity(installed_component, modifier, user_type):
  humanity_loss = 0
  if user_type == "Disabled":
    for part in installed_component:
      if part[4] == "Medical":
        humanity_loss += part[2]* 0.5
      else:
        humanity_loss += part[2]
  else:
    for part in installed_component:
      humanity_loss += part[2] * modifier
  humanity = 100- humanity_loss
  return humanity
  
def calc_power_load(capacity, total_power):
  power_percentage = total_power / capacity * 100
  if power_percentage >100:
    power_percentage = 100
  return power_percentage

def find_clashes(installed_component):
  seen = []
  clashes = []
  for part in installed_component:
    if not part[1] in seen:
      seen.append(part[1])
    else:
      clashes.append(part[1])
  return clashes

def calc_penalty(clashes):
  penalty = len(clashes) * 25
  if penalty >100:
    penalty = 100
  return penalty
    

def calc_overload(power_percentage,humanity, penalty):
  overload_score = 0.4*power_percentage + 0.3 * (100 - humanity) + 0.3 * penalty
  return overload_score



def get_status(humanity, overload_score):
  if humanity >= 70:
    status = "Stable"
  elif humanity >= 40: 
    status = "Warning"
  elif humanity >= 20:
    status = "Cyberpsychosis Risk"
  else:
    status = "Critical"
    
  if overload_score > 75 and (status == "Warning" or status == "Stable"):
    status = "Cyberpsychosis Risk"
  return status

def recommend(installed_component, status):
  recommendation = ""
  highest_power = 0
  if status == "Stable":
    recommendation= "No removal needed."
  elif status == "Warning":
    recommendation ="No removal needed. Do not install more."
  elif status == "Cyberpsychosis Risk" or status == "Critical":
    for part in installed_component:
      if part[3] > highest_power:
        highest_power = part[3]
        recommendation = f"Remove {part[0]}"
  return recommendation




#btw jgn run lagi, sbb ada function yang aku  belum define recommend dll
#and ni aku hardcode can dia punya value
def show_report():
  print(f"+{20*"-"} SAFETY REPORT {20*"-"}")
  print(f'|{" HUMANITY INDEX":<20}{make_bar(humanity)}')
  print(f'|{" POWER LOAD":<20}{make_bar(power_percentage)}')
  print(f'|{" SLOT CLASHES":<20} {len(clashes)} {clashes} -> penalty {penalty}')
  print(f'|{" OVERLOAD RISK":<20}{make_bar(overload_score)}')
  print(f"+{55*'-'}")
  print(f'|{" STATUS":<20}>>{status}<<')
  print(f'|{" DAMPENER ADVISORY":<20}')
  print(f'|{" RECOMMENDATION":<20}{recommendation}')
  print(f'|{" MALFUNCTION CHECK":<20}')
  
  
installed_component = []
allowed_list = []
locked = False
def show_list():
  print(54*"-")
  for index, component in enumerate(component_list, 1):
    print(f"{index}|{component[0]:<20}|{component[1]:<10}|{component[2]:<3}|{component[3]:<3}|{component[4]:<11}|")


def choose_user_type():
  user_type = ""
  print("SELECT USER TYPE")
  print("[1] Citizen")
  print("[2] Worker")
  print("[3] Military")
  print("[4] Disabled")
  
  user_input = ask_number(">.....",1,4)
  print("")
  if user_input == 1:
    user_type = "citizen"
    capacity = 100
    modifier = 1.0
    allowed = ["Civilian"]
  elif user_input == 2:
    user_type = "worker"
    capacity = 150
    modifier = 1.0
    allowed = ["Civilian", "Industrial"]
  elif user_input == 3:
    user_type = "military"
    capacity = 250
    modifier = 0.8
    allowed = ["Civilian", "Industrial", "Combat"]
  elif user_input == 4:
    user_type = "disabled"
    capacity = 100
    modifier = 1.0
    allowed = ["Civilian", "Medical"]
  print(f"USER TYPE........{user_type.upper()}")
  print(f"POWER CORE.......{capacity}W")
  print(f"HUMANITY MOD.....x{modifier:.2f}")
  return user_type.capitalize(), capacity, modifier, allowed
  
#btw aku buat terus yang bawah ni sbb klu tak, value tak keluar dari function

def allowing_component(allowed):
  allowed_list = []
  for part in component_list:
    if part[4] in allowed:
      allowed_list.append(part[0])
  return allowed_list


def install_component(component_list, installed_component, allowed,locked):
  if locked == True:
    print("Unable to install new cybernetics, HI is Below 20")
    return
  user_input = ask_number("select cybernetics....", 0, len(component_list))
  if user_input == 0:
      return
  for part in component_list:
    if user_input == part[5] and part[0] in allowed_list:
      if part in installed_component:
        print("component has already been installed")
        break
      else:
        installed_component.append(part)
        print(f"{part[0]} installed")
      break
    elif user_input == part[5] and part[0] not in allowed_list:
      print("component not allowed for your user type")
      break
  else:
    print("component not found")

def remove_component(installed_component):
  if not installed_component:
    print("no component installed")
    return
  for index, component in enumerate(installed_component, 1):
    print(f"{index}|{component[0]:<20}|{component[1]:<10}|{component[2]:<3}|{component[3]:<3}|{component[4]:<11}|")
  user_input = ask_number("select cybernetics to be removed....", 0, len(installed_component))
  if user_input == 0:
    return
  else:
    user_input -= 1
    removed = installed_component.pop(user_input)
    print(f"successfully remove {removed[0]}")
  








component_list = (["Optical Scanner", "Eyes", 5, 10, "Civilian",1],["Subdermal Armor", "Skin", 10, 20, "Civilian",2],["Load-Lifter Arm", "Arm", 12, 40, "Industrial",3],["Kerenzikov", "Nervous", 15, 30, "Combat",4],["Mantis Blades", "Arm", 18, 35, "Combat",5], ["Sandvistan","Nervous", 25, 60, "Combat",6], ["Neural Link", "Nervous", 20,50,"Combat",7], ["Prosthetic Arm", "Arm", 8,25,"Medical",8],["Retinal Implant","Eyes",6,12,"Medical",9], ["Smart Wrist Display","Arm", 3,5,"Civilian",10],["Night Vision Lens","Eyes", 7,15,"Civilian",11], ["Heavy Grip Hand", "Arm", 10, 30, "Industrial",12])
installed_component = []


show_list()
user_type, capacity, modifier, allowed = choose_user_type()
allowed_list = allowing_component(allowed)
print("  [1] Show available components\n  [2] Install a component\n  [3] remove a component\n  [4] Run analysis\n  [5] Change user type (resets installed list)\n  [6]exit\n  [0]see menu again")
while True:
  menuNum = ask_number("",0,6)
  if menuNum == 0:
    print("  [1] Show available components\n  [2] Install a component\n  [3] remove a component\n  [4] Run analysis\n  [5] Change user type (resets installed list)\n  [6]exit\n  [0]see menu again")
  elif menuNum == 1:
    for index, component in enumerate(allowed_list):
     print(f"....{component}")
  elif menuNum == 2:
    install_component(component_list, installed_component, allowed,locked)
  elif menuNum == 3:
    remove_component(installed_component)
  elif menuNum == 4:
    total_power = calc_power(installed_component)
    power_percentage = calc_power_load(capacity, total_power)
    humanity = calc_humanity(installed_component, modifier, user_type)
    clashes = find_clashes(installed_component)
    penalty = calc_penalty(clashes)
    overload_score = calc_overload(power_percentage,humanity, penalty)
    status = get_status(humanity, overload_score)
    recommendation = recommend(installed_component, status)
    show_report()
  elif menuNum == 5:
    #belum lagi
    print("not yet")
  elif menuNum == 6:
    exit()
    
def make_bar(value):
  value = round(value/100*20)
  filledHash = value
  emptyHash = 20-value
  return f"[{filledHash*"#"}{emptyHash*"-"}]"

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


def advisory(status):
  

HIbar= make_bar(50)

def show_report():
  print(f"+{20*"-"} SAFETY REPORT {20*"-"}")
  print(f'|{" HUMANITY INDEX":<20}{HIbar}')
  print(f'|{" POWER LOAD":<20}{make_bar(40)}')
  print(f'|{" SLOT CLASHES":<20} 2 (nervous,arm) -> penalty 50')
  print(f'|{" OVERLOAD RISK":<20}{make_bar(70)}')
  print(f"+{55*'-'}")
  print(f'|{" STATUS":<20}>>{get_status(50, 80)}<<')
  print(f'|{" DAMPENER ADVISORY":<20}{advisory(status)}')
  print(f'|{" RECOMMENDATION":<20}{recommend(installed, status)}')
  print(f'|{" MALFUNCTION CHECK":<20}')
  
  
  

print(show_report())

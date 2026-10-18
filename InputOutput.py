
#ni aku dah buat ask_number punya function, fahamkan dulu broski- adib
def ask_number(question, low, high):
    user_input = input(question)
    while not user_input.isdigit() or not low <= int(user_input) <= high:
        print(f"Bro type number outside range, pls select from {low} to {high}")
        user_input = input(question)
    return int(user_input)

    #ni example of how to use ts-adib
menuNum = ask_number("next?", 1, 5)
print(menuNum)

#ni pulak untuk buat bar
def make_bar(value):
  value = round(value/100*20)
  filledHash = value
  emptyHash = 20-value
  return f"[{filledHash*"#"}{emptyHash*"-"}]"

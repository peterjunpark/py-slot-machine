import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

SYMBOLS_PER_REEL = 5
REELS = 3

symbol_count = {
  "😂": 1,
  "💀": 2,
  "🐸": 3,
  "🌮": 4,
  "🍄": 5,
  "🌀": 6,
}

symbol_value = {
  "😂": 7,
  "💀": 6,
  "🐸": 5,
  "🌮": 4,
  "🍄": 3,
  "🌀": 2,
}

def check_winnings(reels, lines, bet, values):
  winnings = 0
  winning_lines = []

  for line in range(lines):
    symbol = reels[0][line]

    for reel in reels:
      symbol_to_check = reel[line]
      if symbol != symbol_to_check:
        break
    else:
      winnings += values[symbol] * bet
      winning_lines.append(line + 1)

  return winnings, winning_lines


def get_slots_spin(reels, symbols_per_reel, symbols):
  all_symbols = []

  for symbol, symbol_count in symbols.items():
    for _ in range(symbol_count):
      all_symbols.append(symbol)

  reels_list = []

  for _ in range(reels):
    reel_list = []
    # note: slice operator
    current_symbols = all_symbols[:]
    for _ in range(symbols_per_reel):
      value = random.choice(current_symbols)
      current_symbols.remove(value)
      reel_list.append(value)

    reels_list.append(reel_list)

  return reels_list

def print_slots(reels):
  for row in range(len(reels[0])):
    for i, col in enumerate(reels):
      print(col[row], end=" | " if i != len(reels) - 1 else "\n")


def deposit():
  while True:
    amount = input("Enter amount to deposit: $")
    if amount.isdigit():
      amount = int(amount)
      if amount > 0:
        break
      else:
        print("Deposit amount must be greater than 0.")
    else:
      print("Please enter a number.")
  return amount

def get_number_of_lines():
  while True:
    lines = input(f"Enter a number of lines to bet on (1-{MAX_LINES}): ")
    if lines.isdigit():
      lines = int(lines)
      if 1 <= lines <= MAX_LINES:
        break
      else:
        print("Invalid number of lines.")
    else:
      print("Please enter a number.")
  return lines

def get_bet():
  while True:
    amount = input("Enter amount to bet on each line: $")
    if amount.isdigit():
      amount = int(amount)
      if MIN_BET <= amount <= MAX_BET:
        break
      else:
        print(f"Amount to be must be between ${MIN_BET} and ${MAX_BET}")
    else:
      print("Please enter a number.")
  return amount

def play(balance):
  lines = get_number_of_lines()

  while True:
    bet = get_bet()
    total_bet = bet * lines

    if balance < total_bet:
      print(f"Your total bet exceeds your current balance of ${balance}.")
    else:
      balance -= total_bet
      break

  print(f"You are betting ${bet} on {lines} lines.\nYour total bet amount is {total_bet}.")

  slots = get_slots_spin(REELS, SYMBOLS_PER_REEL, symbol_count)
  print_slots(slots)

  winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)

  if winnings > 0:
    print(f"You won ${winnings} on lines:", *winning_lines)
  else:
    print("You lost.")

  return winnings - total_bet

def main():
  balance = deposit()

  while True:
    # print(f"Current balance is ${balance}.")
    spin = input("Press enter to play (q to quit).")

    if spin == "q":
      break

    balance += play(balance)
    print(f"Your balance is now ${balance}.")

  print(f"You left with ${balance}!")


if __name__ == "__main__":
  main()

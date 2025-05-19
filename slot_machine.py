import random

MAX_LINES=3
MAX_BET=100
MIN_BET=1

ROWS=3
COLS=3

symbol_count={ "A":2, "B":4, "C":6,"D":8}

symbol_values={ "A":5, "B":4, "C":3,"D":2}

def check_winnings(columns, lines, bet, value):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings+= value[symbol]*bet
            winning_lines.append(line+1)
    return winning_lines, winnings

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol, symbol_count in symbols.items():
        for i in range(symbol_count):
            all_symbols.append(symbol)
    columns =[]
    for col in range(cols):
        column=[]
        current_symbols = all_symbols[:]
        for row in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_machine_slot(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!= len(columns) - 1:
                print(column[row], "|" , end=" ")
            else:
                print(column[row])


def deposit():
    while True:
        amount=input("What amount would you like to deposit? $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_num_of_lines():
    while True:
        lines=input("Enter the number of lines you wanna bet on(1-" + str(MAX_LINES) +"): ")
        if lines.isdigit():
            lines=int(lines)
            if 1<=lines<=MAX_LINES:
                break
            else:
                print("NUmber of lines must be within max lines allowed.")
        else:
            print("Please enter a valid number.")
    return lines

def get_bet():
    while True:
        bet=input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet=int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f"Bet amount must be within ${MIN_BET}-${MAX_BET}")
        else:
            print("Error! Please try again!")
    return bet

def game(balance):
    lines= get_num_of_lines()
    while True:
        bet=get_bet()
        total_bet= bet*lines
        if total_bet> balance:
            print(f"You do not have enough penny to bet. Your current balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} in {lines} lines. Total bet is ${total_bet}")
    slots=get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_machine_slot(slots)
    winnings_lines, winnings = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won ${winnings} on lines: {winnings_lines}")
    return winnings - total_bet

def main():
    balance= deposit()
    while True:
        
        print("your currrent balance is", f"${balance}")
        spin=input("press enter to spin (q to quit):")
        if spin=='q':
            break
        balance+=game(balance)
main()
            
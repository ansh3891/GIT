import random
MAX_LINES=3
MAX_BET=100
MIN_BET=1
ROWS=3
COLS=3

Symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8
}
Symbol_value={
    "A":5,
    "B":4,
    "C":3,
    "D":2
}

def check_winnings(columns,lines,bets,values):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
            else:
                winnings+=values[symbol]*bets
                winning_lines.append(line + 1)
    return winnings,winning_lines

def get_slot_machine_spin(rows,cols,symbols):
    all_symbols=[]
    for symbol,Symbol_count in symbols.items():
        for _ in range(Symbol_count):
            all_symbols.append(symbol)
            columns=[]
    for _ in range(cols):
        column=[]
        current_symbols=all_symbols[:] #we used slice operator as we dont want the changes of curr symbls to be reflected in all_symbols
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns
def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i,column in enumerate(columns): #changed column to columns
            if i!=len(columns)-1:
                print(column[row],end=" | ")
            else:
                print(column[row],end="")
        print()

def deposit():
    while True:
        try:
            amount=int(input("How much would you like to deposit? $"))
        except ValueError:
            print("Please enter a number")
            continue
        if amount<=0:
            print("Amount can't be less than 0.")
            continue
        else:
            return amount
def get_no_of_lines():
    while True:
        try:
            amount=int(input("How many lines you'd like to bet on? (1 -"+str(MAX_LINES)+")"))
        except ValueError:
            print("Enter a number")
            continue 
        if amount < 1 or amount > MAX_LINES:
            print("Invalid!")
            continue
        else:
            return amount

def get_bet(balance): #added balance as a parameter
    while True:
        try:
            amount=int(input(f"How much would you like to bet on each line? ${MIN_BET} - ${MAX_BET} $"))
        except ValueError:
            print("Enter a valid amount")
            continue 
        if amount < MIN_BET or amount > MAX_BET:
            print("Invalid!")
            continue
        elif amount*MAX_LINES > balance: #added this condition to check if the bet exceeds the balance
            print(f"You can't bet more than your balance of ${balance}")
            continue
        else:
            return amount

def spin(balance): #added balance as a parameter
    lines=get_no_of_lines()
    bet=get_bet(balance) #passed balance as an argument
    total_bet=bet*lines
    
    print(f"You are betting ${bet} on {lines} lines, total bet=${total_bet}")
    slots=get_slot_machine_spin(ROWS,COLS,Symbol_count) #changed COlS to COLS
    print_slot_machine(slots)

    winnings,winning_lines=check_winnings(slots,lines,bet,Symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on ", *winning_lines)
    return winnings-total_bet #changed winning_lines to winnings


def main():
    balance=deposit()
    while True:
        print(f"The Current balance is ${balance}")
        play=input("Press any key to play, q to quit")
        if play=="q":
            break
        balance+=spin(balance) #passed balance as an argument
    print(f"You left with ${balance},")
main()
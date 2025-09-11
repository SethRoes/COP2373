# The code is allowing a buyer to buy up to 4 tickets, No more than 20 tickets can be sold total.

def get_ticket_purchase(remaining_tickets):

    while True:
        try:
            num_tickets = int(
                input(f"How many tickets would you like to purchase? (You may buy up to 4, {remaining_tickets} remaining): "))
            if 1 <= num_tickets <= 4 and num_tickets <= remaining_tickets:
                return num_tickets
            elif num_tickets > remaining_tickets:
                print(f"Error: You cannot buy more tickets than available. Only {remaining_tickets} tickets remaining.")
            else:
                print("Error: You can buy between 1 and 4 tickets.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def sell_tickets():

    total_tickets = 10
    remaining_tickets = total_tickets
    buyer_count = 0

    print("Welcome to the Cinema Ticket Pre-Sale!")

    while remaining_tickets > 0:
        tickets_to_buy = get_ticket_purchase(remaining_tickets)

        remaining_tickets -= tickets_to_buy
        buyer_count += 1
        print(f"Purchase successful! {remaining_tickets} tickets remaining.")

    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {buyer_count}")

if __name__ == "__main__":
    sell_tickets()
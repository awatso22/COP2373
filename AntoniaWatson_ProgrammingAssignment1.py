"""
Cinema Ticket Pre-Sale Application
Allows buyers to purchase up to 4 tickets each
Maximum of 20 tickets sold total
"""

MAX_TICKETS = 20
MAX_PER_BUYER = 4

def get_ticket_request(tickets_remaining):
    """
    Prompts the user for the number of tickets they want to buy
    Ensures the request is valid before returning it
    """
    requested = int(input(f"How many tickets would you like to buy?(1-{MAX_PER_BUYER}): "))

    if requested < 1:
        print("You must buy at least 1 ticket.")
        return 0
    elif requested > MAX_PER_BUYER:
        print("You can buy a maximum of 4 tickets.")
        return 0
    elif requested > tickets_remaining:
        print(f"Only {tickets_remaining} tickets remaining.")
        return 0

    return requested

def run_ticket_sales():
    """
    Main function that runs the ticket sales loop
    """
    tickets_remaining = MAX_TICKETS
    total_buyers = 0

    while tickets_remaining > 0:
        print(f"\nTickets remaining: {tickets_remaining}")
        tickets_requested = get_ticket_request(tickets_remaining)

        if tickets_requested > 0:
            tickets_remaining -= tickets_requested
            total_buyers += 1
            print(f"Purchase successful! {tickets_remaining} tickets left.")

    print("\nAll tickets have been sold!")
    print(f"Total number of buyers: {total_buyers}")

# Start the program
run_ticket_sales()

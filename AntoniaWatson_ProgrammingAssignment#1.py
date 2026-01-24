"""
Cinema Ticket Pre-sale Application
This script manages the sale of 20 limited cinema tickets.
Users can buy 1-4 tickets at a time until the stock is depleted.
"""

def process_purchase(remaining_tickets):
"""
Prompts the user for input and validates the purchase amount.

Args:
    remaining_tickets (int): The current pool of available tickets.

Returns:
    int: The number of tickets successfully purchased.
"""

while True:
    try:
        #2. Input
        num_requested = int(input(f"How man tickets would you like to buy? (Max 4, {remaining_tickets} left):"))

        # 5. If state statement (Validation)
        if num_requested < 1:
            print("You must buy at least 1 ticket.")
        elif num_requested > 4:
            print("Transaction denied: You cannot buy more than 4 tickets.")
        elif num_requested > remaining_tickets:
            print(f"Transaction denied: Only {remaining_tickets} tickets remaining.")
        else:
            return num_requested
        except ValueError:
            print("Invalid input. Please enter a whole number.")

def start_sale():
    """
    Main loop to run the ticket booth until all tickets are sold.
    Tracks the total number of buyers.
    """
    total_tickets = 20
    # 4. Accumulator (Total Buyers)
    total_buyers = 0

    print("---Welcome to the Cinema Pre-sale! ---")

    # 6. Loop
    while total_tickets > 0:
        purchased = process_purchase(total_tickets)

        # Update remaining tickets and increment buyer count
        total_tickets -= purchased
        total_buyers += 1

        # 3. Output
        print(f"Purchase successful! {total_tickets} tickets remaining.")
        print("-" * 30)

    print("\nPre-sale Sold Out!")
    print(f"Total number of buyers: {total_buyers}")

if __name__ == "__main__":
    start_sale()

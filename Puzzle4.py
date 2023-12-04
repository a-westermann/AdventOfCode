import file_ops
import re


class Ticket:
    def __init__(self, card_id: str, winning_numbers: list[str], my_numbers: list[str]):
        # Note: could convert these to ints w/ list comprehension if need in part 2
        self.card_id = card_id
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers


def parse_ticket(ticket_str: str) -> Ticket:
    # search for the card number
    num_regex = re.compile(r'\d+')
    card_id = num_regex.search(ticket_str.split(':')[0]).group()
    winning_numbers = num_regex.findall(ticket_str.split(':')[1].split('|')[0])
    my_numbers = num_regex.findall(ticket_str.split(':')[1].split('|')[1])
    return Ticket(card_id, winning_numbers, my_numbers)


input_lines = file_ops.read_input(4)
total_points = 0
for line in input_lines:
    ticket = parse_ticket(line)
    win_count = len([n for n in ticket.winning_numbers if n in ticket.my_numbers])
    points = 1 * 2 ** (win_count - 1) if win_count > 0 else 0
    total_points += points
    print(f' ticket {ticket.card_id}')
    print(f'ponts: {points} for {len([n for n in ticket.my_numbers if n in ticket.winning_numbers])} wins')

print(f'Final points: {total_points}')


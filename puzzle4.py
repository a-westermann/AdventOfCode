import file_ops
import re


class Ticket:
    def __init__(self, card_id: str, winning_numbers: list[str], my_numbers: list[str]):
        self.card_id = int(card_id)
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers
        self.win_count = 0


def parse_ticket(ticket_str: str) -> Ticket:
    # search for the card number
    num_regex = re.compile(r'\d+')
    card_id = num_regex.search(ticket_str.split(':')[0]).group()
    winning_numbers = num_regex.findall(ticket_str.split(':')[1].split('|')[0])
    my_numbers = num_regex.findall(ticket_str.split(':')[1].split('|')[1])
    return Ticket(card_id, winning_numbers, my_numbers)


input_lines = file_ops.read_input(4)
total_points = 0  # part 1
tickets = []
for line in input_lines:
    # build all the Ticket objecst
    ticket = parse_ticket(line)
    ticket.win_count = len([n for n in ticket.winning_numbers if n in ticket.my_numbers])
    points = 1 * 2 ** (ticket.win_count - 1) if ticket.win_count > 0 else 0
    total_points += points
    tickets.append(ticket)
for ticket in tickets:  # part 2
    # When adding more tickets, just use the index of the card_id rather than building a list
    # print(f'analyzing ticket {ticket.card_id}')
    for i in range(ticket.win_count):
        tickets.append(tickets[ticket.card_id + i])
        # print(f'Adding ticket {tickets[ticket.card_id + i].card_id}')


print(f'Final points: {total_points}')
print(f' Part 2 # of tickets: {len(tickets)}')


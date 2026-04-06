"""
Напишіть програму, яка генерує лотерейні білети для групи користувачів. Кожен білет складається з унікального набору чисел.
Програма повинна забезпечити наступне:
1.Лотерейний білет містить 6 чисел від 1 до 49.
2.Номери в білеті не повторюються.
3.Для кожного учасника генерується певна кількість білетів (визначається випадковим чином у діапазоні від 1 до 5)-
4.Програма зберігає всі білети та забезпечує, що білети унікальні навіть між різними учасниками.
5.Наприкінці виводиться список учасників та їхні білети.
"""

import random

def generate_lottery_ticket(participants: list)-> dict:
    all_tickets = set()
    participant_tickets = {}
    
    for participant in participants:
        num_tickets = random.randint(1, 5)
        tickets = list()
        
        for _ in range(num_tickets):
            while True:
                 
                ticket = tuple(sorted(random.sample(range(1, 50), k=6))) 
                if ticket not in all_tickets:
                    all_tickets.add(ticket)
                    tickets.append(ticket)
                    break

        participant_tickets[participant] = tickets

    return participant_tickets

def pick_random_winner(participant_tickets):
    all_tickets = []
    for participant, tickets in participant_tickets.items():
        for ticket in tickets:
            all_tickets.append((participant, ticket))
    winner = random.choice(all_tickets)
    winner_name, winning_ticket  = winner

    message = (f"Congratulation: {winner_name}!\n"
           f"Your winning ticket: {winning_ticket}"
           )
    return message


participants = ["Serhii", "Yuliia", "Viktoriia"]

participant_tickets = generate_lottery_ticket(participants)
for participant, tickets in participant_tickets.items():
    print(f"Participant: {participant}")
    print(f"Tickets:")
    for ticket in tickets:
        print(f"\t{ticket}")

print(pick_random_winner(participant_tickets))
sandwich_orders = ['pan con pollo', 'pastrami' ,'butifarra', 'jamón del país', 'pastrami', 'jamón del norte', 'pastrami']
finished_sandwiches = []

print("\nWe run out of pastrami")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made you a {sandwich} sandwich")
    finished_sandwiches.append(sandwich)

for sandwich in finished_sandwiches:
    print(sandwich)

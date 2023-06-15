from collections import deque
customers = deque(int(x) for x in input().split(", "))
taxis = deque(int(x) for x in input().split(", "))

total_time = 0

while customers:
    customer = customers.popleft()
    taxi = taxis.pop()
    if taxi >= customer:
        total_time += customer
    else:
        customers.appendleft(customer)

    if not taxis and customers:
        print(f"Not all customers were driven to their destinations \n"
              f"Customers left: {', '.join([(str(x))for x in customers])}")
        break
if not customers:
    print("All customers were driven to their destinations \n"
          f"Total time: {total_time} minutes")




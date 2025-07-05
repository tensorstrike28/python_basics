n = int(input("Enter number of rows: ").strip())
print(f"Enter {n} rows of csv:\n")
users = []
for _ in range(n):
    user = {}
    user['name'], user['age'], user['city'] = input().strip().split(',')
    users.append(user)
for user in users:
    if user['city'].lower() == "mumbai":
        print(user['name'])

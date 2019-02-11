# Example input() statement
state = input('Please enter a State: ')

my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', 'New York': 'Albany'}
if my_dct == state:
    print(my_dct.get(my_dct))
else:
    print('Not Found')
    
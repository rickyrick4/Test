my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago',
          'New York': 'Albany', 'Iowa': 'Des Moines',
          'California': 'Sacramento', 'Utah': 'Salt Lake City',
          'Ohio': 'Columbus'}
for state in my_dct:
    if my_dct[state].startswith('S'): 
        print(my_dct[state])
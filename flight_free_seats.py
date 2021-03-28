from string import ascii_uppercase
seats = [i for i in ascii_uppercase if i!='I']
reserved = ['1B', '1C','1F']
for i in (1,3):
    all_seats=[]
    available=[]
    for c in (seats[:10]):
        all_seats.append(str(i)+c)
    available = [j if j in reserved else "GREEN" for j in all_seats  ]
    print(all_seats)
    no_seats=0
    if 'GREEN' not in available:
        no_seats=no_seats+2
    if all(seat == 'GREEN' for seat in available[2:5] ):
        no_seats=no_seats+1
    if all(seat == 'GREEN' for seat in available[6:9] ):
        no_seats=no_seats+1
    print(no_seats)

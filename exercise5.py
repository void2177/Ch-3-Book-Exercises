def bottle_verse(num):
   bottlenum = "bottle" if num == 1 else "bottles"
   print(f"""{num} {bottlenum} of beer on the wall
{num} {bottlenum}  of beer 
Take one down, pass it around
{num - 1} {bottlenum}  of beer on the wall!""")

def bottle_song(num):
    for i in range(num, 0, -1):
        bottle_verse(i)

bottle_song(50)




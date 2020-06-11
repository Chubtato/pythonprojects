def move(height, start, mid, end):
    if height >= 1:
        move(height-1, start, end, mid)
        moving(start,end, height)
        move(height-1, mid, start, end)
def moving(start, end, height):
    print("Moving disk of size %s from tower %s to tower %s"%(height,start,end))

move(4,"A","B","C")

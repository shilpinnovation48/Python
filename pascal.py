Start = [1,1]
End = [1, 1]
for z in range(5):
    for x in range(len(Start) - 1):
        y  = Start[x] + Start[x + 1]
        End.insert(x + 1, y)
    print End
    Start = End
    End = [1, 1]

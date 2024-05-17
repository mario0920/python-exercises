building = {
    "Entrance 1": {
        "floor 1": [
            "ap 1",
            "ap 2",
            "ap 3",
            "ap 4",
        ],
        "floor 2": [
            "ap 5",
            "ap 6",
            "ap 7",
            "ap 8",
        ],
        "floor 3": [
            "ap 9",
            "ap 10",
            "ap 11",
            "ap 12",
        ],
    },
    "Entrance 2": {
        "floor 1": [
            "ap 13",
            "ap 14",
            "ap 15",
            "ap 16",
        ],
        "floor 2": [
            "ap 17",
            "ap 18",
            "ap 19",
            "ap 20",
        ],
        "floor 3": [
            "ap 21",
            "ap 22",
            "ap 23",
            "ap 24",
        ],
    },
} 

for b in building:
    print(b)
    for f in building[b]:
        print("\t" + f)
        for a in building[b][f]:
            print("\t\t" + a)






    
    
numberDict={
    "one":1,
    "two":2,
    "three":3,
    "four":4,
    "five":5,
    "six":6,
    "seven":7,
    "eight":8,
    "nine":9
}

str = "twotwentytwothree"

for count, i in enumerate(str):
    try:
        print(str.index("two", count))
    except:
        pass
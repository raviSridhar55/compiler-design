def function(str):
    if(str.find('|') != -1):
        print('The Transition table is:\n')
        print("St1'      St2''    A\n")
        print("St1'      St2''    B\n")
        function(input("Give a regular expression:  "))
    elif(str.find('*') != -1):
        print('The Transition table is:\n')
        print("St1'     St2     e\n")
        print("St2      St3     A\n")
        print("St3      St4''   e\n")
        print("St4''    St2     e\n")
        print("St1'     St4     e\n")
        function(input("Give a regular expression:  "))
    elif(str.count('a') == 1):
        print('The Transition table is:\n')
        print("St1'      St2''     A\n")
        function(input("Give a regular expression:  "))
    elif(str.count('b') == 1):
        print('The Transition table is:\n')
        print("St1'      St2''     B\n")
        function(input("Give a regular expression:  "))
    elif(str.count('end')):
        return 0
    else:
        print('Give a valid expression please...')
        function(input("Give a regular expression:  "))

function(input("Give a regular expression:  "))
# Input a list command and its args, then process the command

n = int(input())
out_arr = []

for i in range(n):
    args = input().split()
    if args[0].lower() == 'insert':
        out_arr.insert(int(args[1]), int(args[2]))
    elif args[0].lower() == 'print':
        print(out_arr)
    elif args[0].lower() == 'remove':
        out_arr.remove(int(args[1]))
    elif args[0].lower() == 'append':
        out_arr.append(int(args[1]))
    elif args[0].lower() == 'sort':
        out_arr.sort()
    elif args[0].lower() == 'pop':
        out_arr.pop()
    elif args[0].lower() == 'reverse':
        out_arr.reverse()
    elif args[0].lower() == 'quit' or args[0].lower() == 'exit':
        quit()
    else:
        print('Invalid args: ' + args)

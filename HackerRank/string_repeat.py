def str_rpt(s, n):
    r = 0
    l = len(s)
    for i in range(0, l):
        if s[i] == 'a':
            r+= 1
    r*= int(n / l)
    for i in range(0, n % l):
        if s[i] == 'a':
            r+= 1
    return r

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = str_rpt(s, n)

    #fptr.write(str(result) + '\n')

    #fptr.close()
    print(result)


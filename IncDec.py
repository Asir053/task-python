def increasingDecreasing( i,  n):
    if(i == n + 1): return
    print(i , ' ')
    increasingDecreasing(i + 1, n)
    if(i != n): print(i , ' ')

def main():
    n=int(input())
    increasingDecreasing( 1,  n)
main()

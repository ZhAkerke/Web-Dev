print( (lambda a,b: ' '.join(([b[a-1-i] for i in range(a)]))) ( int(input()), input().split() )  )  

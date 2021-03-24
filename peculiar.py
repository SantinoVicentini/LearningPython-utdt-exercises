def misma_paridad(n:int, m:int) -> str:

    if n % 2 == 0 and m % 2 == 0 or n % 2 == 1 and m % 2 == 1: 
        print('si')
        return 'si' 

    else: 
        print('no')
        return 'no'  

    
misma_paridad(3,3)
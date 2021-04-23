def letras_ordenadas(s:str) -> bool:
    ''' Determina si las letras de s están ordenadas alfabéticamente.
    Pre: len(s)>0; s tiene solamente letras en minúscula: abcde...xyz, 
         sin tildes, diéresis ni eñes.
    Post: vr equivale a que las letras de s están ordenadas.
    '''
    vr:bool = True
    i:int = 1
    while i<len(s):
        vr = vr and s[i-1] <= s[i]
        i = i + 1
    return vr

def execute4(term,k) : return ([3*term[k]+((-1)**term[k])*term[k+1]] if term[k+1] != None else [2*term[k],2*term[k]+1]) if term[k] != None else ([term[k+1],3-term[k+1]] if term[k+1] != None else [0,1,2,3])
def execute2(term,k) : return [term[k]] if term[k] != None else [0,1]
def is_legal_region(kmap_function, term) :
    (columns, rows) = (execute4(term,0), execute4(term,2)) if len(term) == 4 else (execute4(term,0), execute2(term,2)) if len(term) == 3 else (execute2(term,0), execute2(term,1))
    isLEGAL = True
    for i in rows : 
        for j in columns :
            if isLEGAL and kmap_function[i][j] == 0 : isLEGAL = False
    if columns == [0,3] : columns = [3,0]
    if rows == [0,3] : rows = [3,0]
    return ((rows[0],columns[0]), (rows[-1],columns[-1]), isLEGAL)
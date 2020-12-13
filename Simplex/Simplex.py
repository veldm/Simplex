

def calculate(lines):
        table = []
        basis = []
        result = []
        rows = []
        buffer = []
        m = 0
        n =0

        #text = "25 -3 5\n30 -2 5\n10 1 0\n6 3 -8\n0 -6 -5"
        #lines = text.split('\n')
        m = len(lines)

        for l in range(0,len(lines)):
            rows = list(map(int, lines[l].split()))         
            buffer.append(rows)
 
        n = len(rows)

        for i in range(0,m):
            table.append([])
            for j in range(0,n+m-1):
              if j<n:
                  table[i].append(buffer[i][j])
              else:
                  table[i].append(0)

            if (n+i)<n+m-1:
                table[i][n+i]=1
                basis.append(n+i)
    
        for i in range(0,2):
            result.append(0)

        n = n+m-1

        mainCol =0
        mainRow = 0

        while True:

            flag = True

            for j in range(1,n):
                if(table[m-1][j]<0):
                    flag=False
                    break
                
            if flag == True:
                break

            mainCol = 1

            for j in range(2,n):
                if(table[m-1][j]<table[m-1][mainCol]):
                    mainCol=j
                    
            mainRow = 0

            for i in range(0,m-1):
                if(table[i][mainCol]>0):
                    mainRow=i
                    break

            for i in range(mainRow+1,m-1):
                if ((table[i][mainCol]>0) and ((table[i][0] / table[i][mainCol])<(table[mainRow][0]/table[mainRow][mainCol]))):
                    mainRow=i
                    
            basis[mainRow] = mainCol

            new_table = []

            for i in range(0,m):
                new_table.append([])
                for j in range(0,n):
                    new_table[i].append(0)

            for j in range(0,n):
                new_table[mainRow][j] = table[mainRow][j]/table[mainRow][mainCol]

            for i in range(0,m):

                if i== mainRow:
                    continue
            
                for j in range(0,n):
                    new_table[i][j] = table[i][j]-table[i][mainCol]*new_table[mainRow][j]

            table=new_table

        for i in range(0,len(result)):
             k = -1
             for j in range(0,len(basis)):
                 if basis[j]==i+1:
                     k=j
                     break
             if k!=-1:
                  result[i]=table[k][0]
             else:
                  result[i]=0
                  

        out = "Симплекс таблица:\n"

        for i in range(0,m):
            for j in range(0,n):
                out=out+str(round(table[i][j],2))+" | "
            out=out+"\n"

        out=out+"\nРешение:\nX[1] = "+str(result[0])+"\nX[2] = "+str(result[1])
        
        print(out)

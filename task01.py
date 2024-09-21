def makeset(r):
    par[r] = r

def union(u,v):
    u = find_par(u)
    v = find_par(v)

    if u != v:
        if par.count(u) >= par.count(v):
            par[v] = u
            if par.count(v)!=0: 
                for i in range(len(par)):
                    if par[i] == v:
                        par[i] = u
            output_file.writelines(f"{par.count(u)}\n")
        else:
            par[u] = v
            if par.count(u) != 0:
                for i in range(len(par)):
                    if par[i] == u:
                        par[i] = v
            output_file.writelines(f"{par.count(v)}\n")
    else:
        output_file.writelines(f"{par.count(u)}\n")
def find_par(v):
    if par[v] == v:
        return v
    par[v] = find_par(par[v])
    return par[v]

input_file = open("input/input01.txt", "r")
output_file = open("output/output01.txt", "w")

n, m = [int(i) for i in input_file.readline().strip().split(" ")]

par = [None] * (n+1)
# print(n, m, par)
for i in range(1, n+1):
    makeset(i)

for i in range(m):
    u, v = [int(i) for i in input_file.readline().strip().split(" ")]
    # print(u, v)
    
    union(u, v)
    # print(par)

output_file.close()


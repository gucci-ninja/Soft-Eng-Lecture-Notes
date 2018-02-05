def AgivenG(i, N):
    ans = float(1/i) - float(N/((1+i)**N-1))
    return ans

def totA(Aprime, G, i, N):
    ans = float(Aprime) + float(G*AgivenG(i, N))
    return ans

def i0(g, i):
    ans = float((1+i)/(1+g)) - 1.0
    return ans

def geometric(A, g, i, N):
    i_0 = i0(g, i)
    ans = A*float(1/(1+g))*float((((1+i_0)**N)-1.0)/(i_0*(1+i_0)**N))
    return ans

def ie(r, m, k):
    ans = float((1+float(r/m))**k) - 1
    return ans

def PgivenA(A, i, N):
    ans = A*float((((1+i)**N)-1)/(i*(1+i)**N))
    return ans

def AgivenP(P, i, N):
    ans = P*float((i*(1+i)**N)/(((1+i)**N)-1))
    return ans

def FgivenA(A, i, N):
    ans = A*float((((1+i)**N)-1)/i)
    return ans

def AgivenF(F, i, N):
    ans = F*float(i/(((1+i)**N)-1))
    return ans

def FgivenP(P, i, N):
    ans = P*float((1+i)**N)
    return ans

def PgivenF(F, i, N):
    ans = F*float(1/((1+i)**N))
    return ans

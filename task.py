import sympy as sp
from typing import Dict

# Controlla il file readme.md per i dettagli su ciascun sub-task

def calcola_derivata(espressione: str, variabile: str) -> sympy.Expr:
    x= sp.Symbol("x")
    funzione = str(input('Inserisci funzione: '))
    derivata = sp.diff(funzione, x)
    return derivata
    pass

def calcola_integrale_definito(espressione: str, variabile: str, estremo_inf: float, estremo_sup: float) -> sympy.Expr:
    x= sp.Symbol("x")
    funzione = str(input('Inserisci funzione: '))
    a=int(input('Inserisci a (primo estremo di integrazione): '))
    b=int(input('Inserisci b (secondo estremo di integrazione): '))
    integrale_definito = sp.integrate(funzione,( x,a,b))
    return integrale_definito
    pass

def calcola_limite(espressione: str, variabile: str, punto: str) -> sympy.Expr:
    x= sp.Symbol("x")
    funzione = str(input('Inserisci funzione: '))
    punto= str(input('Inserisci punto: '))
    limite= sp.limit(funzione,x,punto)
    return limite
    pass

def calcola_polinomio_taylor(espressione: str, variabile: str, punto: float, ordine: int) -> sympy.Expr:
    x= sp.Symbol("x")
    funzione = str(input('Inserisci funzione: '))
    punto= str(input('Inserisci punto: '))
    ordine= int(input('Inserisci ordine: '))
    serie_taylor= sp.series(funzione,x,punto,ordine)
    return serie_taylor
    pass

def risolvi_sistema_lineare(eq1: str, eq2: str, var1: str, var2: str) -> Dict[sympy.Symbol, sympy.Expr]:
    x,y = sp.symbols('x, y')
    eq1= str('Inserisci prima equazione: ')
    eq2= str('Inserisci seconda equazione: ')
    soluzione = sp.solve((eq1, eq2), (x, y))
    return soluzione
    pass

def main():
    print("Sub-task 1:", calcola_derivata("x**3 + 2*x", "x"))
    print("Sub-task 2:", calcola_integrale_definito("x**2", "x", 0, 3))
    print("Sub-task 3:", calcola_limite("sin(x)/x", "x", "0"))
    print("Sub-task 4:", calcola_polinomio_taylor("exp(x)", "x", 0.0, 4))
    print("Sub-task 5:", risolvi_sistema_lineare("x + y - 3", "x - y - 1", "x", "y"))

if __name__ == "__main__":
    main()

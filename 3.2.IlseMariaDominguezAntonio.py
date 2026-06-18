# Definición del AFN
Q = {"q0", "q1", "q2", "q3", "q4"}
sigma = {"0", "1"}
q0 = "q0"
F = {"q2", "q4"}

delta = {
    "q0": {"0": {"q0", "q3"}, "1": {"q0", "q1"}},
    "q1": {"0": set(), "1": {"q2"}},
    "q2": {"0": {"q2"}, "1": {"q2"}},
    "q3": {"0": {"q4"}, "1": set()},
    "q4": {"0": {"q4"}, "1": {"q4"}}
}

print("Q:",Q)
print("Σ:",sigma)
print("q0:",q0)
print("F:",F)

print("δ:")
print("Estado |     0    |     1"     )
print("q0","     {q0, q3}", "  {q0, q1}")
print("q1", "     { }", "       {q2}")
print("q2", "     {q2}", "      {q2}")
print("q3", "     {q4}", "      { }")
print("q4", "     {q4}", "      {q4}")

def ordenar(estados):
    return sorted(estados, key=lambda x: int(x[1:]))

def mostrar_recursivo(w):
    for i in range(len(w), 0, -1):        # recorre la cadena más larga hasta la más corta
        prefijo = w[:i]                   # el prefijo actual
        if i == 1:                        # caso base de un solo símbolo
            estados = delta[q0][prefijo]  # aplica δ al estado inicial con ese símbolo
            print(f"δ'(q0, {prefijo}) = δ(q0, {prefijo}) = {','.join(ordenar(estados))}")
        else:                     
            anterior = w[:i-1]            # prefijo anterior sin el último símbolo
            ultimo = w[i-1]               # último símbolo del prefijo actual
            print(f"δ'(q0, {prefijo}) = δ'(δ'(q0, {anterior}), {ultimo})")

def delta_hat_reversa(states, w):
    current_states = states              
    print(f"\nRecorrido en reversa")
    print(f"Estado inicial: {','.join(ordenar(current_states))}")
    for symbol in reversed(w):            # recorre la cadena al revés
        next_states = set()               # conjunto de estados siguientes
        for state in current_states:      # para cada estado actual
            if symbol in delta[state]:    # si existe transición con ese símbolo
                next_states |= delta[state][symbol]  # agrega los estados alcanzados
        print(f"Símbolo {symbol}: δ({','.join(ordenar(current_states))}, {symbol}) = {','.join(ordenar(next_states))}")
        current_states = next_states      
    return current_states   

def evaluar_cadena(w):
    print(f"\nEvaluando cadena: {w}")

    mostrar_recursivo(w)

    final_states_rev = delta_hat_reversa({q0}, w)

    # verifica si el conjunto final contiene estados de F
    print(f"\nδ'(q0, {w[::-1]}) = {','.join(ordenar(final_states_rev))}")
    if final_states_rev & F:  # intersección con estados finales
        print(f"La cadena {w} es aceptada (finales: {','.join(ordenar(final_states_rev & F))})\n")
    else:
        print(f"La cadena {w} no es aceptada\n")

# evaluar las cadenas
cadenas = ["101", "01001"]
for w in cadenas:
    evaluar_cadena(w)

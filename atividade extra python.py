def uniao(conjunto1, conjunto2):
    for i in range(len(conjunto2)):
        if not conjunto2[i] in conjunto1:
            conjunto1.append(conjunto2[i])
    return conjunto1

def diferenca(conjunto1, conjunto2):
    for i in range(len(conjunto2)):
        if conjunto2[i] in conjunto1:
            conjunto1.remove(conjunto2[i])
    return conjunto1

def intersecao(conjunto1, conjunto2):
    novoConjunto = []
    for i in range(len(conjunto2)):
        if conjunto2[i] in conjunto1:
            novoConjunto.append(conjunto2[i])
    return novoConjunto

A = [3,5,7,9]
B = [2,3,4,5,6]
print(f"Ex 1:\nA = {A}, B = {B}, A +- B = {uniao(diferenca(A.copy(), B.copy()), diferenca(B.copy(), A.copy()))}\n")
print(f"Ex 2:\nA = {A}, B = {B}, (A u B) - (A ^ B) = {diferenca(uniao(A.copy(), B.copy()), intersecao(A.copy(), B.copy()))} = (igual ao de cima)\n")
print(f"Ex 3:\nA = {A}, B = {B}, A +- A = {uniao(diferenca(A.copy(), A.copy()), diferenca(A.copy(), A.copy()))}, [vazio] +- A = {uniao(diferenca([], A.copy()), diferenca(A.copy(), []))}")


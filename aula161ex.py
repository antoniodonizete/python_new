import copy
from dados import produtos

# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
novos_produtos = [
    {**p, #cria novo dicionario
     'preco': round(p['preco'] * 1.1,2)} #nova chave preço - round e ,2 no fim para ficar 2 casas decimais
    for p in copy.deepcopy(produtos)
]
print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()


# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

print(*produtos_ordenados_por_nome, sep='\n')
print()

# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
    
)
print(*produtos_ordenados_por_preco, sep='\n')
print()

print(*produtos, sep='\n')

#####################################################################


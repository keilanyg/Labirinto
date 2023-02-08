# Labirinto

Descrições de permissões do sistema e suas funcionalidades:

- O rato tenta escapar do labirinto, sistematicamente, em todas as rotas.
- Se chegar em um beco sem saída, ele retornar alguns passos por caminhos já percorridos até que tenha um ou mais caminhos não testados.
- Mesmo próximo a saída, ele sempre testa os caminhos não percorridos na mesma ordem: direita, esquerda, baixo e cima.
- Para evitar cair em um loop infinito de testar todos os caminhos, os quais já foram investigados, cada posição visitada deve ser marcada.

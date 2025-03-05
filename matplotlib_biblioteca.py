import matplotlib.pyplot as plt  # Corrigido para importar o módulo pyplot corretamente

estudantes = ['JOÃO', 'MARIA', 'JOSÉ']
notas = [8.5, 9, 6.5]

plt.bar(x=estudantes, height=notas)  # Corrigido "heigth" para "height" e "nota" para "notas"
plt.xlabel('Estudantes')  # Adicionando rótulo para o eixo x
plt.ylabel('Notas')       # Adicionando rótulo para o eixo y
plt.title('Notas dos Estudantes')  # Adicionando um título ao gráfico
plt.show()  # Para exibir o gráfico
from bokeh.plotting import figure, output_file, show
import numpy as np

# cria um array de dados aleatórios
x = np.random.rand(100)
y = np.random.rand(100)

# especifica o arquivo de saída e o título do gráfico
output_file("grafico.html")
p = figure(title='Exemplo de gráfico de dispersão',
           x_axis_label='x',
           y_axis_label='y')

# adiciona os dados ao gráfico
p.circle(x, y, size=5)

# exibe o gráfico
show(p)

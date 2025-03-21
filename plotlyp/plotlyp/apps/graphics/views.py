import numpy as np

import plotly.express as px
import plotly.graph_objects as go

from django.shortcuts import render


# region Basic Plotly
def plotly_main(request):
    return render(request, 'main.html', {})


def plotly_graph(request):
    title = "Barras"

    # Datos de ejemplo para el gráfico
    data = {
        'lote': ['A', 'B', 'C', 'D'],
        'clientes': [10, 15, 13, 18]
    }
    
    # Crear el gráfico con Plotly
    fig = px.bar(data, x='lote', y='clientes', title="Gráfico de barras")
    
    # Convertir el gráfico a HTML
    graph_html = fig.to_html(full_html=False)

    # Renderizar la página con el gráfico
    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_graph_line(request):
    title = "Lineas"

    data = {
        'ventas': [1, 2, 3, 4, 5],
        'total': [10, 15, 7, 20, 12],
    }

    fig = px.line(data, x='ventas', y='total', title="Gráfico de Lineas")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_graph_scatter_plot(request):
    title = "Dispersión"

    df = px.data.iris()

    """
         sepal_length  sepal_width  petal_length  petal_width    species  species_id
    0             5.1          3.5           1.4          0.2     setosa           1
    1             4.9          3.0           1.4          0.2     setosa           1
    2             4.7          3.2           1.3          0.2     setosa           1
    3             4.6          3.1           1.5          0.2     setosa           1
    4             5.0          3.6           1.4          0.2     setosa           1
    ..            ...          ...           ...          ...        ...         ...
    145           6.7          3.0           5.2          2.3  virginica           3
    146           6.3          2.5           5.0          1.9  virginica           3
    147           6.5          3.0           5.2          2.0  virginica           3
    148           6.2          3.4           5.4          2.3  virginica           3
    149           5.9          3.0           5.1          1.8  virginica           3
    """

    fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species", title="Gráfico de Dispersión")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_graph_area(request):
    title = "Áreas"

    df = px.data.gapminder().query("country == 'Brazil'")

    """
        country continent  year  lifeExp        pop    gdpPercap iso_alpha  iso_num
    168  Brazil  Americas  1952   50.917   56602560  2108.944355       BRA       76
    169  Brazil  Americas  1957   53.285   65551171  2487.365989       BRA       76
    170  Brazil  Americas  1962   55.665   76039390  3336.585802       BRA       76
    171  Brazil  Americas  1967   57.632   88049823  3429.864357       BRA       76
    172  Brazil  Americas  1972   59.504  100840058  4985.711467       BRA       76
    173  Brazil  Americas  1977   61.489  114313951  6660.118654       BRA       76
    174  Brazil  Americas  1982   63.336  128962939  7030.835878       BRA       76
    175  Brazil  Americas  1987   65.205  142938076  7807.095818       BRA       76
    176  Brazil  Americas  1992   67.057  155975974  6950.283021       BRA       76
    177  Brazil  Americas  1997   69.388  168546719  7957.980824       BRA       76
    178  Brazil  Americas  2002   71.006  179914212  8131.212843       BRA       76
    179  Brazil  Americas  2007   72.390  190010647  9065.800825       BRA       76
    """

    fig = px.area(df, x="year", y="pop", title="Crecimiento de la población en Brasil")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_graph_pie(request):
    title = "Pastel"
    
    df = px.data.tips()

    """
         total_bill   tip     sex smoker   day    time  size
    0         16.99  1.01  Female     No   Sun  Dinner     2
    1         10.34  1.66    Male     No   Sun  Dinner     3
    2         21.01  3.50    Male     No   Sun  Dinner     3
    3         23.68  3.31    Male     No   Sun  Dinner     2
    4         24.59  3.61  Female     No   Sun  Dinner     4
    ..          ...   ...     ...    ...   ...     ...   ...
    239       29.03  5.92    Male     No   Sat  Dinner     3
    240       27.18  2.00  Female    Yes   Sat  Dinner     2
    241       22.67  2.00    Male    Yes   Sat  Dinner     2
    242       17.82  1.75    Male     No   Sat  Dinner     2
    243       18.78  3.00  Female     No  Thur  Dinner     2
    """

    fig = px.pie(df, values='total_bill', names='day', title="Distribución de ingresos por día")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_grapg_histograms(request):
    title = "Histograma"
    df = px.data.tips()

    """
         total_bill   tip     sex smoker   day    time  size
    0         16.99  1.01  Female     No   Sun  Dinner     2
    1         10.34  1.66    Male     No   Sun  Dinner     3
    2         21.01  3.50    Male     No   Sun  Dinner     3
    3         23.68  3.31    Male     No   Sun  Dinner     2
    4         24.59  3.61  Female     No   Sun  Dinner     4
    ..          ...   ...     ...    ...   ...     ...   ...
    239       29.03  5.92    Male     No   Sat  Dinner     3
    240       27.18  2.00  Female    Yes   Sat  Dinner     2
    241       22.67  2.00    Male    Yes   Sat  Dinner     2
    242       17.82  1.75    Male     No   Sat  Dinner     2
    243       18.78  3.00  Female     No  Thur  Dinner     2
    """
    fig = px.histogram(df, x="total_bill", title="Distribución de cuentas en un restaurante")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_grapg_box(request):
    title = "Caja"
    
    df = px.data.tips()

    """
         total_bill   tip     sex smoker   day    time  size
    0         16.99  1.01  Female     No   Sun  Dinner     2
    1         10.34  1.66    Male     No   Sun  Dinner     3
    2         21.01  3.50    Male     No   Sun  Dinner     3
    3         23.68  3.31    Male     No   Sun  Dinner     2
    4         24.59  3.61  Female     No   Sun  Dinner     4
    ..          ...   ...     ...    ...   ...     ...   ...
    239       29.03  5.92    Male     No   Sat  Dinner     3
    240       27.18  2.00  Female    Yes   Sat  Dinner     2
    241       22.67  2.00    Male    Yes   Sat  Dinner     2
    242       17.82  1.75    Male     No   Sat  Dinner     2
    243       18.78  3.00  Female     No  Thur  Dinner     2
    """

    fig = px.box(df, x="day", y="total_bill", color="sex", title="Diagrama de Caja de Cuentas por Día")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_grapg_violin(request):
    title = "Violin"
    
    df = px.data.tips()

    """
         total_bill   tip     sex smoker   day    time  size
    0         16.99  1.01  Female     No   Sun  Dinner     2
    1         10.34  1.66    Male     No   Sun  Dinner     3
    2         21.01  3.50    Male     No   Sun  Dinner     3
    3         23.68  3.31    Male     No   Sun  Dinner     2
    4         24.59  3.61  Female     No   Sun  Dinner     4
    ..          ...   ...     ...    ...   ...     ...   ...
    239       29.03  5.92    Male     No   Sat  Dinner     3
    240       27.18  2.00  Female    Yes   Sat  Dinner     2
    241       22.67  2.00    Male    Yes   Sat  Dinner     2
    242       17.82  1.75    Male     No   Sat  Dinner     2
    243       18.78  3.00  Female     No  Thur  Dinner     2
    """

    fig = px.violin(df, x="day", y="total_bill", color="sex", box=True, title="Gráfico de Violín")

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_grapg_choroplethics(request):
    title = "Coropléticos"

    df = px.data.gapminder().query("year == 2007")

    """
                     country continent  year  ...     gdpPercap  iso_alpha  iso_num
    11           Afghanistan      Asia  2007  ...    974.580338        AFG        4
    23               Albania    Europe  2007  ...   5937.029526        ALB        8
    35               Algeria    Africa  2007  ...   6223.367465        DZA       12
    47                Angola    Africa  2007  ...   4797.231267        AGO       24
    59             Argentina  Americas  2007  ...  12779.379640        ARG       32
    ...                  ...       ...   ...  ...           ...        ...      ...
    1655             Vietnam      Asia  2007  ...   2441.576404        VNM      704
    1667  West Bank and Gaza      Asia  2007  ...   3025.349798        PSE      275
    1679         Yemen, Rep.      Asia  2007  ...   2280.769906        YEM      887
    1691              Zambia    Africa  2007  ...   1271.211593        ZMB      894
    1703            Zimbabwe    Africa  2007  ...    469.709298        ZWE      716
    """

    fig = px.choropleth(df, locations="iso_alpha", color="gdpPercap",
                     hover_name="country", color_continuous_scale=px.colors.sequential.Plasma,
                     title="GDP per Cápita en 2007")
    
    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_grapg_heatmaps(request):
    title = "Calor"
    
    data = np.random.rand(10, 10)

    """
    [[0.0021164  0.10764098 0.7299582  0.30338671 0.71809212 0.95424194
    0.90406331 0.69357935 0.47490954 0.46034667]
    [0.5403301  0.52955935 0.44242415 0.71449649 0.35174473 0.25715469
    0.122299   0.60609302 0.68394597 0.90560197]
    [0.60938921 0.29221458 0.23297553 0.35543731 0.38907294 0.39266806
    0.99761709 0.48131628 0.89209373 0.41247162]
    [0.1503145  0.77710727 0.34575166 0.08106405 0.14690602 0.93399694
    0.23152538 0.5580246  0.47058381 0.19469444]
    [0.89044497 0.97571801 0.14920761 0.54463006 0.65725596 0.22708782
    0.48571611 0.05128787 0.38469338 0.03252574]
    [0.47468359 0.98123726 0.87326145 0.28545274 0.26490487 0.35318964
    0.10700189 0.37908616 0.42609605 0.28605546]
    [0.62843551 0.4543277  0.21969965 0.5313994  0.3057985  0.01400186
    0.32232229 0.26427236 0.94382037 0.11408834]
    [0.85756904 0.29696284 0.54063333 0.51017764 0.02487904 0.99547032
    0.70605646 0.07559412 0.70258362 0.23825185]
    [0.07797717 0.89049214 0.96444054 0.60459087 0.18605817 0.54066333
    0.43815248 0.95140149 0.73892075 0.72401617]
    [0.30880623 0.43326472 0.05006371 0.42951437 0.17445408 0.9026255
    0.5848922  0.20233499 0.88733133 0.22891285]]
    """

    fig = go.Figure(data=go.Heatmap(z=data, colorscale='Viridis'))

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})

def plotly_grapg_3d(request):
    title = "3D"

    x = np.linspace(-5, 5, 100)
    y = np.linspace(-5, 5, 100)
    x, y = np.meshgrid(x, y)
    z = np.sin(np.sqrt(x**2 + y**2))

    fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

    fig.update_layout(
        title='Gráfico 3D de una superficie sinusoidal',
        scene=dict(
            xaxis_title='Eje X',
            yaxis_title='Eje Y',
            zaxis_title='Eje Z'
        ),
        autosize=False,
        width=800,
        height=800,
        margin=dict(l=65, r=50, b=65, t=90)
    )

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_grapg_slider(request):
    title = "SLIDE"
    fig = go.Figure()

    # Add traces, one for each slider step
    for step in np.arange(0, 5, 0.1):
        fig.add_trace(
            go.Scatter(
                visible=False,
                line=dict(color="#00CED1", width=6),
                name="𝜈 = " + str(step),
                x=np.arange(0, 10, 0.01),
                y=np.sin(step * np.arange(0, 10, 0.01))))

    # Make 10th trace visible
    fig.data[10].visible = True

    # Create and add slider
    steps = []
    for i in range(len(fig.data)):
        step = dict(
            method="update",
            args=[{"visible": [False] * len(fig.data)},
                {"title": "Slider switched to step: " + str(i)}],  # layout attribute
        )
        step["args"][0]["visible"][i] = True  # Toggle i'th trace to "visible"
        steps.append(step)

    sliders = [dict(
        active=10,
        currentvalue={"prefix": "Frequency: "},
        pad={"t": 50},
        steps=steps
    )]

    fig.update_layout(
        sliders=sliders
    )

    graph_html = fig.to_html(full_html=False)

    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})

# endregion Basic Plotly

# region PX | GO
def plotly_graph_scatter_plot_px(request):
    title = "Dispersión PX"
    df = px.data.iris()
    fig = px.scatter(df, x='sepal_width', y='sepal_length', color='species', title='Gráfico de Dispersión Iris')
    graph_html = fig.to_html(full_html=False)
    
    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})


def plotly_graph_scatter_plot_go(request):
    title = "Dispersión GO"
    df = px.data.iris()
    fig = go.Figure(data=go.Scatter(x=df['sepal_width'], y=df['sepal_length'], mode='markers', marker=dict(color=df['species_id'])))
    graph_html = fig.to_html(full_html=False)
    
    return render(request, 'plotly_graph.html', {'graph_html': graph_html, 'title': title})
# endregion PX | GO

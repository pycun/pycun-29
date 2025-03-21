from django.urls import path
from . import views
from plotlyp.apps.graphics.views import (
    plotly_main, plotly_graph, plotly_graph_line, plotly_graph_scatter_plot, plotly_graph_area, plotly_graph_pie,
    plotly_grapg_histograms, plotly_grapg_box, plotly_grapg_violin, plotly_grapg_choroplethics, plotly_grapg_heatmaps,
    plotly_graph_scatter_plot_px, plotly_graph_scatter_plot_go, plotly_grapg_3d, plotly_grapg_slider)

urlpatterns = [
    path('', plotly_main, name='main'),
    path('plotly-graph/bars/', plotly_graph, name='plotly_graph_bars'),
    path('plotly-graph/lines/', plotly_graph_line, name='plotly_graph_line'),
    path('plotly-graph/scatter/', plotly_graph_scatter_plot, name='plotly_graph_scatter_plot'),
    path('plotly-graph/area/', plotly_graph_area, name='plotly_graph_area'),
    path('plotly-graph/pie/', plotly_graph_pie, name='plotly_graph_pie'),
    path('plotly-graph/histograms/', plotly_grapg_histograms, name='plotly_grapg_histograms'),
    path('plotly-graph/box/', plotly_grapg_box, name='plotly_grapg_box'),
    path('plotly-graph/violin/', plotly_grapg_violin, name='plotly_grapg_violin'),
    path('plotly-graph/choroplethics/', plotly_grapg_choroplethics, name='plotly_grapg_choroplethics'),
    path('plotly-graph/heatmaps/', plotly_grapg_heatmaps, name='plotly_grapg_heatmaps'),
    path('plotly-graph/3d/', plotly_grapg_3d, name='plotly_grapg_3d'),
    path('plotly-graph/slide/', plotly_grapg_slider, name='plotly_grapg_slider'),

    path('plotly-graph/scatter/px/', plotly_graph_scatter_plot_px, name='plotly_graph_scatter_plot_px'),
    path('plotly-graph/scatter/go/', plotly_graph_scatter_plot_go, name='plotly_graph_scatter_plot_go'),
]

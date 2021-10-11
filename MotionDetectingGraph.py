from bokeh.models.glyphs import Quad
from MotionDetecting import df
from bokeh.plotting import figure, show, output_file

p = figure(x_axis_type='datetime', height=100, width=500, title="Motion Graph")
q = p.quad(left=df["Start"], right=df["End"], bottom=0, top=1, color="green")

output_file("./results/MotionDetectingGraph.html")

show(p)
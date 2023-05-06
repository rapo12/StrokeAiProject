import streamlit as st
import pandas as pd
from plotnine import ggplot, aes, facet_grid, labs, geom_col,theme_xkcd
import plotly.express as px
from io import BytesIO
from PIL import Image

data_balanced = pd.read_csv("data/data_balanced.csv")


# Load data


# Define function to create plot
# Define function to create plot
def create_plot(data):
    plot = (
            ggplot(data)
            + facet_grid(facets="~gender")
            + aes(x="age_interval", y="gender", fill="stroke_c")
            + labs(
        x="age_interval",
        y="count",
    )
            + geom_col()
            + theme_xkcd()
    )
    return plot

# Streamlit app
st.title("Plot Title")
plot = create_plot(data_balanced)

# Convert plot to Matplotlib figure
fig = plot.draw()

# Save figure as image and read back as bytes
buf = BytesIO()
fig.savefig(buf, format='png')
buf.seek(0)
img_bytes = buf.read()

# Convert image bytes to Plotly figure
plotly_fig = px.imshow(Image.open(BytesIO(img_bytes)))

# Display plot
st.plotly_chart(plotly_fig)
import warnings
warnings.filterwarnings('ignore')

from mlpipeline import Pipline
import streamlit as st

st.set_page_config(layout='wide')

st.markdown(
    body="<h3 style='text-align: center;'>Stellar Classification</h3>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    alpha = st.slider(label='Ascension angle', min_value=0.0, max_value=360.0, value=150.0)
    delta = st.slider(label='Declination angle', min_value=0.0, max_value=360.0, value=150.0)
    u = st.slider(label='Ultraviolet', min_value=0.0, max_value=30.0, value=22.0)
    g = st.slider(label='Green', min_value=0.0, max_value=30.0, value=22.0)
    r = st.slider(label='Red', min_value=0.0, max_value=30.0, value=25.0)
    i = st.slider(label='Infrared (I)', min_value=0.0, max_value=30.0, value=10.0)
    z = st.slider(label='Infrared (Z)', min_value=0.0, max_value=30.0, value=5.0)
    redshift = st.slider(label='Redshift', min_value=0.0, max_value=10.0, value=2.0)

data = [[alpha, delta, u, g, r, i, z, redshift]]
pipe = Pipline(data=data)
conclusion, fig, pred_class = pipe.pipeline()
image_credits = "A random {} image taken from nasa.gov image gallery.".format(pred_class.lower())

conclusion = "<p style='text-align: center;'>{}</p>".format(conclusion)
image_credits = "<p style='text-align: center;'>{}</p>".format(image_credits)

with col2:
    st.markdown(body=conclusion, unsafe_allow_html=True)
    st.plotly_chart(figure_or_data=fig, use_container_width=True)
    st.markdown(body=image_credits, unsafe_allow_html=True)

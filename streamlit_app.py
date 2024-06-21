import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
DEBUG = True
st.set_page_config(layout = "wide")
hide_streamlit_style = """
<style>
#root > div:nth-child(1) > div.withScreencast > div > div > header {visibility:hidden;height:0px;}
#root > div:nth-child(1) > div.withScreencast > div > div > div > section > div.block-container.st-emotion-cache-1jicfl2.ea3mdgi5 {padding: 1rem}
footer {visibility: hidden;}
</style>
"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

col1, col2, col3 = st.columns([6,1,6])

with col1:
    st.write("")

with col2:
    st.image(
        "images/logo_black.png",
        width=250
    )

with col3:
    st.write("")
st.divider()
iframe_src = "https://embed.waze.com/iframe?zoom=12&lat=-25.436144&lon=-49.351273&ct=livemap&utm_medium=fullscreen_map"
proportions = [0.9, 0.1]
col1, col2 = st.columns(proportions)
height = 1050
width = 1920
with col1:
    iframe_html = f"""
         <div style="width: {width*proportions[0]};height: {height-150}px; overflow: hidden;">
            <iframe 
                src="https://embed.waze.com/iframe?zoom=12&lat=-25.436144&lon=-49.351273&ct=livemap&utm_medium=fullscreen_map" 
                width="{width*proportions[0]}" 
                height="{height}"
                style="position: 
                relative; 
                top: -100px;
                bottom: -100px;">
            </iframe> 
        </div>
    """
    components.html(
        iframe_html,
        height=height,
        
    )
with col2:
    html_source = """
        <a class="weatherwidget-io" href="https://forecast7.com/en/n25d43n49d27/curitiba/" data-label_1="CURITIBA" data-label_2="WEATHER" data-theme="pure" >CURITIBA WEATHER</a>
        <script>
        !function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0];if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src='https://weatherwidget.io/js/widget.min.js';fjs.parentNode.insertBefore(js,fjs);}}(document,'script','weatherwidget-io-js');
        </script>
    """
    components.html(
        html_source,
        height= height,
        width = proportions[1]*width
    )
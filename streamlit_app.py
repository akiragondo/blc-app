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
proportions = [0.9, 0.1]
col1, col2 = st.columns(proportions)
height = 1050
width = 1920

radius = 80
border_size = 1
x = 888
y = 391

with col1:
    iframe_html = f"""
         <div style="width: {width*proportions[0]};height: {height-150}px; overflow: hidden;">
            <iframe 
                src="https://embed.waze.com/iframe?zoom=10&lat=-25.52613&lon=-49.379926&ct=livemap&utm_medium=fullscreen_map" 
                width="{width*proportions[0]}" 
                height="{height}"
                style="position: 
                relative; 
                top: -100px;
                bottom: -100px;">
            </iframe> 
            <div
                style = "
                    width: {radius+border_size}px;
                    position: absolute;
                    left: {x-radius/2}px;
                    top: {y}px;
                    z-index: 998;
                ">
            <img src="https://upload.wikimedia.org/wikipedia/commons/c/cd/Volvo-Spread-Word-Mark-Black.svg"/>
            </div>
    """
    components.html(
        iframe_html,
        height=height
    )
with col2:
    html_source = """
        <script>
        (function(d, s, id) {
            if (d.getElementById(id)) {
                if (window.__TOMORROW__) {
                    window.__TOMORROW__.renderWidget();
                }
                return;
            }
            const fjs = d.getElementsByTagName(s)[0];
            const js = d.createElement(s);
            js.id = id;
            js.src = "https://www.tomorrow.io/v1/widget/sdk/sdk.bundle.min.js";

            fjs.parentNode.insertBefore(js, fjs);
        })(document, 'script', 'tomorrow-sdk');
        </script>

        <div class="tomorrow"
           data-location-id="011524"
           data-language="EN"
           data-unit-system="METRIC"
           data-skin="light"
           data-widget-type="upcoming"
           style="padding-bottom:22px;position:relative;"
        >
          <a
            href="https://www.tomorrow.io/weather-api/"
            rel="nofollow noopener noreferrer"
            target="_blank"
            style="position: absolute; bottom: 0; transform: translateX(-50%); left: 50%;"
          >
            <img
              alt="Powered by the Tomorrow.io Weather API"
              src="https://weather-website-client.tomorrow.io/img/powered-by.svg"
              width="250"
              height="18"
            />
          </a>
        </div>
    """
    components.html(
        html_source,
        height= height,
        width = proportions[1]*width
    )
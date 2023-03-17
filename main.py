import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('streamlit 超入門')

st.write('Display Image')

img = Image.open('85646589_p0.png')
st.image(img, caption='Irustrios',use_column_width=True)




st.write('プログレスバーの表示')
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i + 1}')
    bar.progress(i + 1)
    time.sleep(0.01)


# df = pd.DataFrame({
#     '1列目':[1, 2, 3, 4],
#     '2列目':[10, 20, 30, 40]
# })
# st.table(df.style.highlight_min(axis = 0))

"""
# ぬぬ
"""


# text = st.sidebar.text_input('あなたの趣味を教えて')
# text = st.sidebar.slider('あなたの身長', 0 ,100, 50)

left_column, center_column,right_column = st.columns(3)


button = left_column.button('右columnに文字を表示')
if button:
    right_column.write('ここは右columnです')

expander = st.expander('問い合わせ')
expander.write('問い合わせ内容を書く')

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50,50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)


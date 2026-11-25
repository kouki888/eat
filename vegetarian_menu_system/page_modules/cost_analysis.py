import streamlit as st
from services.cost_service import suggested_price
def render():
    st.title('成本與售價分析')
    cost = st.number_input('每批食材成本（元）', min_value=0.0, value=660.0)
    qty = st.number_input('製作份數', min_value=1, value=100)
    ratio = st.slider('目標食材成本率（%）', 10, 90, 40)
    a,b = st.columns(2)
    a.metric('每份食材成本', f'{cost/qty:.2f} 元')
    b.metric('每份建議售價', f'{suggested_price(cost/qty, ratio/100)} 元')
    st.caption('售價向上取至5元倍數，未包含完整營運成本。')

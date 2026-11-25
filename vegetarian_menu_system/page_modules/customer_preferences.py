import streamlit as st
def render():
    st.title('顧客喜好')
    with st.form('preferences'):
        foods = st.multiselect('喜歡的食材', ['豆腐','高麗菜','南瓜','菇類','豆皮','地瓜'])
        tastes = st.multiselect('口味偏好', ['清淡','香辣','酸甜','濃郁'])
        price = st.slider('每餐可接受價格（元）', 30, 200, 80)
        if st.form_submit_button('提交偏好'):
            st.session_state.preferences = dict(foods=foods, tastes=tastes, price=price)
            st.success('已暫存本次偏好，尚未寫入正式資料庫。')

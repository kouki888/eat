import streamlit as st
def render():
    st.title('AI 菜單推薦')
    s = st.session_state.settings
    with st.form('recommend'):
        budget = st.number_input('每月總預算（元）', min_value=1, value=s['budget'])
        people = st.number_input('每日供餐人數', min_value=1, value=s['people'])
        dishes = st.number_input('每日菜色數', min_value=1, value=s['dishes'])
        required = st.text_input('店家指定菜色（以逗號分隔）')
        excluded = st.text_input('排除食材（以逗號分隔）')
        submitted = st.form_submit_button('確認推薦條件')
    if submitted:
        st.session_state.recommendation_request = dict(budget=budget, people=people, dishes=dishes, required=required, excluded=excluded)
        st.success('已暫存推薦條件（本次工作階段）')
        st.info('推薦演算法尚未實作，因此目前不生成菜單。')

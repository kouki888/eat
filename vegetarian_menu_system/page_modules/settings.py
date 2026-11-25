import streamlit as st
def render():
    st.title('系統設定')
    s = st.session_state.settings
    with st.form('settings'):
        budget = st.number_input('每月總預算', min_value=1, value=s['budget'])
        days = st.number_input('每月營業天數', min_value=1, max_value=31, value=s['days'])
        people = st.number_input('每日供餐人數', min_value=1, value=s['people'])
        dishes = st.number_input('每日菜色數', min_value=1, value=s['dishes'])
        food_ratio = st.slider('食材預算占比（%）', 1, 100, s['food_ratio'])
        if st.form_submit_button('儲存設定'):
            st.session_state.settings = dict(budget=budget, days=days, people=people, dishes=dishes, food_ratio=food_ratio)
            st.success('已儲存至本次工作階段')

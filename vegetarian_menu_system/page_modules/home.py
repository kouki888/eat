import streamlit as st
from services.database import load_menu
def render():
    st.title('營運總覽')
    s = st.session_state.settings
    a,b,c,d = st.columns(4)
    a.metric('每月總預算', f"${s['budget']:,}")
    b.metric('每日食材預算', f"${s['budget']*s['food_ratio']/100/s['days']:,.0f}")
    try:
        c.metric('菜色資料數', len(load_menu()))
    except (ValueError, OSError) as e:
        c.metric('菜色資料數', '讀取失敗'); st.error(str(e))
    d.metric('每日供餐人數', s['people'])
    st.info('目前為介面開發階段，尚未串接正式 AI 與營運資料。')
    st.subheader('系統開發進度')
    st.write('網頁架構 → 資料庫 → AI 推薦 → 營運回饋')

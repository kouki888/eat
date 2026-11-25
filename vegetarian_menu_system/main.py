from pathlib import Path
import streamlit as st
from config import DEFAULT_SETTINGS
from page_modules import home, recommendation, menu_database, ingredients, cost_analysis, customer_preferences, weather, feedback, settings
st.set_page_config(page_title='平價素食菜單推薦系統', page_icon='🥬', layout='wide')
if 'settings' not in st.session_state:
    st.session_state.settings = DEFAULT_SETTINGS.copy()
css = Path(__file__).parent / 'assets' / 'style.css'
st.markdown(f'<style>{css.read_text(encoding="utf-8")}</style>', unsafe_allow_html=True)
pages = {'首頁總覽':home, 'AI 菜單推薦':recommendation, '菜單資料庫':menu_database, '食材管理':ingredients, '成本分析':cost_analysis, '顧客喜好':customer_preferences, '天氣資訊':weather, '剩菜分析':feedback, '系統設定':settings}
with st.sidebar:
    st.title('🥬 智慧素食餐廳')
    page = st.radio('功能選單', list(pages))
    st.caption('MVP 開發版本｜測試資料')
pages[page].render()

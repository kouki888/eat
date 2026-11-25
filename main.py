
import streamlit as st
from page_modules import home

# 網頁基本設定
st.set_page_config(
    page_title="平價素食自助餐廳菜單推薦系統",
    page_icon="🥬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 側邊導覽列
with st.sidebar:

    st.title("🥬 智慧素食餐廳")

    st.caption("AI Vegetarian Menu System")

    st.divider()

    page = st.radio(
        "功能選單",
        [
            "🏠 首頁總覽",
            "🤖 AI 菜單推薦",
            "📋 菜單資料庫",
            "🥕 食材管理",
            "💰 成本分析",
            "👥 顧客喜好",
            "🌤️ 天氣與季節",
            "📊 剩菜分析",
            "⚙️ 系統設定"
        ]
    )

    st.divider()

    st.caption("系統版本：V1.0")

# 頁面切換
if page == "🏠 首頁總覽":
    home.render()

else:
    st.title(page)
    st.info("此功能尚未開發")

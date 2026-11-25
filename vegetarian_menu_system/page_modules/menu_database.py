import streamlit as st
from services.database import load_menu
def render():
    st.title('菜單資料庫')
    try:
        df = load_menu()
    except (ValueError, OSError) as e:
        st.error(str(e)); return
    q = st.text_input('搜尋菜色或食材')
    if q:
        df = df[df['菜單名稱'].astype(str).str.contains(q, regex=False) | df['食材'].astype(str).str.contains(q, regex=False)]
    st.caption(f'共 {len(df)} 筆｜目前資料為模擬資料')
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.download_button('下載目前資料', df.to_csv(index=False).encode('utf-8-sig'), 'menu.csv', 'text/csv')

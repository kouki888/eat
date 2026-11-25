
import streamlit as st

def render():

    st.title("平價素食自助餐廳菜單推薦系統")

    st.subheader("歡迎使用智慧菜單管理平台")

    st.write(
        "透過人工智慧、食材成本、顧客喜好、"
        "天氣及季節資訊，協助餐廳規劃每日菜單。"
    )

    st.divider()

    st.subheader("營運總覽")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("每月總預算", "NT$100,000")

    with col2:
        st.metric("每日供餐人數", "100 人")

    with col3:
        st.metric("菜單資料數量", "尚未匯入")

    with col4:
        st.metric("本週菜單", "尚未生成")

    st.divider()

    st.subheader("本週菜單規劃")

    days = st.columns(5)

    weekdays = [
        "星期一",
        "星期二",
        "星期三",
        "星期四",
        "星期五"
    ]

    for col, day in zip(days, weekdays):

        with col:

            with st.container(border=True):

                st.markdown(f"### {day}")

                st.caption("尚未安排菜單")

    st.divider()

    st.subheader("系統公告")

    st.info("目前系統正在開發中，尚未串接正式資料庫。")

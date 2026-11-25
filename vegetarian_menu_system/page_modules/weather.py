import streamlit as st
def render():
    st.title('天氣與季節資訊')
    st.selectbox('供餐地區', ['台中市','台北市','高雄市','台南市'])
    st.info('尚未串接中央氣象署 API，目前不顯示即時天氣。')

import streamlit as st
import pandas as pd
def render():
    st.title('剩菜分析')
    st.caption('模擬資料，可編輯測試')
    df = st.data_editor(pd.DataFrame({'星期':['週一','週二','週三','週四','週五'],'製作量(kg)':[50]*5,'剩菜量(kg)':[4,2,10,5,1]}), hide_index=True)
    if df.isna().any().any() or (df['製作量(kg)']<=0).any() or (df['剩菜量(kg)']<0).any() or (df['剩菜量(kg)']>df['製作量(kg)']).any():
        st.error('請確認製作量大於零，剩菜量介於零與製作量之間。'); return
    df['剩菜率(%)'] = df['剩菜量(kg)']/df['製作量(kg)']*100
    st.metric('整週剩菜率', f"{df['剩菜量(kg)'].sum()/df['製作量(kg)'].sum()*100:.1f}%")
    st.bar_chart(df.set_index('星期')['剩菜率(%)'])

import streamlit as st
def func_page_1():
    st.title('Page 1')
    
from datetime import datetime
st.title('Clock Time')
clock = st.empty()
while True:
    time = datetime.now().strftime("%H:%M:%S")
    clock.info('**Current time: ** %s' % (time))
    if time == '16:09:50':
        clock.empty()
        st.warning('Alarm!!')
        break

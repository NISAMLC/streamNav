import time

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
st.set_option('deprecation.showPyplotGlobalUse', False)



st.title('Navigation and Sidebar')

# st.sidebar.multiselect('Select A Team',['RR','RCB','CSK','MI'])

page = st.sidebar.radio('Navgation',['Home','About','Contact'])
df = pd.read_csv('Superstore.csv')

if page=='Home':
    feat = st.sidebar.multiselect('Select a Feature',df.columns,default='Profit')
    plt.plot(df[feat],df['Profit'])
    plt.title(f'{feat} vs  Profit ')
    plt.xlabel(feat)
    plt.ylabel('Profit')
    st.pyplot()
elif page=='About':
    st.write('Write Something About You Here')
    st.write('Uploading in Progress...')
    prog = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        prog.progress(i+1)
    st.balloons()
    st.write('Upload Completed ✔')

else:
    st.write('Your Contact Goes Here')

    st.error('You Encountered an Error')
    st.success('Successfully Submitted')
    st.info('Info Available Here')
    st.exception(SyntaxError('You Missed an End Quote'))
    st.warning('This method is depricated from 2021')


team = st.radio('Your Favorite IPL Team',['RR','CSK','RCB'])

bt1 = st.button('Submit')
if bt1:
    st.write(team)
    if team=='RR':
        st.write('Hurray')


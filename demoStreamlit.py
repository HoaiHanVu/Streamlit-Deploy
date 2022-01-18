from this import d
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = pd.read_csv('train.csv')

st.title('Trung tam Tin hoc')
st.header('Data Science')





menu = ['Display Text', 'Display Data', 'Display Chart', 'Display Interactive Widget']
choice = st.sidebar.selectbox('Menu', menu)

if choice == 'Display Text':
    st.subheader('Hanh trang tot nghiep Data Science')
    st.text('Khoa hoc duoc thiet ke nham on tap va bo sung kien thuc cho HV Data Science')
    st.markdown('### Co 5 chu de: ')
    st.write("""
    - Chu de 1
    - Chu de 2
    - Chu de 3
    """)
    st.write('### Ngon ngu lap trinh: Python')
    st.code ("st.display_text_function('Noi dung')", language = 'Python')

elif choice == 'Display Data':
    st.write('## Display Data')
    st.dataframe(data.head(3))
    st.table(data.head(3))
    st.json(data.head(2).to_json())

elif choice == 'Display Chart':
    st.write('## Display Chart')
    count_pclass = data[['PassengerId', 'Pclass']].groupby(['Pclass']).count()
    st.bar_chart(count_pclass)
    fig, ax = plt.subplots()
    ax = sb.boxplot(x = 'Pclass', y = 'Fare', data = data)
    st.pyplot(fig)

else:
    st.write('## Display Interaction Widget')
    st.write('### Input your information')
    name = st.text_input('Name:')
    sex = st.radio('Sex', options = ['Male', 'Female'])
    age = st.slider('Age', 1, 100, 1)
    jobtime = st.selectbox('You have', options = ['Part time job', 'Full time job'])
    hobbies = st.multiselect('Hobbies', options = ['Cooking', 'Reading', 'Writing', 'Travel', 'Others'])
    house = st.checkbox('Have house/apartment')
    submit = st.button('Submit')
    if submit:
        st.write('### Your Information: ')
        st.write('Name:', name,
        'Sex:', sex,
        'Age:', age,
        '- You have a', jobtime,
        ' and a house/apartment' if house else "",
        '- Hobbies:', ', '.join(map(str, hobbies)))
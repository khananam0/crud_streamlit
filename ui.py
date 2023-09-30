import mysql.connector as mycon
db = mycon.connect(host='localhost', user = 'root', password = 'root', database= 'pydb')
print(db)
db_curr = db.cursor()



import streamlit as st
st.title('CRUD operation')

tab1, tab2, tab3 = st.tabs(['Insert', 'Update', 'Delete'])

with tab1:
    no = st.number_input('Enter Product No: ')
    name= st.text_input('Enter Product No: ')
    loc= st.text_input('Enter Location: ')

    # st.button('submit')       

    if st.button('submit'):
        sql = 'insert into dmart(pro_no,pro_name,pro_loc) values (%s,%s,%s)'
        val = (no,name,loc)
        # val = (pro_no,pro_name,pro_loc)
        # st.write(pro_no,pro_name,pro_loc)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('Select * from dmart')
        st.table(db_curr.fetchall())



with tab2:
    no_u = st.number_input('Enter Product no update: ')
    name_u= st.text_input('Enter Product name: ')
    loc_u = st.text_input('Enter Loc: ') 

    if st.button('update'):
        sql = 'update dmart set pro_no = %s, pro_loc = %s, pro_name = %s where pro_loc = %s'
        val = (no_u,name_u,loc_u)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('Select * from dmart')
        st.table(db_curr.fetchall())
    

with tab3:
    no_u = st.number_input('Enter Product Delete: ')
    name_u= st.text_input('Enter Product name delete: ')
    loc_u = st.text_input('Enter Loc delete: ')

    if st.button('Delete'):
        sql = 'Delete from dmart where pro_no = %s'
        val = (no_u,name_u,loc_u)
        db_curr.execute(sql,val)
        db.commit()
        db_curr.execute('Select * from dmart')
        st.table(db_curr.fetchall())
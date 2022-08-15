import streamlit as st

st.set_page_config(page_title='Storeacts', page_icon='🖇️', initial_sidebar_state='collapsed', )
hide_streamlit_style = st.markdown("""
            <style>
            #MainMenu {visibility: visible;}
            footer {visibility: hidden;}
            footer {
                visibility: hidden;
            }
            footer:after {
                content:'STOREACTS 🖇️';
                visibility: visible;
                display: block;
                position: relative;
                #background-color: red;
                padding: 5px;
                top: 2px;
            }
            </style>
            """, unsafe_allow_html=True)
Contact_manager_design = st.markdown("""
<style>
.black-lives-matter {
  font-size: 2vw;
  line-height: 1vw;
  margin: 0;
  font-family: 'Red Hat Display', sans-serif;
  font-weight: 900;
  background-size: 40%;
  background-position: 50% 50%;
  -webkit-background-clip: text;
  color: grey;
  animation: zoomout 10s ease 500ms forwards;
}
</style>
<h1 class="black-lives-matter">Contacts Manager</h1>""", unsafe_allow_html=True)
Sub_heading_design = st.markdown("""
<style>
.black-lives-matter1 {
  font-size: .7vw;
  line-height: 1vw;
  margin: 0;
  font-family: 'Red Hat Display', sans-serif;
  font-weight: 900;
  background-size: 40%;
  background-position: 50% 50%;
  -webkit-background-clip: text;
  color:grey ;
  animation: zoomout 10s ease 500ms forwards;
}
</style>
<h1 class="black-lives-matter1">-> Manage Contacts with ease</h1>""", unsafe_allow_html=True)

st.text('')
st.text('')
b1,b2 = st.beta_columns(2)
def update_file(filename) -> None:
    input_user = st.text_input(f'-- Name --')
    input_no = st.text_input(f'-- Number --')

    file = open(filename, 'r')
    file_read = file.readlines()
    update_button = st.button('ADD', key=False)
    if update_button:
        if input_user == '':
            st.info('--- Fields Empty ---')
        elif not (input_no.isdigit()):
            st.info('--- Should be a digit ---')
        elif input_user+'\n' in file_read or input_no+'\n' in file_read:
            st.info('-- Name/Number Already Exists --')
        else:
            st.success('--Added--')
            file = open(filename, 'a')
            file.write(input_user + '\n')
            file.write(input_no + '\n')
            file.close()

def delete_item_from_file(delete_item, filename):
    file = open(filename, 'r')
    read_file: list = file.readlines()
    delete_button = st.button('Delete', key=False)
    if delete_button:
        if delete_item + '\n' not in read_file:
            st.info('-- Field Empty --')
        else:
            for i in range(len(read_file)):
                if read_file[i] == delete_item + '\n':
                    read_file.remove(read_file[i])
                    read_file.remove(read_file[i])
                    break
            file.close()
            file = open(filename, 'w')
            for i in read_file:
                file.write(i)
            file.close()
            st.success('Deleted')

def inplace_change(filename, old_string, new_string):
    f = open(filename, 'r')
    s = f.readlines()
    for i in range(len(s)):
        if s[i] == old_string + '\n':
            s[i] = new_string + '\n'
    f = open(filename, 'w')
    for i in range(len(s)):
        f.write(s[i])
    f.close()

def show_contacts(filename):
    file = open(filename, 'r')
    file_read = file.readlines()
    data_file = ['']
    for i in range(0, len(file_read), 2):
        data_file.append(file_read[i].strip('\n') + ' : ' + file_read[i + 1].strip('\n'))
    len_numbers = str(len(data_file) - 1)

    select_search = st.selectbox('CONTACTS' + ' | ' + len_numbers + ' |', data_file)
    file.close()
    return select_search

def show_data_button(filename):
    show_data = st.beta_expander('')
    file = open(filename, 'r')
    new = file.readlines()
    if not new:  # new == []
        show_data.info('-- 0 Contacts --')
    increment = 1
    for i in range(0, len(new), 2):
        organise = len(str(increment)) + 2
        show_data.text(str(increment) + '. Name : ' + new[i].strip('\n') + '\n' + ' ' * organise + 'Number : ' + new[
            i + 1].strip('\n'))
        increment += 1
    file.close()

def main():
    st.sidebar.header('| NAVIGATE 🔘 |')
    select = st.sidebar.selectbox('',
                                  (
                                  'Home 🏠', 'Add ♾', 'Delete Item 🗑️', 'Change Name 🔄', 'Change Number 🔢', 'About 📜'))

    if select == 'Home 🏠':
        show_contacts('C:/Users/ayaan/Phone_numbers.txt')
        show_data_button('C:/Users/ayaan/Phone_numbers.txt')

    elif select == 'Add ♾':
        show_contacts('C:/Users/ayaan/Phone_numbers.txt')
        update_file('C:/Users/ayaan/Phone_numbers.txt')

        show_data_button('C:/Users/ayaan/Phone_numbers.txt')

    elif select == 'Delete Item 🗑️':
        select_search = show_contacts('C:/Users/ayaan/Phone_numbers.txt')
        delete_item = ''
        for i in range(len(select_search)):
            if select_search[i] == ':':
                delete_item = select_search[0:i - 1]
                break
        file = open('C:/Users/ayaan/Phone_numbers.txt', 'r')
        check_read = file.read()
        delete_item_from_file(delete_item, 'C:/Users/ayaan/Phone_numbers.txt')

        show_data_button('C:/Users/ayaan/Phone_numbers.txt')

    elif select == 'Change Name 🔄':
        select_search = show_contacts('C:/Users/ayaan/Phone_numbers.txt')
        change_to = st.text_input("New Name :")
        change_button = st.button('Change', key=False)

        file = open('C:/Users/ayaan/Phone_numbers.txt', 'r')
        new1 = file.readlines()
        if change_button:
            if change_to == '' or select_search == '':
                st.info('-- Fields Empty --')
            elif change_to + '\n' in new1:
                st.info('--- Already Exists --- ')
            elif not (change_to[0].isalpha()):
                st.error('--- Atleast One Alphabet ---')
            else:
                st.success('Updated')
                select_search_name_split = select_search.split()
                changename_from = ''
                for i in range(1, len(select_search_name_split)):
                    if select_search_name_split[i] == ':':
                        select_search_name_split = select_search_name_split[0:i]
                        for i in range(len(select_search_name_split)):
                            changename_from += select_search_name_split[i] + ' '
                        break
                changename_from = changename_from[0:len(changename_from) - 1]
                inplace_change('C:/Users/ayaan/Phone_numbers.txt', changename_from, change_to)

        show_data_button('C:/Users/ayaan/Phone_numbers.txt')

    elif select == 'Change Number 🔢':
        select_search = show_contacts('C:/Users/ayaan/Phone_numbers.txt')
        change_to = st.text_input("New Number :")
        change_button = st.button('Change', key=False)

        file = open('C:/Users/ayaan/Phone_numbers.txt', 'r')
        new2 = file.readlines()
        if change_button:
            if change_to == '' or select_search == '':
                st.info('-- Fields Empty --')
            elif not (change_to.isdigit()):
                st.error('---Only digits allowed---')
            elif change_to + '\n' in new2:
                st.info('--- Already Exists --- ')
            else:
                st.success('Updated')
                select_search_number_split = select_search.split()
                changenumber_from = ''
                for i in range(1, len(select_search_number_split)):
                    if select_search_number_split[i] == ':':
                        select_search_number_split = select_search_number_split[i + 1]
                        for i in range(len(select_search_number_split)):
                            changenumber_from += select_search_number_split[i]
                        break
                changenumber_from = changenumber_from[0:len(changenumber_from)]
                inplace_change('C:/Users/ayaan/Phone_numbers.txt', changenumber_from, change_to)

        show_data_button('C:/Users/ayaan/Phone_numbers.txt')

    elif select == 'About 📜':
        about_info1 = '''<div
            style="background-image: linear-gradient(to left,black, grey);padding:3px;border-radius:9px">
            </div> '''

        st.markdown(about_info1, unsafe_allow_html=True)

        about_info2 = '''<div
            style="background-color:#36363d;padding:10px;border-radius:9px">
            <h2
            style="color:#1BA7B5;text-align:center;font-size:20px">DEVELOPER : AYAAN IZHAR
            </h2>
            </div> '''
        st.markdown(about_info2, unsafe_allow_html=True)

        about_info3 = '''<div
            style="background-image: linear-gradient(to right,black, grey);padding:3px;border-radius:9px">
            </div> '''
        st.markdown(about_info3, unsafe_allow_html=True)
        st.text('')

        st.header('[![GitHub](https://img.shields.io/badge/-Git_Hub-181717?style=flat&logo=github)](https://github.com/Ayaan-20)')

        button_more_info = st.button('More Info')
        if button_more_info:
            st.text('')
            st.text("")
            more_info = st.markdown("""
            <style>

            body{
              height: calc(100vh - 8em);
              padding: 4em;
              color: rgba(255,255,255,.75);
              font-family: 'Anonymous Pro', monospace;
              background-color: rgb(25,25,25);
            }
            .line-1{
                position: relative;
                top: 50%;
                width: 24em;
                margin: 0 auto;
                border-right: 2px solid rgba(255,255,255,.75);
                font-size: 120%;
                white-space: nowrap;
                overflow: hidden;
                transform: translateY(-50%);
            }

            /* Animation */
            .anim-typewriter{
              animation: typewriter 4s steps(44) 1s 1 normal both,
                         blinkTextCursor 500ms steps(44) infinite normal;
            }
            @keyframes typewriter{
              from{width: 0;}
              to{width: 27em;}
            }
            @keyframes blinkTextCursor{
              from{border-right-color: rgba(255,255,255,.75);}
              to{border-right-color: transparent;}
            }
            </style>
            <p class="line-1 anim-typewriter">Hi , I am a high-school python web/desktop app developer. </p>
            """, unsafe_allow_html=True)

main()
Button_Design = st.markdown("""
<style>
div.stButton> button:first-child{

    color:  #1BA7B5;
    background: linear-gradient(to left,  #36363D,  #36363D,grey) right;
    background-size: 500%;
    transition: 0.3s ;
    border-radius:10px;

}
div.stButton:hover> button:first-child  {
    background-position: left;
    border:10px;
    color: white
}
</style>""", unsafe_allow_html=True)

# ''' important -> Background-color-theme-secondary : #181717'''

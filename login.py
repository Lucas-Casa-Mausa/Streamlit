import streamlit as st
from streamlit import dialog

@st.dialog('Alert')
def validation_login(usr,passw):
    if usr == '' or passw == '':
        st.error('Please enter your username or password')
    else:
        st.success('Login Sucessful')

with st.form('Sign in'):
    st.title('Sign In')
    st.caption('Please enter your username and password')
    st.divider()

    username = st.text_input('Username')
    password = st.text_input('Password',type='password')

    st.divider()
    submit_btn = st.form_submit_button(label='Submit',icon=':material/mail:',use_container_width=True,type='primary')   
    google_btn = st.form_submit_button(label='Continue with Google',icon=':material/alternate_email:',use_container_width=True,type='secondary')

    col_left, col_right = st.columns([1, 1], gap='small')
    with col_left:
        remember_box = st.checkbox('Remember Me')

    with col_right:
        st.markdown("""
            <style>
                .custom-link:link, 
                .custom-link:visited, 
                .custom-link:active {
                    color: #f0f2f6; 
                    text-decoration: none;
                }
                .custom-link:hover {
                    color: #0300FF; 
                    text-decoration: underline;
                }
            </style>
            <p style="text-align:right; margin-top:8px;">
                <a href="#" class="custom-link">Forgot Password?</a>
            </p>
        """, unsafe_allow_html=True)



create_acc_btn = st.button(label='Create an account',use_container_width=True,type='secondary')   

sentiment_mapping = ['one','two','three','four','five']
st.caption("What's your experience with our form? ")
selected = st.feedback("stars")

code = '''def login(username, password):
    if username == "admin" and password == "1234":
        return "Access granted! 🟢"
    elif username == "" or password == "":
        return "Please fill in all fields! ⚠️"
    else:
        return "Access denied! 🚫"

# Give it a try...
username = input("Username: ")
password = input("Password: ")
print(login(username, password))'''

st.code(code,language='python')

if submit_btn :
    validation_login(username,password)
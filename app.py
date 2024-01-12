import streamlit as st

st.set_page_config(
    page_title="Catherine Chen - Lab 1",
    page_icon="🦋",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

st.markdown(
    """
# Hello👋 I'm Catherine (She/Her)
""")

col1, col2 = st.columns([0.4, 0.6])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 60%;
    }
    </style>

    <div class="profile-img">

    ![](https://framerusercontent.com/images/fJ3lA855CTiUPE0zVScw0fjU9Q.jpg?scale-down-to=1024)
    </div>
    """,
        unsafe_allow_html=True,
    )
    # st.image('https://framerusercontent.com/images/fJ3lA855CTiUPE0zVScw0fjU9Q.jpg?scale-down-to=1024', width=150)
with col2:
    st.markdown(
        """
    <style>
    .intro-text {
        padding-top: 30px;
    }
    </style>
    
    <div class="intro-text">
    I'm a UI/UX designer currently a graduate student pursuing a Master of Science in Technology Innovation at the University of Washington in Seattle. \n
    I have two years of experience designing web and mobile interfaces for B2C platforms. \n
    I completed a Bachelor in Arts (majored in Visual Arts) from the University of British Columbia and obtained an Associate certificate in Web Technology from BCIT School of Business and Media. With a solid fine art background and professionally trained in HTML and CSS coding, I am following my passion and diving into the field of product design. \n
    For my leisure time, you can also find me working as a commercial model @WILD MGMT in Vancouver, Canada.
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
# Education

- Master of Science (Technology Innovation) - University of Washington, Seattle, WA, USA
- Bachelor of Arts (Visual Arts) - University of British Columbia, Vancouver, BC, Canada
"""
)

st.markdown(
    """
# Work Experience

- UI/UX Designer (July, 2022 - August, 2023) - Giraffy Co. Ecommerce, Vancouver, Canada
- UI/UX Designer (August, 2021 - June, 2022) - Taoxue Life Technology, Vancouver, Canada
"""
)


st.markdown(
    """
# Hobbies & Interest
""")

col1, col2, col3 = st.columns(3)

# Card with image and text
with col1:
    st.markdown(
        """
    <style>
    .col-img img {            
        width: 100%;
        height: 150px;
    }
    </style>

    <div class="col-img">

    ![Hobbies](https://www.allrecipes.com/thmb/gSwtUoSNE0TfWQ7kbGNbOzNp6qs=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Why-Bake-at-350-Degrees-3x2-1-bd2294f1e91242968739da686dd2472f.png)
    </div>
    """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
    <style>
    .col-img img {            
        width: auto;        
        height: 150px;
    }
    </style>

    <div class="col-img">

    ![Hobbies](https://i.mscwlns.co/mosaic-wellness/image/upload/f_auto,w_1000,c_limit/v1648647977/BW%20BLOG/Untitled-design--41-.jpg)
    </div>
    """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
    <style>
    .col-img img {            
        width: 100%;
    }
    </style>

    <div class="col-img">

    ![Hobbies](https://images.squarespace-cdn.com/content/v1/54822a56e4b0b30bd821480c/1466806421172-H3JXTFR7QW6AH1I7LWR9/image-asset.jpeg)
    </div>
    """,
        unsafe_allow_html=True,
    )
st.markdown(
    """
# Highlighted Projects (Pocket Fridge)
"""
)

col1, col2 = st.columns([0.6, 0.4])
with col1:
    st.markdown(
        """
    <style>
    .profile-img img {
        width: 100%;
    }
    </style>

    <div class="profile-img">

    ![](https://framerusercontent.com/images/0qk9WgK0CHOzZYd3kwmxDib3Z8k.jpg?scale-down-to=4096)
    </div>
    """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
    <style>
    .intro-text {
        padding-top: 10px;
    }
    </style>
    
    <div class="intro-text">
    Pocket Fridge is an academic project aimed at resolving the social phenomenon of global food waste for individual households. The integration of the application and the smart refrigerator maximizes convenience for human beings.\n
    <a href="https://www.xuanchen.ca/pocket-fridge">View the Project</a> 
    </div>
    """,
        unsafe_allow_html=True,
    )

import streamlit as st
from PIL import Image
from sidebar import add_sidebar_message

# Set page configuration (title, icon, layout, sidebar state)
st.set_page_config(
    page_title="Mallikarjun - Data Scientist",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add the sidebar footer
add_sidebar_message()

# Main content
with st.container():
    st.title("Hey there! 👋  I'm a Data Spider 🕷️")  # Title
    st.markdown("")
    # Create two columns with a minimal gap
    col1, col2 = st.columns((1, 1.5), gap="small")
    
    with col1:
        # Display profile image
        st.markdown('<div class="profile-img">', unsafe_allow_html=True)
        st.image('./assets/img/profile-pic.png', use_column_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # Personal introduction
        st.markdown("""
            **I'm Mallikarjun Aitha**, your go-to Data Spider, here to spin raw data into actionable insights with a dash of data-driven magic! Armed with a Master’s in Data Science from the University of New Haven and hands-on experience in Machine Learning (ML), Spatial Data Science, and Advanced Analytics, I specialize in turning complex data problems into clear, impactful solutions. Currently, I work as a GIS Analyst at the University of New Haven, analyzing New Haven Police Department Crime data
            """)
        
        # Career background and expertise
        st.markdown("""
            My journey spans working as an Associate Analyst at American Express and Data Analyst at Downtown Evening Soup Kitchen, where I utilized analytics to refine strategies, enhance offerings, and create data-driven solutions. 
            Whether it’s developing machine learning models, exploring spatial data with GIS, or automating workflows, 
            I thrive on solving complex challenges and delivering actionable intelligence.
            """)

        # Personal interests
        st.markdown("""
            But beyond the world of data, I’m a curious explorer with a love for traveling, cricket, and photography. 
            I believe that the best insights come from a mix of technical expertise, creativity, and storytelling—transforming 
            data into experiences that truly matter.
            """)

        # Closing statement
        st.markdown("""
            _In the world of data, with great algorithms comes great responsibility — but don’t worry, I’ve got your back! 🕷️✨_
            """)

        # Resume download button
        with open("assets/Mallikarjun_Aitha_Resume.pdf", "rb") as file:
            st.download_button(
                label="Download my resume",
                data=file,
                file_name="Mallikarjun_Aitha_Resume.pdf",
                mime="application/pdf"
            )
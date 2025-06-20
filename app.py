import streamlit as st
import base64
from pathlib import Path

# Set page config
st.set_page_config(
    page_title="Zubair Abdullah - AI & Python Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# Custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("assets/css/style.css")


# Helper function for images
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded


def img_to_html(img_path, width=None, height=None):
    img_format = img_path.split('.')[-1].lower()
    if img_format == 'svg':
        with open(img_path, "r") as f:
            svg = f.read()
        if width:
            svg = svg.replace('<svg', f'<svg width="{width}"')
        if height:
            svg = svg.replace('<svg', f'<svg height="{height}"')
        return svg
    else:
        img_html = f"<img src='data:image/{img_format};base64,{img_to_bytes(img_path)}'"
        if width:
            img_html += f" width='{width}'"
        if height:
            img_html += f" height='{height}'"
        img_html += "/>"
        return img_html


# Navigation
def navigation():
    st.markdown("""
    <nav class="mk-header">
        <div class="mk-header-container">
            <div>
                <div class="mk-logo-bg">
                    <img src="data:image/png;base64,{}" alt="logo" class="mk-logo"/>
                </div>
            </div>
            <div class="d-flex">
                <div>
                    <button class="mk-button-md mx-3 mx-lg-5">Curriculum Vitae | CV</button>
                </div>
            </div>
        </div>
    </nav>
    """.format(img_to_bytes("assets/images/profile.jpeg")), unsafe_allow_html=True)


# Home Section
def home_section():
    st.markdown("""
    <div id="home" class="view-element">
        <div class="mk-outer">
            <div class="container">
                <div class="mk-outer-container d-flex justify-content-between align-items-center">
                    <div class="mk-outer-text">
                        <div class="mk-outer-heading">G'day, I'm</div>
                        <div class="mk-outer-heading">Zubair Abdullah,</div>
                        <div class="mk-outer-heading2">AI Enthusiast & Python Developer</div>
                        <div class="mk-outer-description">
                            I'm a passionate AI developer specializing in conversational chatbots and Python solutions. 
                            With expertise in local LLMs, Gemini, and Ollama, I build intelligent systems that enhance 
                            user engagement and service efficiency. My work combines AI, machine learning, and full-stack 
                            development to create impactful solutions.
                        </div>
                        <div class="mk-outer-contact">
                            <button class="mk-button">Contact me!</button>
                        </div>
                    </div>
                    <div class="mk-outer-gooery">
                        <div class="mk-gooery">
                            <svg style="position:absolute;width:0;height:0">
                                <filter id="goo">
                                    <feGaussianBlur in="SourceGraphic" result="blur" stdDeviation="30"></feGaussianBlur>
                                    <feColorMatrix in="blur" values="1 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 30 -7"></feColorMatrix>
                                </filter>
                            </svg>
                            <div class="hooks-main">
                                <div class="hooks-filter">
                                    <div class="b1" style="transform:translate3d(0px,0px,0) translate3d(-50%,-50%,0)"></div>
                                    <div class="b2" style="transform:translate3d(0px,0px,0) translate3d(-50%,-50%,0)"></div>
                                    <div class="b3" style="transform:translate3d(0px,0px,0) translate3d(-50%,-50%,0)"></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# About Section
def about_section():
    st.markdown("""
    <div id="my-self" class="view-element">
        <div class="mk-myself">
            <div class="container">
                <div class="mk-myself-container">
                    <div class="mk-views-title-container">
                        <div class="mk-views-title-text">My Portfolio</div>
                        <div class="mk-views-title-line-container">
                            <div class="mk-views-title-line"></div>
                        </div>
                    </div>
                    <div class="row justify-content-center">
                        <div class="col-12 col-md-8">
                            <div class="">
                                <div class="mk-myself-paragraph">
                                    Hello, I'm Zubair Abdullah, an AI enthusiast and full-stack Python developer based in Pakistan.
                                </div>
                                <div class="mk-myself-paragraph">
                                    Driven by a strong passion for customer support technologies, I specialize in building intelligent, 
                                    conversational chatbots that enhance user engagement and service efficiency.
                                </div>
                                <div class="mk-myself-paragraph">
                                    I've successfully developed AI-powered support bots using local Large Language Models (LLMs), 
                                    Gemini, and Ollama, integrating them with Python, Anaconda, HTML, and CSS — all within the 
                                    PyCharm development environment.
                                </div>
                                <div class="mk-myself-paragraph">
                                    With over 5 years of hands-on experience in WordPress development, I've built dynamic and 
                                    responsive websites locally using Apache and MySQL.
                                </div>
                                <div class="mk-myself-paragraph">
                                    Alongside web development, I've been a passionate graphic designer since 2018 — crafting logos, 
                                    templates, and visual assets using Canva and Adobe Illustrator.
                                </div>
                                <div class="mk-myself-list-parent row">
                                    <div class="col">
                                        <div class="mk-myself-skill">Python</div>
                                        <div class="mk-myself-skill">AI/ML/NLP</div>
                                        <div class="mk-myself-skill">Local LLMs</div>
                                        <div class="mk-myself-skill">Ollama</div>
                                        <div class="mk-myself-skill">Gemini</div>
                                    </div>
                                    <div class="col">
                                        <div class="mk-myself-skill">WordPress</div>
                                        <div class="mk-myself-skill">Graphic Design</div>
                                        <div class="mk-myself-skill">Canva</div>
                                        <div class="mk-myself-skill">Adobe Illustrator</div>
                                        <div class="mk-myself-skill">Streamlit</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div class="col-12 col-md-4 mt-5 mt-md-0">
                            <div class="mk-myself-profile-wrapper d-flex justify-content-center">
                                <div class="mk-hover-image mk-myself-profile-parent">
                                    <div class="mk-hover-image-border undefined"></div>
                                    <div class="mk-hover-image-filter undefined"></div>
                                    <img alt="profile" class="mk-hover-profile mk-myself-profile" src="data:image/jpeg;base64,{}"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """.format(img_to_bytes("assets/images/profile.jpeg")), unsafe_allow_html=True)


# Experience Section
def experience_section():
    st.markdown("""
    <div id="experience" class="view-element">
        <div class="mk-works">
            <div class="container h100per-min100vh d-flex justify-content-center">
                <div class="mk-works-container">
                    <div class="mk-views-title-container">
                        <div class="mk-views-title-text">My Work Experiences</div>
                        <div class="mk-views-title-line-container">
                            <div class="mk-views-title-line"></div>
                        </div>
                    </div>
                    <div>
                        <div class="mk-works-tab">
                            <div class="mk-works-left-border">
                                <div style="transform:translateY(0px)" class="mk-works-left-border-selection"></div>
                            </div>
                            <div class="mk-works-tab-left">
                                <div><div class="mk-works-tab-left-button mk-works-tab-left-button-selected">Freelance Projects</div></div>
                                <div><div class="mk-works-tab-left-button">Upwork & Fiverr</div></div>
                                <div><div class="mk-works-tab-left-button">Personal Projects</div></div>
                            </div>
                            <div class="mk-works-tab-right">
                                <div class="mk-works-tab-right-title">AI Developer & Python Programmer</div>
                                <div class="mk-works-tab-right-duration">Remote | 2018 - Present</div>
                                <div class="mk-works-tab-right-list">
                                    <div class="mk-works-tab-right-list-item">
                                        As a freelance developer, I've specialized in creating AI-powered solutions including chatbots, 
                                        predictive models, and automation tools. My projects leverage Python, local LLMs, and various 
                                        machine learning techniques to solve real-world problems.
                                    </div>
                                    <div class="mk-works-tab-right-list-item">
                                        I've also built numerous WordPress websites with custom functionality and provided graphic design 
                                        services including logo creation, branding, and marketing materials.
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Projects Section
def projects_section():
    st.markdown("""
    <div id="my-work" class="view-element">
        <div class="mk-projects">
            <div class="container">
                <div class="mk-projects-container">
                    <div class="mk-views-title-container">
                        <div class="mk-views-title-text">Projects I've Built</div>
                        <div class="mk-views-title-line-container">
                            <div class="mk-views-title-line"></div>
                        </div>
                    </div>
                    <div class="row justify-content-center">
                        <!-- Project 1 -->
                        <div class="mk-projects-single">
                            <div class="row">
                                <div class="col-6 d-none d-lg-block">
                                    <div class="mk-window-screen mk-projects-image-container mk-projects-image-container-right">
                                        <div><div class="mk-hover-image"><div class="mk-hover-image-filter"></div>
                                        <img alt="LegalEase Bot" class="mk-hover-profile mk-image" src="data:image/png;base64,{}"/></div></div>
                                    </div>
                                </div>
                                <div class="col-12 col-lg-6 d-flex align-items-center order-first">
                                    <div class="mk-projects-text-side mk-projects-text-side-right">
                                        <div class="mk-projects-text-featured">Featured Project</div>
                                        <div class="mk-projects-text-title">LegalEase Judiciary Bot</div>
                                        <div class="mk-projects-text-description text-left">
                                            A local LLM-powered chatbot trained on Pakistani law (CrPC, PPC) for legal guidance with context awareness. 
                                            This AI assistant provides accurate legal information while maintaining conversation history for better user experience.
                                        </div>
                                        <div class="mk-projects-text-tecs">Python | Ollama | PyCharm | Local LLM</div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- Project 2 -->
                        <div class="mk-projects-single">
                            <div class="row">
                                <div class="col-6 d-none d-lg-block">
                                    <div class="mk-window-screen mk-projects-image-container mk-projects-image-container-left">
                                        <div><div class="mk-hover-image"><div class="mk-hover-image-filter"></div>
                                        <img alt="Aviator Bot" class="mk-hover-profile mk-image" src="data:image/png;base64,{}"/></div></div>
                                    </div>
                                </div>
                                <div class="col-12 col-lg-6 d-flex align-items-center">
                                    <div class="mk-projects-text-side mk-projects-text-side-left">
                                        <div class="mk-projects-text-featured">Featured Project</div>
                                        <div class="mk-projects-text-title">Aviator Prediction Bot</div>
                                        <div class="mk-projects-text-description text-left">
                                            AI bot to predict Aviator game crash points using real-time DB + CSV-based ML logic and UI in Streamlit. 
                                            The system analyzes patterns and provides predictions with a user-friendly interface.
                                        </div>
                                        <div class="mk-projects-text-tecs">Python | Pandas | Streamlit | MySQL</div>
                                        <div class="mk-projects-text-link"><a href="#" target="_blank">Try the Live Bot 🚀</a></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- Project 3 -->
                        <div class="mk-projects-single">
                            <div class="row">
                                <div class="col-6 d-none d-lg-block">
                                    <div class="mk-window-screen mk-projects-image-container mk-projects-image-container-right">
                                        <div><div class="mk-hover-image"><div class="mk-hover-image-filter"></div>
                                        <img alt="Geo Guide" class="mk-hover-profile mk-image" src="data:image/png;base64,{}"/></div></div>
                                    </div>
                                </div>
                                <div class="col-12 col-lg-6 d-flex align-items-center order-first">
                                    <div class="mk-projects-text-side mk-projects-text-side-right">
                                        <div class="mk-projects-text-featured">Featured Project</div>
                                        <div class="mk-projects-text-title">Geo Guide Website</div>
                                        <div class="mk-projects-text-description text-left">
                                            Tourist-friendly website designed in Google Sites for travel guidance and destination insights. 
                                            The platform provides comprehensive information about various locations with intuitive navigation.
                                        </div>
                                        <div class="mk-projects-text-tecs">Google Sites | Web Design</div>
                                        <div class="mk-projects-text-link"><a href="#" target="_blank">Visit Site 🌐</a></div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!-- Project 4 -->
                        <div class="mk-projects-single">
                            <div class="row">
                                <div class="col-6 d-none d-lg-block">
                                    <div class="mk-window-screen mk-projects-image-container mk-projects-image-container-left">
                                        <div><div class="mk-hover-image"><div class="mk-hover-image-filter"></div>
                                        <img alt="LIFT MVP" class="mk-hover-profile mk-image" src="data:image/png;base64,{}"/></div></div>
                                    </div>
                                </div>
                                <div class="col-12 col-lg-6 d-flex align-items-center">
                                    <div class="mk-projects-text-side mk-projects-text-side-left">
                                        <div class="mk-projects-text-featured">Featured Project</div>
                                        <div class="mk-projects-text-title">LIFT MVP — Skill Uplift Platform</div>
                                        <div class="mk-projects-text-description text-left">
                                            A humanitarian web-based platform connecting underprivileged users to job opportunities, NGOs, skill courses, and donations — accessible even via SMS and WhatsApp. 
                                            Built with Flask, SQLite, Tailwind, and integrated with AI-based job-user matching and Stripe donations. Targeted at poor communities with low internet access.
                                        </div>
                                        <div class="mk-projects-text-tecs">Python | Flask | SQLite | Tailwind CSS | AI Matching | Stripe</div>
                                        <div class="mk-projects-text-link"><a href="https://github.com/zubairabdullah98/lift" target="_blank">View on GitHub 🔗</a></div>
                                    </div>
                                </div>
                            </div>
                        </div>                        
                    </div>
                </div>
            </div>
        </div>
    </div>
    """.format(
        img_to_bytes("assets/images/projects/bot.png"),
        img_to_bytes("assets/images/projects/aviator.png"),
        img_to_bytes("assets/images/projects/title.png"),
        img_to_bytes("assets/images/projects/lift.png")
    ), unsafe_allow_html=True)


# Reviews Section
def reviews_section():
    st.markdown("""
    <div id="reviews" class="view-element">
        <div class="mk-reviews">
            <div class="container">
                <div class="mk-reviews-container">
                    <div class="mk-views-title-container">
                        <div class="mk-views-title-text">Client Reviews</div>
                        <div class="mk-views-title-line-container">
                            <div class="mk-views-title-line"></div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="mk-reviews-list">
                <div style="width:fit-content;align-self:self-end">
                    <div class="mk-review-item-info mk-reviwe-color-theme1-invert">Upwork Client</div>
                    <div class="mk-review-item mk-reviwe-color-theme1">"Zubair built a fully functional chatbot with smart memory in record time."</div>
                </div>
                <div style="width:fit-content;align-self:self-start">
                    <div class="mk-review-item-info mk-reviwe-color-theme2-invert">Gerald via Fiverr</div>
                    <div class="mk-review-item mk-reviwe-color-theme2">"I loved the responsiveness and professionalism!"</div>
                </div>
                <div style="width:fit-content;align-self:self-end">
                    <div class="mk-review-item-info mk-reviwe-color-theme1-invert">Upwork Client</div>
                    <div class="mk-review-item mk-reviwe-color-theme1">"The AI solution exceeded our expectations and was delivered ahead of schedule."</div>
                </div>
                <div style="width:fit-content;align-self:self-start">
                    <div class="mk-review-item-info mk-reviwe-color-theme2-invert">Sarah via Fiverr</div>
                    <div class="mk-review-item mk-reviwe-color-theme2">"Excellent communication and technical skills. Will definitely work with again."</div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


# Certifications Section
def certifications_section():
    st.markdown("""
    <div id="certifications" class="view-element">
        <div class="mk-certifications">
            <div class="container p-3">
                <div class="mk-certifications-top-background"></div>
                <div class="mk-certifications-container">
                    <div class="mk-views-title-container">
                        <div class="mk-views-title-text">Licenses & Certifications</div>
                        <div class="mk-views-title-line-container">
                            <div class="mk-views-title-line"></div>
                        </div>
                    </div>
                    <div class="mk-certifications-grid">
                        <!-- Certification 1 -->
                        <div class="mk-certifications-item">
                            <div class="mk-item-body">
                                <div class="mk-item-head">
                                    <div style="background-image:url(data:image/png;base64,{})" class="mk-item-logo"></div>
                                    <div class="mk-item-share">
                                        <a href="assets/images/Certifications/certificate/50th Canva Certificate.gif" target="_blank">
                                            <svg width="22" height="22" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title>External Link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                                        </a>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <div class="mk-item-title">50th Canva Certificate</div>
                                    <div class="mk-item-platform">Canva</div>
                                </div>
                                <div class="mk-item-date">Issued 2023 · No Expiration Date</div>
                            </div>
                        </div>
                        <!-- Certification 2 -->
                        <div class="mk-certifications-item">
                            <div class="mk-item-body">
                                <div class="mk-item-head">
                                    <div style="background-image:url(data:image/png;base64,{})" class="mk-item-logo"></div>
                                    <div class="mk-item-share">
                                        <a href="assets/images/Certifications/certificate/Data Science-simplilearn.pdf" target="_blank">
                                            <svg width="22" height="22" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title>External Link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                                        </a>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <div class="mk-item-title">Data Science</div>
                                    <div class="mk-item-platform">Simplilearn</div>
                                </div>
                                <div class="mk-item-date">Issued 2023 · No Expiration Date</div>
                            </div>
                        </div>
                        <!-- Certification 3 -->
                        <div class="mk-certifications-item">
                            <div class="mk-item-body">
                                <div class="mk-item-head">
                                    <div style="background-image:url(data:image/png;base64,{})" class="mk-item-logo"></div>
                                    <div class="mk-item-share">
                                        <a href="assets/images/Certifications/certificate/Generative AI for Everyone-simplilearn.pdf" target="_blank">
                                            <svg width="22" height="22" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title>External Link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                                        </a>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <div class="mk-item-title">Generative AI for Everyone</div>
                                    <div class="mk-item-platform">Simplilearn</div>
                                </div>
                                <div class="mk-item-date">Issued 2024 · No Expiration Date</div>
                            </div>
                        </div>
                        <!-- Certification 4 -->
                        <div class="mk-certifications-item">
                            <div class="mk-item-body">
                                <div class="mk-item-head">
                                    <div style="background-image:url(data:image/png;base64,{})" class="mk-item-logo"></div>
                                    <div class="mk-item-share">
                                        <a href="assets/images/Certifications/certificate/ML with python-simplilearn.pdf" target="_blank">
                                            <svg width="22" height="22" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title>External Link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                                        </a>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <div class="mk-item-title">Machine Learning with Python</div>
                                    <div class="mk-item-platform">Simplilearn</div>
                                </div>
                                <div class="mk-item-date">Issued 2023 · No Expiration Date</div>
                            </div>
                        </div>
                        <!-- Certification 5 -->
                        <div class="mk-certifications-item">
                            <div class="mk-item-body">
                                <div class="mk-item-head">
                                    <div style="background-image:url(data:image/png;base64,{})" class="mk-item-logo"></div>
                                    <div class="mk-item-share">
                                        <a href="assets/images/Certifications/certificate/NLP-simplilearn.pdf" target="_blank">
                                            <svg width="22" height="22" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title>External Link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                                        </a>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <div class="mk-item-title">Natural Language Processing</div>
                                    <div class="mk-item-platform">Simplilearn</div>
                                </div>
                                <div class="mk-item-date">Issued 2023 · No Expiration Date</div>
                            </div>
                        </div>
                        <!-- Certification 6 -->
                        <div class="mk-certifications-item">
                            <div class="mk-item-body">
                                <div class="mk-item-head">
                                    <div style="background-image:url(data:image/png;base64,{})" class="mk-item-logo"></div>
                                    <div class="mk-item-share">
                                        <a href="assets/images/Certifications/certificate/Scientific Computing with Python-freecodecamp.pdf" target="_blank">
                                            <svg width="22" height="22" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-external-link"><title>External Link</title><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
                                        </a>
                                    </div>
                                </div>
                                <div class="flex-1">
                                    <div class="mk-item-title">Scientific Computing with Python</div>
                                    <div class="mk-item-platform">freeCodeCamp</div>
                                </div>
                                <div class="mk-item-date">Issued 2023 · No Expiration Date</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """.format(
        img_to_bytes("assets/images/Certifications/canva.png"),
        img_to_bytes("assets/images/Certifications/simplilearn.png"),
        img_to_bytes("assets/images/Certifications/simplilearn.png"),
        img_to_bytes("assets/images/Certifications/simplilearn.png"),
        img_to_bytes("assets/images/Certifications/simplilearn.png"),
        img_to_bytes("assets/images/Certifications/freecodecamp.png")
    ), unsafe_allow_html=True)

# Contact Section
def contact_section():
    st.markdown("""
    <div id="contact" class="view-element">
        <div class="mk-contact">
            <div class="mk-contact-zebra-img" style="background-image:url(data:image/svg+xml;base64,{})"></div>
            <div class="mk-contact-box">
                <div class="container flex-center flex-column">
                    <div class="mk-contact-box-width">
                        <div class="mk-contact-label">Get in touch</div>
                        <div class="mk-contact-title">Let's Work Together</div>
                        <div class="mk-contact-text">
                            If you have a project or idea in mind, feel free to reach out. I'm always open to new collaborations 
                            and ambitious work! Whether you need an AI solution, web development, or design work, I'd love to hear about it.
                        </div>
                        <div class="mk-contact-button">
                            <button class="mk-button">Say Hello</button>
                        </div>
                        <div class="mk-contact-git-section"></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """.format(img_to_bytes("assets/arrow-sample.svg")), unsafe_allow_html=True)


# Side Elements
def side_elements():
    st.markdown("""
    <div class="mk-side-elements">
        <div class="mk-side-elements-container mk-side-elements-left">
            <div class="mk-side-elements-item">
                <a href="https://github.com/zubairabdullah98" target="_blank">
                    <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-github"><title>GitHub</title><path d="M9 19c-5 1.5-5-2.5-7-3m14 6v-3.87a3.37 3.37 0 0 0-.94-2.61c3.14-.35 6.44-1.54 6.44-7A5.44 5.44 0 0 0 20 4.77 5.07 5.07 0 0 0 19.91 1S18.73.65 16 2.48a13.38 13.38 0 0 0-7 0C6.27.65 5.09 1 5.09 1A5.07 5.07 0 0 0 5 4.77a5.44 5.44 0 0 0-1.5 3.78c0 5.42 3.3 6.61 6.44 7A3.37 3.37 0 0 0 9 18.13V22"></path></svg>
                </a>
            </div>
            <div class="mk-side-elements-item">
                <a href="https://www.linkedin.com/in/abdullah-zubair-b4027b27b/" target="_blank">
                    <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-linkedin"><title>LinkedIn</title><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"></path><rect x="2" y="9" width="4" height="12"></rect><circle cx="4" cy="4" r="2"></circle></svg>
                </a>
            </div>
            <div class="mk-side-elements-item">
                <a href="https://www.fiverr.com/s/ljEK3we" target="_blank">
                    <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-fiverr"><title>Fiverr</title><path d="M19 6.873a2 2 0 0 1 1 1.747v6.536a2 2 0 0 1-1.029 1.748l-6 3.833a2 2 0 0 1-1.942 0l-6-3.833A2 2 0 0 1 4 15.156V8.62a2 2 0 0 1 1.029-1.748l6-3.572a2.056 2.056 0 0 1 2 0l6 3.573z"></path><path d="M10.5 8.5L12 10l1.5-1.5"></path><path d="M12 10v4.5"></path><path d="M12 10l-1.5 1.5"></path></svg>
                </a>
            </div>
            <div class="mk-side-elements-item">
                <a href="https://www.instagram.com/bullehshah_/" target="_blank">
                    <svg width="20" height="20" xmlns="http://www.w3.org/2000/svg" role="img" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="feather feather-instagram"><title>Instagram</title><rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line></svg>
                </a>
            </div>
            <div class="mk-side-elements-line"></div>
        </div>
        <div class="mk-side-elements-container mk-side-elements-right">
            <div class="mk-side-elements-item">
                <a href="mailto:zubairabdullah5665@gmail.com">
                    <div class="mk-side-elements-text">zubairabdullah5665@gmail.com</div>
                </a>
            </div>
            <div class="mk-side-elements-line"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Main App
def main():
    navigation()
    home_section()
    about_section()
    experience_section()
    projects_section()
    reviews_section()
    certifications_section()
    contact_section()
    side_elements()


if __name__ == "__main__":
    main()

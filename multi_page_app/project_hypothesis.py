import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.success(
        f"* We suspect mildew infected cherry leaves have unclear marks/signs, "
        f"the mildew is light roughly-circular, powdery looking patches on young, susceptible leaves. \n\n"
        f"* An Image Montage, shows that typically mildew infected leaves has white marks across. "
        f"Average Image, Variability Image and Difference between Averages studies didn't reveal "
        f"any clear pattern to differentiate one to another."

    )
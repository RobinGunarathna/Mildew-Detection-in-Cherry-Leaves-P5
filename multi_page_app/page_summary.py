import streamlit as st
import matplotlib.pyplot as plt


def page_summary_body():

    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n"
        f"* Powdery mildew of sweet and sour cherry is caused by Podosphaera clandestina, "
        f"an obligate biotrophic fungus.\n"
        f"* Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, "
        f" rendering them unmarketable due to the covering of white fungal growth on the cherry surface.\n"
        f"* According to [WSU](http://treefruit.wsu.edu/crop-protection/disease-management/cherry-powdery-mildew/), "
        f" Season long disease control of both leaves and fruit is critical "
        f"to minimize overall disease pressure in the orchard"
        f"and consequently to protect developing fruit from accumulating spores on their surfaces.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset contains 2104 healthy cherry leaf images "
        f"and 2104 powdery mildew infected cherry leaf images.")

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/RobinGunarathna/Mildew-Detection-in-Cherry-Leaves-P5/blob/main/README.md).")
    

    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in conducting a study to visually differentiate "
        f"a cherry leaf that is healthy from one that contains powdery mildew.\n"
        f"* 2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew. "
        )
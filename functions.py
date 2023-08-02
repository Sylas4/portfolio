import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
import pandas as pd
import streamlit as st
from PIL import Image
import sys

class layout():
    #####################
    # Custom function for printing text
    def head(a, b):
        col1, col2 = st.columns([3,1])
        with col1:
            st.markdown(a)
        with col2:
            st.image(Image.open(b))

    def txt(a, b):
        col1, col2 = st.columns([4,1])
        with col1:
            st.markdown(a, unsafe_allow_html=True)
        with col2:
            st.markdown(b, unsafe_allow_html=True)

    def txt2(a, b, c):
        col1, col2, col3 = st.columns([1,5,6])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)
        with col3:
            st.markdown(c)

    def txt3(a, b):
        col1, col2 = st.columns([1,2])
        with col1:
            st.markdown(a)
        with col2:
            st.markdown(b)

class dashboard():
    
    @st.cache_data
    def demo_df():
        return pd.read_csv("https://plotly.github.io/datasets/country_indicators.csv")

    @st.cache_data
    def merged_df():
        return pd.read_csv("data/demo_merged.csv")
    
    def get_img(path = "idup.jpeg"):
        return Image.open(f'./img/{path}')


class gaussienne():

    def plot_bilateral(aire,scale):
        fig, ax = plt.subplots(figsize=(9,6))
        
        # On définit les x_all et y2 pour tracer un courbe de gauss
        x_all = np.arange(-50, 50, 0.001)
        y = norm.pdf(x_all,0,scale)

        # On calcul le Zscore pour la probabilité voulu en bilatéral
        z = norm.ppf(0.5 + (aire/2),0,scale)

        # On définit les x et y qui délimiteront notre aire sous la courbe grace à -z et z car bilatéral
        x = np.arange(-z, z, 0.001)
        y2 = norm.pdf(x,0,scale)

        # On trace la courbe
        ax.plot(x_all,y)

        # On limite nos abscisse entre -4 et 4
        ax.set_xlim([-3.8*scale, 3.8*scale])

        # On remplit l'aire sous notre courbe en fonction de x et y
        ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
        filled_poly = ax.fill_between(x_all, y, 0, alpha=0.2, color="#ffcc00")
        
        # On écrit le pourcentage d'aire remplit sous la courbe
        (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        
        # On affiche les coordonnées de -z et z
        plt.xlabel('Z') 
        plt.ylabel('Frequency') 
        plt.xticks([-z,z])
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
        # plt.show()
        
        return fig

    def plot_unilateral(aire, scale):
        fig, ax = plt.subplots(figsize=(9,6))
        # On définit les x_all et y2 pour tracer un courbe de gauss
        x_all = np.arange(-50, 50, 0.001)
        y = norm.pdf(x_all,0,scale)
        # On calcul le Zscore pour la probabilité voulu en unilatéral
        z = norm.ppf(aire, 0, scale)
        
        # On définit les x et y qui délimiteront notre aire sous la courbe grace à z car unilatéral
        x = np.arange(-10, z, 0.001)
        y2 = norm.pdf(x,0,scale)

        # On trace la courbe
        ax.plot(x_all,y)

        # On limite nos abscisse entre -4 et 4
        ax.set_xlim([-3.8*scale,4*scale])

        # On remplit l'air sous notre courbe en fonction de x et y
        ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
        filled_poly = ax.fill_between(x_all,y, alpha=0.3, color='#ffcc00')

        # On écrit la pourcentage d'aire remplit sous la courbe
        (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        
        # On affiche les coordonnées de z
        plt.xlabel('Z') 
        plt.ylabel('Frequency') 
        plt.xticks([z])
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
        # plt.show()
        return fig 

    def plot_unilateral_z(z, scale):
        
        fig, ax = plt.subplots(figsize=(9,6))

        # On définit les x_all et y2 pour tracer un courbe de gauss grâce à la fonction pdf (probability density fonction)
        x = np.arange(-10, 10, 0.001)
        y = norm.pdf(x, 0, scale)

        # On définit les x et y qui délimiteront notre aire sous la courbe grace à z et à la fonction pdf
        # On part toujours de -1O mais on s'arrête à Z
        x_fill = np.arange(-10, z, 0.001)
        # On définit y grâce à la fonction pdf
        y_fill = norm.pdf(x_fill,0, scale)

        ax.plot(x, y)
        # On limite nos abscisse entre -4 et 4
        ax.set_xlim([-3.8*scale,3.8*scale])

        # On calcul la probabilité qui correspond à notre Zscore
        aire = norm.cdf(z,0,scale)

        # On remplit l'aire complète sous notre courbe
        ax.fill_between(x, y, alpha=0.3, color='#ffcc00')
        # Puis seulement l'aire qui nous intéresse, en plus foncé
        ax.fill_between(x_fill, y_fill, alpha=0.7, color='#ffcc00')

        # On écrit le pourcentage d'aire remplit sous la courbe
        ax.text(0, .2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')

        plt.xlabel('Z') 
        plt.ylabel('Frequency') 
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])

        return fig

    def plot_bilateral_z(z,scale):
        fig, ax = plt.subplots(figsize=(9,6))
        
        # On définit les x_all et y2 pour tracer un courbe de gauss
        x_all = np.arange(-10, 10, 0.001)
        y2 = norm.pdf(x_all,0,scale)
        
        # On définit les x et y qui délimiteront notre aire sous la courbe grace à z et -z car bilatéral
        x = np.arange(-z, z, 0.001)
        y = norm.pdf(x,0,scale)
        ax.plot(x_all,y2)
        
        # On limite nos abscisse entre -4 et 4
        ax.set_xlim([-3.8*scale,3.8*scale])
        
        # On calcul la probabilité qui correspond à notre Zscore (ne pas oublier on est en bilatéral)
        aire = (norm.cdf(z,0,scale)-0.5)*2
        
        # On remplit l'air sous notre courbe en fonction de x et y
        ax.fill_between(x,y, alpha=0.7, color='#ffcc00', label=aire)
        
        # On écrit la pourcentage d'aire remplit sous la courbe
        filled_poly = ax.fill_between(x_all,y2,0, alpha=0.3, color='#ffcc00')
        (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
        ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        
        plt.xlabel('Z') 
        plt.ylabel('Frequency') 
        plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
        # plt.show()
        return fig

# class tast():

#     def find_z(aire, scale, unilateral=True):
#         if unilateral:
#             return norm.ppf(aire,0,scale)
#         else:
#             # On calcul le Zscore pour la probabilité voulu en bilatéral
#             return norm.ppf(0.5 + (aire/2),0,scale)
    
#     def find_aire(z, scale, unilateral=True):
#         if unilateral:
#             return norm.cdf(z,0,scale)
#         else:
#             # On calcul la probabilité qui correspond à notre Zscore (ne pas oublier on est en bilatéral)
#             return (norm.cdf(z,0,scale)-0.5)*2

#     def plot_it(aire,scale, mode):
#         fig, ax = plt.subplots(figsize=(9,6))
        
#         # On définit les x_all et y2 pour tracer un courbe de gauss
#         x_all = np.arange(-50, 50, 0.001)
#         y = norm.pdf(x_all,0,scale)

#         # On trace la courbe
#         ax.plot(x_all,y)

#         # On limite nos abscisse entre -4 et 4
#         ax.set_xlim([-3.8*scale, 3.8*scale])

#         # On affiche les coordonnées de -z et z
#         plt.xlabel('Z') 
#         plt.ylabel('Frequency')

#         plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
#         # plt.show()

#         if mode=="zb":
#             z = find_z(aire, scale, unilateral=False):
#             x = np.arange(-z, z, 0.001)
#             y2 = norm.pdf(x,0,scale)
#             # On remplit l'aire sous notre courbe en fonction de x et y
#             fill = ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
#             filled_poly = ax.fill_between(x_all, y, 0, alpha=0.2, color="#ffcc00")
#             plt.xticks([-z,z])
            
        
#         return fig



#         # On calcul le Zscore pour la probabilité voulu en bilatéral
#         z = norm.ppf(0.5 + (aire/2),0,scale)

#         # On définit les x et y qui délimiteront notre aire sous la courbe grace à -z et z car bilatéral
#         x = np.arange(-z, z, 0.001)
#         y2 = norm.pdf(x,0,scale)

        

#         # On remplit l'aire sous notre courbe en fonction de x et y
#         fill = ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
#         filled_poly = ax.fill_between(x_all, y, 0, alpha=0.2, color="#ffcc00")
        
#         # On écrit le pourcentage d'aire remplit sous la courbe
#         (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
#         ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        


#     def plot_unilateral(aire,scale):
#         fig, ax = plt.subplots(figsize=(9,6))
#         # On définit les x_all et y2 pour tracer un courbe de gauss
#         x_all = np.arange(-50, 50, 0.001)
#         y = norm.pdf(x_all,0,scale)
#         # On calcul le Zscore pour la probabilité voulu en unilatéral
#         z = norm.ppf(aire, 0, scale)
        
#         # On définit les x et y qui délimiteront notre aire sous la courbe grace à z car unilatéral
#         x = np.arange(-10, z, 0.001)
#         y2 = norm.pdf(x,0,scale)



#         # On trace la courbe
#         ax.plot(x_all,y)

#         # On limite nos abscisse entre -4 et 4
#         ax.set_xlim([-3.8*scale,4*scale])

#         # On remplit l'air sous notre courbe en fonction de x et y
#         ax.fill_between(x,y2,alpha=0.7, color='#ffcc00')
#         filled_poly = ax.fill_between(x_all,y, alpha=0.3, color='#ffcc00')

#         # On écrit la pourcentage d'aire remplit sous la courbe
#         (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
#         ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        
#         # On affiche les coordonnées de z
#         plt.xlabel('Z') 
#         plt.ylabel('Frequency') 
#         plt.xticks([z])
#         plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
#         # plt.show()
#         return fig 

#     def plot_unilateral_z(z,scale):
#         fig, ax = plt.subplots(figsize=(9,6))
#         # On définit les x_all et y2 pour tracer un courbe de gauss
#         x_all = np.arange(-10, 10, 0.001)
#         y2 = norm.pdf(x_all,0,scale)

#         # On définit les x et y qui délimiteront notre aire sous la courbe grace à z car unilatéral
#         x = np.arange(-10, z, 0.001)
#         y = norm.pdf(x,0,scale)
#         # y se limite à x pour l'aire
        
#         ax.plot(x_all,y2)
#         # On limite nos abscisse entre -4 et 4
#         ax.set_xlim([-3.8*1,3.8*1])
       
#         # On calcul la probabilité qui correspond à notre Zscore
#         aire = norm.cdf(z,0,scale)

#         # On remplit l'air sous notre courbe en fonction de x et y
#         ax.fill_between(x, y, alpha=0.7, color='#ffcc00')
#         filled_poly = ax.fill_between(x_all,y2,0, alpha=0.3, color='#ffcc00')

#         # On écrit la pourcentage d'aire remplit sous la courbe
#         (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
#         ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        
#         plt.xlabel('Z') 
#         plt.ylabel('Frequency') 
#         plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
#         # plt.show()
#         return fig

#     def plot_bilateral_z(z,scale):
#         fig, ax = plt.subplots(figsize=(9,6))
#         # On définit les x_all et y2 pour tracer un courbe de gauss
#         x_all = np.arange(-10, 10, 0.001)
#         y2 = norm.pdf(x_all,0,scale)
#         # On définit les x et y qui délimiteront notre aire sous la courbe grace à z et -z car bilatéral
#         x = np.arange(-z, z, 0.001)
#         y = norm.pdf(x,0,scale)
#         ax.plot(x_all,y2)
#         # On limite nos abscisse entre -4 et 4
#         ax.set_xlim([-3.8*scale,3.8*scale])
#         # On calcul la probabilité qui correspond à notre Zscore (ne pas oublier on est en bilatéral)
#         aire = (norm.cdf(z,0,scale)-0.5)*2
#         # On remplit l'air sous notre courbe en fonction de x et y
#         ax.fill_between(x,y, alpha=0.7, color='#ffcc00', label=aire)
#         # On écrit la pourcentage d'aire remplit sous la courbe
#         filled_poly = ax.fill_between(x_all,y2,0, alpha=0.3, color='#ffcc00')
#         (x0, y0), (x1, y1) = filled_poly.get_paths()[0].get_extents().get_points()
#         ax.text((x0 + x1) / 2, (y0 + y1) / 2, round(aire,3), ha='center', va='center', fontsize=16, color='crimson')
        
#         plt.xlabel('Z') 
#         plt.ylabel('Frequency') 
#         plt.yticks([0,.1,.2,.3,.4,.5,.6,.7,.8])
#         # plt.show()
#         return fig
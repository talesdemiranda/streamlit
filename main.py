import streamlit as st
from streamlit_option_menu import option_menu
import seguranca.seguranca as seguranca

st.set_page_config("Projeto Stremlit Tales", layout="wide")

if seguranca.check_password():

	menu_esquerdo              = ["Cadastro", "Adesão", "Arrecadação", "Instituto", "Configuração"]
	menu_esquerdo_icone        = ['people-fill', 'card-list', 'cash-coin', 'bounding-box', 'gear']

	with st.sidebar:
		
		#image = Image.open(local_image)
		#st.image(image, width=30, )

		selected_left_menu = option_menu("Tales",
													menu_esquerdo, 
													icons=menu_esquerdo_icone,
													menu_icon="eyeglasses",
													default_index=0
									)

import streamlit as st

# 1. Configuración de la página
st.set_page_config(page_title="Calculadora de rebajas", page_icon="💵")

# Título y Descripción
st.title("💵 Calculadora de rebajas")
st.markdown("Bienvenido. Introduce el precio original y el porcentaje de descuento.")
st.write("---") # Línea separadora

# 2. Entrada de Datos (Barra Lateral)
st.sidebar.header("Datos del Producto")
precio_original= st.sidebar.number_input("Precio original (€)", min_value=0.0, max_value=10000.0, value=100.0)
descuento = st.sidebar.slider("Porcentaje del descuento (%)", 0, 100, 40)
# 3. Botón de Cálculo y Lógica
if st.button("Calcular rebaja"):
    
    # Cálculos
    cantidad_descuento = precio_original * (descuento / 100)
    precio_final = precio_original - cantidad_descuento
    
    # 4. Mostrar Resultado con Diseño
    col1, col3 = st.columns(2)
    
    with col1:
        # Usamos metric para que el número se vea grande
        st.metric(label="Precio final:", value=f"{precio_final:.2f} €", delta=f"-{cantidad_descuento:.2f} €")
        
    with col3:
     if descuento == 0:
         st.info("Sin descuento aplicado.")
            

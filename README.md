# vehicles_dashboard_project
Panel de control web para visualizar datos de vehículos.

Esta aplicación web permite explorar un conjunto de datos de anuncios de vehículos en EE.UU. Utiliza Streamlit para mostrar visualizaciones interactivas como histogramas y gráficos de dispersión, creados con Plotly Express. Permite visualizar relaciones clave entre variables como precio, kilometraje, año del modelo, condición del vehículo y duración del anuncio.

## Funcionalidades

La app incluye los siguientes componentes interactivos:

- **Botón: Histograma de kilometraje**  
  Muestra la distribución de los valores de `odometer` (kilometraje) en los anuncios.

- **Botón: Dispersión año vs. precio**  
  Visualiza la relación entre el año del modelo (`model_year`) y el precio (`price`).

- **Casilla: Histograma de precios**  
  Permite ver cómo se distribuyen los precios de los vehículos anunciados.

- **Casilla: Histograma de días listados**  
  Muestra cuántos días permanecen publicados los anuncios (`days_listed`).

- **Casilla: Dispersión condición vs. precio**  
  Compara el estado del vehículo (`condition`) con su precio.

Link para ver el render: https://vehicles-dashboard-project.onrender.com

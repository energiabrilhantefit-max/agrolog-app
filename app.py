import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium
import plotly.express as px

# Configuração da Página
st.set_page_config(
    page_title="AgroLog | Intelligence & AgTech", 
    page_icon="🌿", 
    layout="wide"
)

# Estilização Corporativa Avançada (Padrão AgTech / AgroHub)
st.markdown("""
    <style>
        .main { background-color: #f4f6f8; color: #212529; }
        .exec-navbar {
            background-color: #1b4332;
            color: white;
            padding: 15px 25px;
            border-radius: 10px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
            box-shadow: 0 4px 10px rgba(0,0,0,0.08);
        }
        .exec-navbar h2 { margin: 0; font-size: 22px; color: white; }
        .exec-navbar p { margin: 0; font-size: 14px; color: #b7e4c7; }
        .stTabs [data-baseweb="tab-list"] { gap: 8px; overflow-x: auto; }
        .stTabs [data-baseweb="tab"] {
            background-color: #ffffff;
            border-radius: 8px 8px 0px 0px;
            padding: 12px 24px;
            font-weight: 600;
            color: #495057;
            border: 1px solid #dee2e6;
            border-bottom: none;
        }
        .stTabs [aria-selected="true"] {
            background-color: #1b4332 !important;
            color: white !important;
            border-color: #1b4332 !important;
        }
        .card-relevo {
            background-color: #ffffff;
            padding: 24px;
            border-radius: 12px;
            box-shadow: 0 4px 16px rgba(0, 0, 0, 0.04);
            border: 1px solid #e9ecef;
            margin-bottom: 20px;
            color: #212529;
        }
        .stButton>button {
            background: linear-gradient(135deg, #2d6a4f 0%, #1b4332 100%);
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: 600;
            border: none;
            box-shadow: 0 4px 6px rgba(27, 67, 50, 0.2);
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #40916c 0%, #2d6a4f 100%);
        }
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            padding: 18px;
            border-radius: 10px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.03);
            border: 1px solid #e9ecef;
            border-left: 5px solid #2d6a4f;
        }
        div[data-testid="stMetric"] label { color: #6c757d !important; font-weight: 500; }
        div[data-testid="stMetric"] div[data-testid="stMetricValue"] { color: #1b4332 !important; font-weight: 700; }
    </style>
""", unsafe_allow_html=True)

# Navbar Superior Institucional
st.markdown("""
    <div class="exec-navbar">
        <div>
            <h2>🌿 AgroLog | Intelligence & AgTech</h2>
            <p>Projeto Integrado de Safra: Lavoura de Algodão (2.000 ha) | Sapezal - MT</p>
        </div>
        <div style="text-align: right;">
            <strong>Safra 2026/2027</strong><br>
            <span style="font-size: 12px; color: #95d5b2;">● Status: Planejamento Executivo Ativo</span>
        </div>
    </div>
""", unsafe_allow_html=True)

# Métricas globais de topo
col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)
col_m1.metric("Área Total", "2.000 ha", "4 Módulos de 500 ha")
col_m2.metric("Cultura", "Algodão 1ª Safra", "Plantio Direto")
col_m3.metric("Solo (Argila)", "36%", "Latossolo Vermelho")
col_m4.metric("Custo Est. / ha", "R$ 9.503", "Total: R$ 19.0M")
col_m5.metric("Média Projetada", "380,7 @/ha", "Alta Performance")

st.markdown("<br>", unsafe_allow_html=True)

# Abas do Sistema Corporativo
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🗺️ 1. Área, Solo & Mapa", 
    "🌱 2. Cultivares & Semeadura", 
    "🧪 3. Adubação & Fitossanidade", 
    "🚜 4. Manejo & Reguladores", 
    "📊 5. Produtividade & Orçamento"
])

# -------------------------------------------------------------
# ABA 1: Área, Solo & Mapa
# -------------------------------------------------------------
with tab1:
    st.subheader("3. Caracterização da Área, Solo e Zoneamento da Fazenda")
    
    col_mapa, col_info = st.columns([2, 1])
    
    with col_mapa:
        st.markdown("##### 🗺️ Georreferenciamento e Talhagem Exata (Sapezal - MT)")
        
        m = folium.Map(location=[-13.510, -58.730], zoom_start=13, tiles="OpenStreetMap")
        
        talhao_1 = [
            [-13.53981844368093, -58.76215056237926], 
            [-13.51556638810488, -58.75557987760351], 
            [-13.51571840529931, -58.77219463593266], 
            [-13.53971974074189, -58.78003002920741]
        ]
        folium.Polygon(locations=talhao_1, color="#2b8a3e", fill=True, fill_color="#2b8a3e", fill_opacity=0.5, popup="<b>Módulo 01 (500 ha)</b><br>Variedade: TMG 44B2RF").add_to(m)

        talhao_2 = [
            [-13.51579093994054, -58.77242055287298], 
            [-13.5166443672907, -58.79275669430474], 
            [-13.53930760240549, -58.79553135734952], 
            [-13.5397166672417, -58.7800509353763]
        ]
        folium.Polygon(locations=talhao_2, color="#1c7ed6", fill=True, fill_color="#1c7ed6", fill_opacity=0.5, popup="<b>Módulo 02 (500 ha)</b><br>Variedade: FM 944GL (Refúgio)").add_to(m)

        talhao_3 = [
            [-13.515564513977, -58.7555799062929], 
            [-13.50331489163625, -58.75230235807538], 
            [-13.50301838049903, -58.78055534007193], 
            [-13.51640607230507, -58.79256547962144]
        ]
        folium.Polygon(locations=talhao_3, color="#f59f00", fill=True, fill_color="#f59f00", fill_opacity=0.5, popup="<b>Módulo 03 (500 ha)</b><br>Variedade: FM 911GLTP").add_to(m)

        talhao_4 = [
            [-13.51391496859024, -58.75507848180665], 
            [-13.53982841151284, -58.76200120441727], 
            [-13.53978621099757, -58.74543469684172], 
            [-13.51361342653583, -58.7395983024997]
        ]
        folium.Polygon(locations=talhao_4, color="#ae3ec9", fill=True, fill_color="#ae3ec9", fill_opacity=0.5, popup="<b>Módulo 04 (500 ha)</b><br>Variedade: FM 985GLTP").add_to(m)

        folium.Marker(location=[-13.53884590793322, -58.77861906148395], popup="<b>Sede da Fazenda</b>", icon=folium.Icon(color="red", icon="home", prefix="fa")).add_to(m)
        folium.Marker(location=[-13.53490048463956, -58.7968581578988], popup="<b>Armazém & Beneficiamento</b>", icon=folium.Icon(color="blue", icon="warehouse", prefix="fa")).add_to(m)

        st_folium(m, width=650, height=430)

    with col_info:
        st.markdown(
            '<div class="card-relevo">'
            '<h4>📋 Parâmetros da Área</h4>'
            '<ul>'
            '<li><b>Localização:</b> Sapezal - MT (Altitude 581m).</li>'
            '<li><b>Área Produtiva:</b> 2.000 ha (4 módulos de 500 ha).</li>'
            '<li><b>Topografia:</b> Plano a suave ondulado.</li>'
            '<li><b>Tipo de Solo:</b> Latossolo Vermelho Distroférico (36% Argila).</li>'
            '<li><b>Sistema:</b> Plantio Direto (SPD) sobre palhada.</li>'
            '</ul>'
            '</div>', 
            unsafe_allow_html=True
        )
        if st.button("📥 Exportar Relatório Executivo"):
            st.success("Relatório gerado com sucesso!")

# -------------------------------------------------------------
# ABA 2: Cultivares & Semeadura
# -------------------------------------------------------------
with tab2:
    st.subheader("2, 5, 6 e 7. Escolha de Variedades e Parâmetros de Semeadura")
    df_cultivares = pd.DataFrame({
        'Módulo / Variedade': ['Módulo 1: TMG 44B2RF', 'Módulo 2: FM 944GL (Refúgio)', 'Módulo 3: FM 911GLTP', 'Módulo 4: FM 985GLTP'],
        'Tecnologia': ['Bollgard II / RR Flex', 'GlyTol / LibertyLink', 'TwinLink Plus (Bt)', 'TwinLink Plus (Bt)'],
        'Ciclo': ['Médio-Precoce', '160-180 dias', '140-180 dias (Precoce)', '180-190 dias (Tardio)'],
        'População (pl/ha)': ['110.000', '100.000', '100.000', '90.000'],
        'Emergência Esperada': ['93%', '95%', '96%', '98%'],
        'Peso 1.000 Sementes': ['78 g', '88 g', '102 g', '88 g']
    })
    st.markdown('<div class="card-relevo">', unsafe_allow_html=True)
    st.dataframe(df_cultivares, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------------------
# ABA 3: Adubação & Fitossanidade
# -------------------------------------------------------------
with tab3:
    st.subheader("8, 9, 10 e 11. Adubação NPK e Manejo Fitossanitário Avançado")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(
            '<div class="card-relevo">'
            '<h4>🧪 8. Adubação de Base e Cobertura</h4>'
            '<p><b>Fósforo:</b> Superfosfato Simples (SSP) fornecendo 135 kg/ha de P2O5, Ca (120 kg/ha) e Enxofre (75 kg/ha).</p>'
            '<p><b>Nitrogênio e Potássio:</b> Ureia (160 kg N/ha) e Cloreto de Potássio (180 kg K2O/ha).</p>'
            '</div>', 
            unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            '<div class="card-relevo">'
            '<h4>🪲 10. Controle de Pragas e Doenças</h4>'
            '<p><b>Bicudo e Ramulária:</b> Monitoramento com armadilhas de feromônio, controle químico preventivo e destruição rigorosa de soqueiras.</p>'
            '<p><b>Lagarta-Rosada:</b> Proteção Bt combinada com o refúgio estruturado de 25%.</p>'
            '</div>', 
            unsafe_allow_html=True
        )

# -------------------------------------------------------------
# ABA 4: Manejo & Reguladores
# -------------------------------------------------------------
with tab4:
    st.subheader("12 e 13. Reguladores de Crescimento, Desfolha e Maturação")
    st.markdown(
        '<div class="card-relevo">'
        '<h4>🌿 Manejo Fisiológico e Final de Ciclo</h4>'
        '<p><b>Regulador de Crescimento:</b> Cloreto de Mepiquat parcelado para evitar o acamamento e o excesso vegetativo.</p>'
        '<p><b>Desfolha e Maturação:</b> Uso de Etefon e desfolhantes químicos para uniformizar a abertura dos capulhos e antecipar a colheita limpa.</p>'
        '</div>', 
        unsafe_allow_html=True
    )

# -------------------------------------------------------------
# ABA 5: Produtividade & Orçamento
# -------------------------------------------------------------
with tab5:
    st.subheader("14 e 15. Estimativa de Produtividade, Gráficos e Orçamento")
    
    df_prod = pd.DataFrame({
        'Cultivar': ['TMG 44B2RF', 'FM 944GL', 'FM 911GLTP', 'FM 985GLTP'],
        'Capulhos/Planta': [12, 11, 13, 12],
        'Peso Capulho': ['4,5 g', '5,0 g', '4,7 g', '4,9 g'],
        'Produtividade (kg/ha)': [5940, 5500, 6110, 5292],
        'Produtividade (@/ha)': ['396,0 @', '366,6 @', '407,3 @', '352,8 @']
    })
    
    st.markdown('<div class="card-relevo">', unsafe_allow_html=True)
    st.markdown("##### 📊 Simulação de Produtividade por Módulo")
    st.dataframe(df_prod, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    fig = px.bar(
        df_prod, 
        x='Cultivar', 
        y='Produtividade (kg/ha)', 
        color='Cultivar',
        text='Produtividade (kg/ha)',
        title="<b>Comparativo de Produtividade por Cultivar (kg/ha)</b>"
    )
    fig.update_traces(textposition='outside')
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 💰 15. Orçamento de Custos Variáveis (Safra 2026/2027)")
    df_orc = pd.DataFrame({
        'Item de Custo': ['Sementes & Biotecnologia', 'Corretivos de Solo', 'Fertilizantes NPK & Nutrição', 'Defensivos (Fungicidas/Inseticidas/Herbicidas)', 'Regulador de Crescimento', 'Desfolhantes & Maturadores', 'Operações Mecanizadas & Combustível'],
        'R$ / ha': ['R$ 650,00', 'R$ 420,00', 'R$ 3.850,00', 'R$ 2.943,12', 'R$ 180,00', 'R$ 260,00', 'R$ 1.200,00'],
        'Total (2.000 ha - R$)': ['R$ 1.300.000,00', 'R$ 840.000,00', 'R$ 7.700.000,00', 'R$ 5.886.250,00', 'R$ 360.000,00', 'R$ 520.000,00', 'R$ 2.400.000,00']
    })
    
    st.markdown('<div class="card-relevo">', unsafe_allow_html=True)
    st.dataframe(df_orc, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.success("💰 **Custo Variável Total da Lavoura:** R$ 19.006.250,00 (Média de **R$ 9.503,12 / ha**).")

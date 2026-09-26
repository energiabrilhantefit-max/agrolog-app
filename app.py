import streamlit as st
import pandas as pd
import folium
from streamlit_folium import st_folium

# Configuração da Página
st.set_page_config(
    page_title="AgroLog - Gestão Agronômica de Algodão", 
    page_icon="🌿", 
    layout="wide"
)

# Estilização Profissional Avançada (Cores, Efeitos de Relevo e Sombra)
st.markdown("""
    <style>
        /* Fundo geral da página */
        .main { background-color: #f4f6f8; }
        
        /* Estilização das Abas (Tabs) */
        .stTabs [data-baseweb="tab-list"] { gap: 8px; }
        .stTabs [data-baseweb="tab"] {
            background-color: #ffffff;
            border-radius: 8px 8px 0px 0px;
            padding: 12px 24px;
            font-weight: 600;
            color: #495057;
            border: 1px solid #dee2e6;
            border-bottom: none;
            box-shadow: 0 -2px 5px rgba(0,0,0,0.02);
        }
        .stTabs [aria-selected="true"] {
            background-color: #1b4332 !important;
            color: white !important;
            border-color: #1b4332 !important;
        }

        /* Cartões em Relevo (Efeito Sombra/Profundidade) */
        .card-relevo {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
            border: 1px solid #e9ecef;
            margin-bottom: 20px;
        }

        /* Botões em Relevo Personalizados */
        .stButton>button {
            background: linear-gradient(135deg, #2d6a4f 0%, #1b4332 100%);
            color: white;
            border-radius: 8px;
            padding: 10px 24px;
            font-weight: 600;
            border: none;
            box-shadow: 0 4px 6px rgba(27, 67, 50, 0.2);
            transition: all 0.3s ease;
        }
        .stButton>button:hover {
            background: linear-gradient(135deg, #40916c 0%, #2d6a4f 100%);
            box-shadow: 0 6px 12px rgba(27, 67, 50, 0.3);
            transform: translateY(-2px);
        }

        /* Ajuste de Métricas para visual mais limpo */
        div[data-testid="stMetric"] {
            background-color: #ffffff;
            padding: 15px;
            border-radius: 10px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.04);
            border-left: 5px solid #2d6a4f;
        }
    </style>
""", unsafe_allow_html=True)

# Cabeçalho Principal do Sistema
st.title("🌿 AgroLog | Plataforma de Inteligência Agrícola")
st.markdown("**Projeto Integrado de Safra: Lavoura de Algodão (2.000 ha) | Sapezal - MT**")
st.divider()

# Métricas globais de topo
col_m1, col_m2, col_m3, col_m4, col_m5 = st.columns(5)
col_m1.metric("Área Total", "2.000 ha", "4 Talhões de 500 ha")
col_m2.metric("Cultura", "Algodão 1ª Safra", "Ciclo 2026/2027")
col_m3.metric("Solo (Argila)", "55%", "Latossolo Vermelho")
col_m4.metric("Custo Est. / ha", "R$ 5.400", "Total: R$ 10.8M")
col_m5.metric("Produtividade", "~315 @/ha", "Alta Performance")

st.markdown("<br>", unsafe_allow_html=True)

# Criação das Abas Integradas
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
        st.markdown("##### 🗺️ Georreferenciamento e Talhagem (Sapezal - MT)")
        
        # Mapa centralizado na área da fazenda em Sapezal com as coordenadas reais
        m = folium.Map(location=[-13.510, -58.730], zoom_start=13, tiles="OpenStreetMap")
        
        # Talhão 01 - Variedade 1 (500 ha)
        talhao_1 = [
            [-13.53981844368093, -58.76215056237926], 
            [-13.51556638810488, -58.75557987760351], 
            [-13.51571840529931, -58.77219463593266], 
            [-13.53971974074189, -58.78003002920741]
        ]
        folium.Polygon(
            locations=talhao_1, color="#2b8a3e", fill=True, fill_color="#2b8a3e", fill_opacity=0.5,
            popup="<b>Talhão 01 (500 ha)</b><br>Variedade: TMG 824 B2RF"
        ).add_to(m)

        # Talhão 02 - Variedade 2 (500 ha)
        talhao_2 = [
            [-13.51579093994054, -58.77242055287298], 
            [-13.5166443672907, -58.79275669430474], 
            [-13.53930760240549, -58.79553135734952], 
            [-13.5397166672417, -58.7800509353763]
        ]
        folium.Polygon(
            locations=talhao_2, color="#1c7ed6", fill=True, fill_color="#1c7ed6", fill_opacity=0.5,
            popup="<b>Talhão 02 (500 ha)</b><br>Variedade: TMG 81WS"
        ).add_to(m)

        # Talhão 03 - Variedade 3 (500 ha)
        talhao_3 = [
            [-13.515564513977, -58.7555799062929], 
            [-13.50331489163625, -58.75230235807538], 
            [-13.50301838049903, -58.78055534007193], 
            [-13.51640607230507, -58.79256547962144]
        ]
        folium.Polygon(
            locations=talhao_3, color="#f59f00", fill=True, fill_color="#f59f00", fill_opacity=0.5,
            popup="<b>Talhão 03 (500 ha)</b><br>Variedade: IMA 5801 B2RF"
        ).add_to(m)

        # Talhão 04 - Variedade 4 (500 ha)
        talhao_4 = [
            [-13.51391496859024, -58.75507848180665], 
            [-13.53982841151284, -58.76200120441727], 
            [-13.53978621099757, -58.74543469684172], 
            [-13.51361342653583, -58.7395983024997]
        ]
        folium.Polygon(
            locations=talhao_4, color="#ae3ec9", fill=True, fill_color="#ae3ec9", fill_opacity=0.5,
            popup="<b>Talhão 04 (500 ha)</b><br>Variedade: FM 985 GLTP"
        ).add_to(m)

        # Marcador da Sede
        folium.Marker(
            location=[-13.53884590793322, -58.77861906148395],
            popup="<b>Sede da Fazenda</b><br>Escritório Central, Residência e Apoio Operacional",
            icon=folium.Icon(color="red", icon="home", prefix="fa")
        ).add_to(m)

        # Marcador do Armazém
        folium.Marker(
            location=[-13.53490048463956, -58.7968581578988],
            popup="<b>Armazém & Unidade de Beneficiamento</b>",
            icon=folium.Icon(color="blue", icon="warehouse", prefix="fa")
        ).add_to(m)

        st_folium(m, width=650, height=430)

    with col_info:
        st.markdown("""
            <div class="card-relevo">
                <h4>📋 Parâmetros da Área</h4>
                <ul>
                    <li><b>Localização:</b> Sapezal - MT (Chapadão).</li>
                    <li><b>Área Total:</b> 2.000 hectares (4 blocos de 500 ha).</li>
                    <li><b>Topografia:</b> Plano a suave ondulado (0,5% a 2%).</li>
                    <li><b>Tipo de Solo:</b> Latossolo Vermelho Distroférrico (~55% argila).</li>
                    <li><b>Histórico:</b> Área consolidada em plantio direto (rotação com soja).</li>
                    <li><b>Correção:</b> Calcário dolomítico + Gessagem (400 kg/ha).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)
        
        if st.button("📥 Exportar Relatório da Área"):
            st.success("Relatório da área exportado com sucesso!")
    
    st.info("💡 **Estratégia de 1ª Safra:** O algodão entra como cultura principal, aproveitando o regime regular de chuvas do final do ano.")

# -------------------------------------------------------------
# ABA 2: Cultivares & Semeadura
# -------------------------------------------------------------
with tab2:
    st.subheader("2, 5, 6 e 7. Escolha de Variedades e Parâmetros de Semeadura")
    
    df_cultivares = pd.DataFrame({
        'Variedade': ['Var 1: TMG 824 B2RF', 'Var 2: TMG 81WS', 'Var 3: IMA 5801 B2RF', 'Var 4: FM 985 GLTP'],
        'Tecnologia': ['Bollgard II / RR', 'WideSect / RR', 'Bollgard II / RR', 'GlyTol / TwinLink+'],
        'Ciclo': ['Médio (150-160 d)', 'Precoce (140-150 d)', 'Médio (155 d)', 'Precoce (145 d)'],
        'Espaçamento': ['0,76 m', '0,76 m', '0,76 m', '0,76 m'],
        'População (pl/ha)': ['95.000', '100.000', '90.000', '95.000'],
        'Emergência (%)': ['93%', '95%', '96%', '98%'],
        'Peso 100 sem': ['12,0 g', '11,5 g', '12,5 g', '11,8 g']
    })
    
    st.markdown('<div class="card-relevo">', unsafe_allow_html=True)
    st.dataframe(df_cultivares, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 🧮 Estimativa de Sementes (por hectare e total na área)")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Sementes Var 1", "24,8 kg/ha", "Total: 49,6 t")
    col2.metric("Sementes Var 2", "24,2 kg/ha", "Total: 48,4 t")
    col3.metric("Sementes Var 3", "24,7 kg/ha", "Total: 49,4 t")
    col4.metric("Sementes Var 4", "23,6 kg/ha", "Total: 47,2 t")
    st.caption("*Cálculo baseado em 500 hectares dedicados para cada uma das 4 variedades.*")

# -------------------------------------------------------------
# ABA 3: Adubação & Fitossanidade
# -------------------------------------------------------------
with tab3:
    st.subheader("8, 9, 10 e 11. Adubação NPK e Manejo Fitossanitário")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="card-relevo">
                <h4>🧪 8. Adubação NPK</h4>
                <p>Uso de adubo formulado <b>04-30-16</b> no plantio (400 kg/ha &rarr; 800 t total) e cobertura planejada com Ureia e Cloreto de Potássio.</p>
                <hr>
                <h4>🦠 9. Ramularia e Mofo Branco</h4>
                <p><b>Ramularia:</b> Rotação rigorosa de fungicidas multissítios com sistêmicos preventivos a cada 7-10 dias.</p>
                <p><b>Mofo Branco:</b> Tratamento de sementes com biológicos (<i>Trichoderma</i>) e manutenção de palhada em cobertura.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card-relevo">
                <h4>🪲 10. Bicudo e Lagarta Rosada</h4>
                <p><b>Bicudo-do-algodoeiro:</b> Monitoramento com armadilhas de feromônio, controle químico focal (Malathion) e rigor na destruição de plantas tiguera.</p>
                <p><b>Lagarta Rosada:</b> Uso de cultivares transgênicas com refúgio estruturado obrigatório de 20% e liberação de <i>Trichogramma</i>.</p>
                <hr>
                <h4>🌾 11. Plantas Daninhas</h4>
                <p>Manejo integrado combinando herbicidas pré-emergentes seletivos e aplicações sequenciais de Glifosato nas cultivares tolerantes.</p>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# ABA 4: Manejo & Reguladores
# -------------------------------------------------------------
with tab4:
    st.subheader("12 e 13. Reguladores de Crescimento, Desfolha e Maturação")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
            <div class="card-relevo">
                <h4>🌿 12. Regulador de Crescimento</h4>
                <p>Aplicações parceladas de <b>Cloreto de Mepiquat</b> para controle preciso do porte vegetativo, evitando o acamamento e otimizando a retenção de capulhos e a penetração de luz no dossel.</p>
            </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div class="card-relevo">
                <h4>🍂 13. Desfolha, Maturador e Dessecação</h4>
                <p>Operações realizadas na fase final de maturação (140-150 dias):</p>
                <ul>
                    <li><b>Desfolhantes:</b> Indução química da queda controlada de folhas (Thidiazuron + Diuron).</li>
                    <li><b>Maturadores:</b> Aceleração da abertura uniforme dos capulhos para colheita eficiente (Etefông).</li>
                </ul>
            </div>
        """, unsafe_allow_html=True)

# -------------------------------------------------------------
# ABA 5: Produtividade & Orçamento
# -------------------------------------------------------------
with tab5:
    st.subheader("14 e 15. Estimativa de Produtividade e Orçamento Detalhado")
    
    df_prod = pd.DataFrame({
        'Variedade': ['Var 1 (TMG 824)', 'Var 2 (TMG 81WS)', 'Var 3 (IMA 5801)', 'Var 4 (FM 985)'],
        'Capulhos/Planta': [12, 11, 13, 12],
        'Peso Capulho': ['4,5 g', '5,0 g', '4,7 g', '4,9 g'],
        'Produtividade Estimada': ['~306 @/ha', '~319 @/ha', '~319 @/ha', '~318 @/ha']
    })
    
    st.markdown('<div class="card-relevo">', unsafe_allow_html=True)
    st.markdown("##### 📊 Estimativa de Produtividade por Talhão / Variedade")
    st.dataframe(df_prod, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### 💰 15. Orçamento de Custos Variáveis (Simulação por Hectare)")
    df_orc = pd.DataFrame({
        'Item de Custo': ['Sementes', 'Corretivo (Calcário/Gesso)', 'Fertilizantes (NPK + Cobertura)', 'Defensivos (Inseticidas/Fungicidas)', 'Regulador de Crescimento', 'Desfolhante / Maturador', 'Operações / Maquinário'],
        'R$ / ha': [650.00, 350.00, 1850.00, 1200.00, 250.00, 300.00, 800.00],
        'Total (2.000 ha - R$)': [1300000, 700000, 3700000, 2400000, 500000, 600000, 1600000]
    })
    
    st.markdown('<div class="card-relevo">', unsafe_allow_html=True)
    st.dataframe(df_orc, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.success("💰 **Custo Operacional Total Estimado:** R$ 10.800.000,00 na área total (~R$ 5.400,00 por hectare).")
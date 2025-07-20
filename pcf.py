import streamlit as st
from streamlit_echarts import st_echarts

# ----------------------------------------
# Page Setup
# ----------------------------------------
st.set_page_config(page_title="Lithium-ion Battery PCF", layout="wide")
st.title("🔋 Product Carbon Footprint Dashboard")

# ----------------------------------------
# Login + Disclaimer
# ----------------------------------------
with st.expander("🔐 Login & Disclaimer", expanded=True):
    username = st.text_input("ID")
    password = st.text_input("Password", type="password")
    st.warning("⚠️ All information shown is for demonstration purposes only. This dashboard is a mockup and contains fictional data without scientific basis.")

# ✅ 로그인 조건: ID = song, PW = 1234
if username == "song" and password == "1234":
    st.success("✅ Login successful!")

    # ----------------------------------------
    # Tabs
    # ----------------------------------------
    tab1, tab2, tab3, tab4 = st.tabs(["📘 Overview", "📈 Scenario", "🔗 Verification", "📄 Methodology"])

    # ----------------------------------------
    # 📘 OVERVIEW
    # ----------------------------------------
    with tab1:
        st.header("📘 Product Information")

        # Sidebar for options
        with st.sidebar:
            st.subheader("⚙️ LCA Options")
            coc_option = st.selectbox("Chain of Custody", ["Not Applied", "Applied"])
            mb_option = st.selectbox("Mass Balance", ["None", "Average", "50% Credit", "100% Credit"])
            alloc_option = st.radio("Allocation Method", ["Cut-off", "Economic", "Energy-based"])

        st.image(
            r"C:\Users\User\Downloads\li-ion20battery.jpg",
            caption="Image: Lithium-ion Battery Cells", 
        )

        st.markdown("""
        | **Field**               | **Value**                         |
        |-------------------------|------------------------------------|
        | Product Name            | Lithium-ion Battery Pack (NMC)     |
        | Order Number            | xxx-2025-009                       |
        | Delivery Number         | xxx-787654                         |
        | Batch Number            | xxx-BATCH-7792                     |
        | Date of Delivery        | 2025-07-20                         |
        | Weight                  | 85.6 g                            |
        | Functional Unit         | 1 unit of battery                       |
        """)


        base_emission = 8.75
        mb_factor = {
            "None": 1.00,
            "Average": 0.95,
            "50% Credit": 0.75,
            "100% Credit": 0.50
        }
        alloc_factor = {
            "Cut-off": 1.0,
            "Economic": 1.1,
            "Energy-based": 0.9
        }

        final_emission = base_emission * mb_factor[mb_option] * alloc_factor[alloc_option]

        st.subheader(f"**Total Emissions:** {final_emission:.2f} kg CO₂e")
        st.subheader("Cradle-to-Gate Stage Breakdown")

        stage_labels = ["Raw material", "Production", "Transportation"]
        stage_values = [2.45, 6.05, 0.25]

        donut_option = {
            "tooltip": {"trigger": "item", "formatter": "{b}: {c} kg CO₂e ({d}%)"},
            "legend": {
                "orient": "horizontal",
                "left": "center",
                "bottom": "bottom",
                "data": stage_labels
            },
            "series": [
                {
                    "name": "Stage Emissions",
                    "type": "pie",
                    "radius": ["40%", "70%"],
                    "label": {"show": True, "position": "inside", "formatter": "{d}%"},
                    "emphasis": {
                        "label": {"show": True, "fontSize": 16, "fontWeight": "bold"}
                    },
                    "data": [
                        {"value": stage_values[0], "name": stage_labels[0]},
                        {"value": stage_values[1], "name": stage_labels[1]},
                        {"value": stage_values[2], "name": stage_labels[2]},
                    ]
                }
            ]
        }

        st_echarts(options=donut_option, height="500px")

    # ----------------------------------------
    # 📈 SCENARIO
    # ----------------------------------------
    with tab2:
    
        years = list(range(2020, 2051))
        pessimistic = [9.5 - 0.05 * (y - 2020) for y in years]
        neutral = [8.75 - 0.08 * (y - 2020) for y in years]
        optimistic = [8.75 - 0.12 * (y - 2020) for y in years]

        option = {
            "legend": {"data": ["Pessimistic", "Neutral", "Optimistic"]},
            "xAxis": {"type": "category", "data": years},
            "yAxis": {"type": "value", "name": "kg CO₂e"},
            "series": [
                {"name": "Pessimistic", "type": "line", "data": pessimistic, "lineStyle": {"color": "black"}},
                {"name": "Neutral", "type": "line", "data": neutral, "lineStyle": {"color": "red"}},
                {"name": "Optimistic", "type": "line", "data": optimistic, "lineStyle": {"color": "green"}},
            ]
        }

        st_echarts(options=option, height="500px")

    # ----------------------------------------
    # 🔗 VERIFICATION
    # ----------------------------------------
    with tab3:
        st.header("🔗 Digital Verification")
        st.markdown("Scan the QR code to access the official verification report:")
        st.image("https://api.qrserver.com/v1/create-qr-code/?data=https://example.com/lithium-battery-pcf&size=150x150")

    # ----------------------------------------
    # 📄 METHODOLOGY
    # ----------------------------------------
    with tab4:
        st.header("📄 Methodology & Declaration")
        st.markdown(f"""
        This PCF assessment is based on a **cradle-to-gate** boundary and follows international standards:

        - ✅ **Chain of Custody**: `{coc_option}`
        - ✅ **Mass Balance**: `{mb_option}`
        - ✅ **Allocation Method**: `{alloc_option}`  
        - 📦 Functional Unit: `1 kg battery`
        - 🧾 Data Sources: supplier-specific + ecoinvent v3.10
        - 🔍 Verified by: _xxx (Limited Assurance)_

        **Disclaimer**: This dashboard is conceptual and contains fictional results.
        """)
else:
    st.info("Please enter the correct ID and Password to access the dashboard.\n\n✅ ID and password is available in the link below.")


# ----------------------------------------
# Sidebar Option
# ----------------------------------------
st.sidebar.header("🧭 Select Options")
show_future = st.sidebar.checkbox("📈 Show Future Carbon Footprint")

# ----------------------------------------
# Scenario Graph (Conditional Display)
# ----------------------------------------
if show_future:
    st.header("📈 Scenario Trend (2020–2050)")

    years = list(range(2020, 2051))
    pessimistic = [8.75 - 0.05 * (y - 2020) for y in years]
    neutral = [8.75 - 0.08 * (y - 2020) for y in years]
    optimistic = [8.75 - 0.12 * (y - 2020) for y in years]

    scenario_option = {
        "tooltip": {"trigger": "axis"},
        "legend": {"data": ["Pessimistic", "Neutral", "Optimistic"]},
        "xAxis": {"type": "category", "data": years},
        "yAxis": {"type": "value", "name": "kg CO₂e"},
        "series": [
            {
                "name": "Pessimistic",
                "type": "line",
                "data": pessimistic,
                "lineStyle": {"color": "black"}
            },
            {
                "name": "Neutral",
                "type": "line",
                "data": neutral,
                "lineStyle": {"color": "red"}
            },
            {
                "name": "Optimistic",
                "type": "line",
                "data": optimistic,
                "lineStyle": {"color": "green"}
            },
        ]
    }

    st_echarts(options=scenario_option, height="500px")
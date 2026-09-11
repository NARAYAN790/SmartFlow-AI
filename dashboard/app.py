import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="SmartFlow AI",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================================================
# SESSION STATE
# =========================================================

if "page" not in st.session_state:
    st.session_state.page = "Dashboard"

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

.stApp {
    background: #eef3f7;
}

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* =======================================================
   SIDEBAR
   ======================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #071a30 0%, #0b3457 100%);
}

section[data-testid="stSidebar"] * {
    color: white;
}

/* SIDEBAR BRAND */

.sidebar-brand {
    text-align: center;
    padding: 10px 0 25px 0;
}

.sidebar-brand .icon {
    font-size: 36px;
}

.sidebar-brand .title {
    font-size: 24px;
    font-weight: 800;
}

.sidebar-brand .subtitle {
    font-size: 11px;
    color: #a9c0d1;
}

/* SIDEBAR MENU LABEL */

section[data-testid="stSidebar"] .stCaption {
    color: #91a9bb;
}

/* MODERN SIDEBAR BUTTONS */

section[data-testid="stSidebar"] .stButton {
    margin-bottom: 3px;
}

section[data-testid="stSidebar"] .stButton button {
    width: 100%;
    min-height: 44px;

    border: 1px solid transparent;
    border-radius: 12px;

    background: transparent;
    color: #dceaf3;

    text-align: left;

    padding: 11px 15px;

    font-size: 14px;
    font-weight: 600;

    transition:
        background 0.2s ease,
        border 0.2s ease,
        transform 0.2s ease;
}

section[data-testid="stSidebar"] .stButton button:hover {
    background: rgba(255, 255, 255, 0.10);
    border-color: rgba(255, 255, 255, 0.08);
    color: white;
    transform: translateX(3px);
}

section[data-testid="stSidebar"] .stButton button:focus {
    outline: none;
    box-shadow: none;
}

/* =======================================================
   HERO
   ======================================================= */

.hero {
    background: linear-gradient(110deg, #071b33, #0b5275);
    border-radius: 18px;
    padding: 28px 32px;
    color: white;
    margin-bottom: 22px;
}

.hero h1 {
    margin: 0;
    font-size: 32px;
}

.hero p {
    margin-top: 6px;
    color: #bdd6e5;
    font-size: 14px;
}

.badge {
    display: inline-block;
    margin-top: 12px;
    padding: 6px 12px;
    border: 1px solid rgba(255,255,255,0.25);
    border-radius: 20px;
    font-size: 11px;
}

/* =======================================================
   PAGE TITLE
   ======================================================= */

.page-title {
    font-size: 30px;
    font-weight: 800;
    color: #17344e;
    margin-bottom: 8px;
}

/* =======================================================
   SECTION
   ======================================================= */

.section-title {
    font-size: 18px;
    font-weight: 700;
    color: #17344e;
    margin-top: 12px;
}

.section-subtitle {
    font-size: 12px;
    color: #7c8b98;
    margin-bottom: 10px;
}

/* =======================================================
   FOOTER
   ======================================================= */

.footer {
    text-align: center;
    color: #84919c;
    font-size: 11px;
    margin-top: 25px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# LOAD ACTUAL SMARTFLOW DATA
# =========================================================

DATA_FILE = r"data\decision_results.csv"

if not os.path.exists(DATA_FILE):
    st.error(
        "SmartFlow data file not found. "
        "Please make sure data\\decision_results.csv exists."
    )
    st.stop()

df = pd.read_csv(DATA_FILE)


# =========================================================
# STANDARDIZE COLUMN NAMES
# =========================================================

required_columns = [
    "timestamp",
    "zone",
    "flow_rate_lpm",
    "consumption_liters",
    "duration_min",
    "severity"
]

missing_columns = [
    col
    for col in required_columns
    if col not in df.columns
]

if missing_columns:
    st.error(
        "Required columns are missing from decision_results.csv: "
        + ", ".join(missing_columns)
    )
    st.stop()


# =========================================================
# DATA PREPARATION
# =========================================================

df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce"
)

df["flow_rate_lpm"] = pd.to_numeric(
    df["flow_rate_lpm"],
    errors="coerce"
)

df["consumption_liters"] = pd.to_numeric(
    df["consumption_liters"],
    errors="coerce"
)

df["duration_min"] = pd.to_numeric(
    df["duration_min"],
    errors="coerce"
)

if "anomaly_score" in df.columns:
    df["anomaly_score"] = pd.to_numeric(
        df["anomaly_score"],
        errors="coerce"
    )

zones = sorted(
    df["zone"].dropna().unique().tolist()
)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("""
    <div class="sidebar-brand">
        <div class="icon">💧</div>
        <div class="title">SmartFlow AI</div>
        <div class="subtitle">
            AI-Enabled Smart Water Management
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.caption("MAIN MENU")

    # Dashboard
    if st.button(
        "⌂   Dashboard",
        use_container_width=True
    ):
        st.session_state.page = "Dashboard"
        st.rerun()

    # Water Flow Data
    if st.button(
        "◈   Water Flow Data",
        use_container_width=True
    ):
        st.session_state.page = "Water Flow Data"
        st.rerun()

    # Zone Analysis
    if st.button(
        "⌖   Zone Analysis",
        use_container_width=True
    ):
        st.session_state.page = "Zone Analysis"
        st.rerun()

    # AI Agent
    if st.button(
        "✦   AI Agent",
        use_container_width=True
    ):
        st.session_state.page = "AI Agent"
        st.rerun()

    # Reports
    if st.button(
        "▤   Reports",
        use_container_width=True
    ):
        st.session_state.page = "Reports"
        st.rerun()

    # Settings
    if st.button(
        "⚙   Settings",
        use_container_width=True
    ):
        st.session_state.page = "Settings"
        st.rerun()

    st.divider()

    st.caption("Greener Campus")
    st.caption("Smarter Tomorrow")


# =========================================================
# DASHBOARD
# =========================================================

if st.session_state.page == "Dashboard":

    # -----------------------------------------------------
    # HERO
    # -----------------------------------------------------

    st.markdown("""
    <div class="hero">
        <h1>💧 SmartFlow AI</h1>
        <p>AI-Enabled Smart Water Management System</p>
        <span class="badge">
            ● AI MONITORING SYSTEM &nbsp; | &nbsp; PROTOTYPE
        </span>
    </div>
    """, unsafe_allow_html=True)

    # -----------------------------------------------------
    # KPI
    # -----------------------------------------------------

    total = len(df)

    critical = int(
        (df["severity"] == "Critical").sum()
    )

    suspicious = int(
        (df["severity"] == "Suspicious").sum()
    )

    normal = int(
        (df["severity"] == "Normal").sum()
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Total Sensor Records",
        f"{total:,}",
        "Monitoring events"
    )

    c2.metric(
        "Critical Anomalies",
        f"{critical:,}",
        "Immediate attention"
    )

    c3.metric(
        "Suspicious Events",
        f"{suspicious:,}",
        "Needs monitoring"
    )

    c4.metric(
        "Normal Patterns",
        f"{normal:,}",
        "No immediate action"
    )

    st.write("")

    # -----------------------------------------------------
    # TABLE + ALERTS
    # -----------------------------------------------------

    left, right = st.columns([1.7, 1])

    with left:

        st.markdown(
            '<div class="section-title">'
            '📊 Water-Flow Monitoring'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'Latest processed sensor observations'
            '</div>',
            unsafe_allow_html=True
        )

        monitoring_columns = [
            "timestamp",
            "zone",
            "flow_rate_lpm",
            "consumption_liters",
            "duration_min",
            "severity"
        ]

        available_monitoring = [
            col
            for col in monitoring_columns
            if col in df.columns
        ]

        display_df = df[
            available_monitoring
        ].head(10).copy()

        display_df = display_df.rename(
            columns={
                "timestamp": "Timestamp",
                "zone": "Zone",
                "flow_rate_lpm": "Flow Rate (L/min)",
                "consumption_liters": "Consumption (L)",
                "duration_min": "Duration (min)",
                "severity": "Severity"
            }
        )

        st.dataframe(
            display_df,
            use_container_width=True,
            hide_index=True,
            height=350
        )

    with right:

        st.markdown(
            '<div class="section-title">'
            '🚨 Priority Alerts'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'High-priority events requiring attention'
            '</div>',
            unsafe_allow_html=True
        )

        alerts = df[
            df["severity"] == "Critical"
        ].head(5)

        if len(alerts) == 0:

            st.success(
                "No critical events detected."
            )

        else:

            for _, row in alerts.iterrows():

                st.error(
                    f"🔴 **{row['zone']}**\n\n"
                    f"Flow: "
                    f"{row['flow_rate_lpm']:.2f} L/min  |  "
                    f"Duration: "
                    f"{row['duration_min']:.2f} min\n\n"
                    f"Consumption: "
                    f"{row['consumption_liters']:.2f} L"
                )

    st.write("")

    # -----------------------------------------------------
    # CHARTS
    # -----------------------------------------------------

    chart1, chart2 = st.columns(2)

    with chart1:

        st.markdown(
            '<div class="section-title">'
            '📈 Anomaly Overview'
            '</div>',
            unsafe_allow_html=True
        )

        chart_data = pd.DataFrame({
            "Status": [
                "Normal",
                "Suspicious",
                "Critical"
            ],
            "Count": [
                normal,
                suspicious,
                critical
            ]
        })

        fig = px.bar(
            chart_data,
            x="Status",
            y="Count",
            text="Count"
        )

        fig.update_layout(
            height=330,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            plot_bgcolor="white",
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    with chart2:

        st.markdown(
            '<div class="section-title">'
            '🎯 Pattern Distribution'
            '</div>',
            unsafe_allow_html=True
        )

        fig = go.Figure(
            data=[
                go.Pie(
                    labels=[
                        "Normal",
                        "Suspicious",
                        "Critical"
                    ],
                    values=[
                        normal,
                        suspicious,
                        critical
                    ],
                    hole=0.60
                )
            ]
        )

        fig.update_layout(
            height=330,
            margin=dict(
                l=20,
                r=20,
                t=20,
                b=20
            ),
            paper_bgcolor="white"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

    # -----------------------------------------------------
    # AI + ZONE
    # -----------------------------------------------------

    ai_col, zone_col = st.columns(2)

    with ai_col:

        st.markdown(
            '<div class="section-title">'
            '🤖 SmartFlow AI Water Agent'
            '</div>',
            unsafe_allow_html=True
        )

        st.markdown(
            '<div class="section-subtitle">'
            'AI-assisted water usage analysis'
            '</div>',
            unsafe_allow_html=True
        )

        selected_zone = st.selectbox(
            "Select Zone",
            zones,
            key="dashboard_ai_zone"
        )

        if st.button(
            "🔍 Analyze Zone",
            key="dashboard_ai_button"
        ):

            zone_data = df[
                df["zone"] == selected_zone
            ]

            avg_flow = zone_data[
                "flow_rate_lpm"
            ].mean()

            critical_zone = int(
                (
                    zone_data["severity"]
                    == "Critical"
                ).sum()
            )

            suspicious_zone = int(
                (
                    zone_data["severity"]
                    == "Suspicious"
                ).sum()
            )

            st.write(
                f"**Zone:** {selected_zone}"
            )

            st.write(
                f"Average Flow: "
                f"**{avg_flow:.2f} L/min**"
            )

            st.write(
                f"Critical Events: "
                f"**{critical_zone}**"
            )

            st.write(
                f"Suspicious Events: "
                f"**{suspicious_zone}**"
            )

            if critical_zone > 0:

                st.warning(
                    f"Critical water-flow patterns detected "
                    f"in {selected_zone}. "
                    f"Immediate inspection is recommended."
                )

            elif suspicious_zone > 0:

                st.info(
                    f"Unusual water-flow patterns detected "
                    f"in {selected_zone}. "
                    f"Continue monitoring and schedule inspection."
                )

            else:

                st.success(
                    f"{selected_zone} is showing a normal "
                    f"water-flow pattern."
                )

    with zone_col:

        st.markdown(
            '<div class="section-title">'
            '📍 Zone-wise Summary'
            '</div>',
            unsafe_allow_html=True
        )

        zone_summary = (
            df.groupby(
                ["zone", "severity"]
            )
            .size()
            .unstack(fill_value=0)
            .reset_index()
        )

        for col in [
            "Normal",
            "Suspicious",
            "Critical"
        ]:

            if col not in zone_summary.columns:
                zone_summary[col] = 0

        zone_summary = zone_summary[
            [
                "zone",
                "Normal",
                "Suspicious",
                "Critical"
            ]
        ]

        zone_summary = zone_summary.rename(
            columns={
                "zone": "Zone"
            }
        )

        st.dataframe(
            zone_summary,
            use_container_width=True,
            hide_index=True,
            height=280
        )


# =========================================================
# WATER FLOW DATA
# =========================================================

elif st.session_state.page == "Water Flow Data":

    st.markdown(
        '<div class="page-title">'
        '📊 Water Flow Data'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Detailed sensor records and water consumption data."
    )

    col1, col2 = st.columns(2)

    with col1:

        zone_filter = st.selectbox(
            "Zone",
            ["All"] + zones,
            key="water_zone"
        )

    with col2:

        severity_filter = st.selectbox(
            "Severity",
            [
                "All",
                "Normal",
                "Suspicious",
                "Critical"
            ],
            key="water_severity"
        )

    filtered = df.copy()

    if zone_filter != "All":

        filtered = filtered[
            filtered["zone"] == zone_filter
        ]

    if severity_filter != "All":

        filtered = filtered[
            filtered["severity"] == severity_filter
        ]

    st.write("")

    st.metric(
        "Records Found",
        f"{len(filtered):,}"
    )

    display_filtered = filtered.rename(
        columns={
            "timestamp": "Timestamp",
            "zone": "Zone",
            "flow_rate_lpm": "Flow Rate (L/min)",
            "consumption_liters": "Consumption (L)",
            "duration_min": "Duration (min)",
            "severity": "Severity",
            "anomaly_score": "Anomaly Score"
        }
    )

    st.dataframe(
        display_filtered,
        use_container_width=True,
        hide_index=True,
        height=550
    )


# =========================================================
# ZONE ANALYSIS
# =========================================================

elif st.session_state.page == "Zone Analysis":

    st.markdown(
        '<div class="page-title">'
        '📍 Zone Analysis'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Compare water consumption and anomaly patterns across zones."
    )

    zone_stats = (
        df.groupby("zone")
        .agg(
            Records=("zone", "count"),
            Average_Flow=(
                "flow_rate_lpm",
                "mean"
            ),
            Average_Consumption=(
                "consumption_liters",
                "mean"
            )
        )
        .reset_index()
    )

    if "anomaly_score" in df.columns:

        anomaly_stats = (
            df.groupby("zone")[
                "anomaly_score"
            ]
            .mean()
            .reset_index()
        )

        zone_stats = zone_stats.merge(
            anomaly_stats,
            on="zone",
            how="left"
        )

        zone_stats = zone_stats.rename(
            columns={
                "anomaly_score": "Average_Anomaly"
            }
        )

    zone_stats["Average_Flow"] = (
        zone_stats["Average_Flow"].round(2)
    )

    zone_stats["Average_Consumption"] = (
        zone_stats["Average_Consumption"].round(2)
    )

    if "Average_Anomaly" in zone_stats.columns:

        zone_stats["Average_Anomaly"] = (
            zone_stats["Average_Anomaly"].round(3)
        )

    zone_stats = zone_stats.rename(
        columns={
            "zone": "Zone"
        }
    )

    st.dataframe(
        zone_stats,
        use_container_width=True,
        hide_index=True
    )

    fig = px.bar(
        zone_stats,
        x="Zone",
        y="Average_Consumption",
        title="Average Water Consumption by Zone"
    )

    fig.update_layout(
        height=450,
        xaxis_tickangle=-35,
        plot_bgcolor="white",
        paper_bgcolor="white"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# =========================================================
# AI AGENT
# =========================================================

elif st.session_state.page == "AI Agent":

    st.markdown(
        '<div class="page-title">'
        '🤖 SmartFlow AI Agent'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Analyze detected water-flow anomalies and "
        "generate maintenance recommendations."
    )

    agent_zones = sorted(
        df[
            df["severity"].isin(
                ["Critical", "Suspicious"]
            )
        ]["zone"]
        .dropna()
        .unique()
        .tolist()
    )

    if len(agent_zones) == 0:

        st.success(
            "No suspicious or critical events detected."
        )

    else:

        selected = st.selectbox(
            "Select Zone",
            agent_zones,
            key="ai_zone"
        )

        zone_data = df[
            df["zone"] == selected
        ]

        avg_flow = zone_data[
            "flow_rate_lpm"
        ].mean()

        avg_consumption = zone_data[
            "consumption_liters"
        ].mean()

        critical_events = int(
            (
                zone_data["severity"]
                == "Critical"
            ).sum()
        )

        suspicious_events = int(
            (
                zone_data["severity"]
                == "Suspicious"
            ).sum()
        )

        c1, c2, c3 = st.columns(3)

        c1.metric(
            "Average Flow",
            f"{avg_flow:.2f} L/min"
        )

        c2.metric(
            "Average Consumption",
            f"{avg_consumption:.2f} L"
        )

        c3.metric(
            "Critical Events",
            critical_events
        )

        if st.button(
            "🔍 Run AI Analysis",
            key="ai_run"
        ):

            critical_rows = zone_data[
                zone_data["severity"]
                == "Critical"
            ]

            suspicious_rows = zone_data[
                zone_data["severity"]
                == "Suspicious"
            ]

            if len(critical_rows) > 0:

                latest = critical_rows.iloc[0]

                st.error(
                    f"⚠️ Critical anomaly detected in "
                    f"**{selected}**."
                )

                if "reason" in latest.index:

                    st.write(
                        "**AI Explanation**"
                    )

                    st.info(
                        str(latest["reason"])
                    )

                if "recommended_action" in latest.index:

                    st.write(
                        "**Recommended Action**"
                    )

                    st.warning(
                        str(
                            latest[
                                "recommended_action"
                            ]
                        )
                    )

            elif len(suspicious_rows) > 0:

                latest = suspicious_rows.iloc[0]

                st.warning(
                    f"Unusual water-flow activity detected "
                    f"in **{selected}**."
                )

                if "reason" in latest.index:

                    st.write(
                        "**AI Explanation**"
                    )

                    st.info(
                        str(latest["reason"])
                    )

                if "recommended_action" in latest.index:

                    st.write(
                        "**Recommended Action**"
                    )

                    st.info(
                        str(
                            latest[
                                "recommended_action"
                            ]
                        )
                    )

            else:

                st.success(
                    f"{selected} is currently showing "
                    f"a normal monitoring pattern."
                )


# =========================================================
# REPORTS
# =========================================================

elif st.session_state.page == "Reports":

    st.markdown(
        '<div class="page-title">'
        '📄 Reports'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "SmartFlow AI system summary and downloadable report."
    )

    report_normal = int(
        (df["severity"] == "Normal").sum()
    )

    report_suspicious = int(
        (df["severity"] == "Suspicious").sum()
    )

    report_critical = int(
        (df["severity"] == "Critical").sum()
    )

    report_average_flow = df[
        "flow_rate_lpm"
    ].mean()

    report_total_consumption = df[
        "consumption_liters"
    ].sum()

    report = pd.DataFrame({
        "Metric": [
            "Total Records",
            "Normal Patterns",
            "Suspicious Events",
            "Critical Anomalies",
            "Number of Zones",
            "Average Flow",
            "Total Consumption"
        ],
        "Value": [
            f"{len(df):,}",
            f"{report_normal:,}",
            f"{report_suspicious:,}",
            f"{report_critical:,}",
            f"{len(zones)}",
            f"{report_average_flow:.2f} L/min",
            f"{report_total_consumption:,.2f} L"
        ]
    })

    st.dataframe(
        report,
        use_container_width=True,
        hide_index=True
    )

    st.write("")

    csv = df.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "⬇️ Download CSV Report",
        csv,
        "smartflow_report.csv",
        "text/csv",
        use_container_width=False
    )


# =========================================================
# SETTINGS
# =========================================================

elif st.session_state.page == "Settings":

    st.markdown(
        '<div class="page-title">'
        '⚙️ Settings'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Configure SmartFlow AI dashboard preferences."
    )

    st.checkbox(
        "Enable anomaly monitoring",
        value=True
    )

    st.checkbox(
        "Show priority alerts",
        value=True
    )

    st.checkbox(
        "Enable AI recommendations",
        value=True
    )

    st.slider(
        "Anomaly sensitivity",
        0.05,
        0.30,
        0.20,
        0.01
    )

    st.success(
        "Dashboard settings are ready."
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        SmartFlow AI | AI Monitoring System | Prototype Dashboard
    </div>
    """,
    unsafe_allow_html=True
)
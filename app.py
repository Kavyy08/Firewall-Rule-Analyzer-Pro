import streamlit as st
import pandas as pd
import plotly.express as px
from analyzer import calculate_risk
from report_generator import generate_report

st.set_page_config(
    page_title="Firewall Rule Analyzer Pro",
    layout="wide"
)

# =========================
# Sidebar
# =========================

st.sidebar.title("🛡 Navigation")

page = st.sidebar.radio(
    "Select Page",
    ["Dashboard", "Risk Analysis", "Reports"]
)

st.title("🛡️ Firewall Rule Analyzer Pro")

st.caption(
    "Security Posture Assessment & Firewall Audit Dashboard"
)

uploaded_file = st.file_uploader(
    "Upload Firewall Rules CSV",
    type=["csv"]
)

if uploaded_file:

    df = pd.read_csv(uploaded_file)

    critical = 0
    high = 0
    medium = 0
    low = 0

    scores = []

    for _, row in df.iterrows():

        score, severity, reasons, recommendations = calculate_risk(row)

        scores.append(score)

        if severity == "Critical":
            critical += 1

        elif severity == "High":
            high += 1

        elif severity == "Medium":
            medium += 1

        else:
            low += 1

    firewall_score = 100 - (sum(scores) / len(scores))
    total_rules = len(df)

    if critical > 0:
        overall_risk = "HIGH"

    elif high > 0:
        overall_risk = "MEDIUM"

    else:
        overall_risk = "LOW"

    # =========================
    # DASHBOARD PAGE
    # =========================

    if page == "Dashboard":

        col1, col2, col3, col4, col5 = st.columns(5)

        col1.metric(
            "Firewall Health",
            f"{firewall_score:.0f}%"
        )

        col2.metric("Critical", critical)
        col3.metric("High", high)
        col4.metric("Medium", medium)
        col5.metric("Low", low)

        if firewall_score >= 80:
            st.success("🟢 Firewall Security Status: GOOD")

        elif firewall_score >= 60:
            st.warning("🟡 Firewall Security Status: MODERATE")

        else:
            st.error("🔴 Firewall Security Status: HIGH RISK")

        st.divider()

        # Gauge Meter
        st.subheader("🛡 Security Posture Score")

        st.progress(int(firewall_score))

        st.metric(
        "Security Score",
        f"{firewall_score:.0f}%"
        )
        
        st.divider()

        # Pie Chart

        chart_data = pd.DataFrame(
            {
                "Severity": [
                    "Critical",
                    "High",
                    "Medium",
                    "Low"
                ],
                "Count": [
                    critical,
                    high,
                    medium,
                    low
                ]
            }
        )

        fig = px.pie(
            chart_data,
            values="Count",
            names="Severity",
            title="Risk Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.divider()

        # Executive Summary

        st.subheader("📋 Executive Summary")

        st.info(
            f"""
Firewall Health Score: {firewall_score:.0f}%

Rules Analyzed: {total_rules}

Critical Findings: {critical}

Overall Risk Level: {overall_risk}
"""
        )

        st.subheader("🚨 Top Security Findings")

        if critical > 0:
            st.error(
                f"Critical Findings Detected: {critical}"
            )

        if high > 0:
            st.warning(
                f"High Risk Findings Detected: {high}"
            )

        if medium > 0:
            st.info(
                f"Medium Risk Findings Detected: {medium}"
            )

        st.divider()

        st.subheader("Firewall Rules")

        st.dataframe(
            df,
            use_container_width=True
        )

    # =========================
    # RISK ANALYSIS PAGE
    # =========================

    elif page == "Risk Analysis":

        st.subheader("Risk Analysis")

        for _, row in df.iterrows():

            score, severity, reasons, recommendations = calculate_risk(row)

            if severity == "Critical":

                st.error(
                    f"Rule {row['RuleID']} | Score: {score} | Severity: {severity}"
                )

            elif severity == "High":

                st.warning(
                    f"Rule {row['RuleID']} | Score: {score} | Severity: {severity}"
                )

            elif severity == "Medium":

                st.info(
                    f"Rule {row['RuleID']} | Score: {score} | Severity: {severity}"
                )

            else:

                st.success(
                    f"Rule {row['RuleID']} | Score: {score} | Severity: {severity}"
                )

            st.write("**Reasons:**")

            if reasons:

                for reason in reasons:
                    st.write(f"• {reason}")

            else:
                st.write("• No issues detected")

            st.write("**Recommendations:**")

            if recommendations:

                for rec in recommendations:
                    st.write(f"✅ {rec}")

            else:
                st.write("✅ No action required")

            st.divider()

    # =========================
    # REPORTS PAGE
    # =========================

    elif page == "Reports":

     st.subheader("📄 Reports")

     st.write(
        "Generate a professional firewall audit report."
    )

    if st.button("Generate Audit Report"):

        generate_report(
            "Firewall_Audit_Report.pdf",
            firewall_score,
            critical,
            high,
            medium,
            low
        )

        with open(
            "Firewall_Audit_Report.pdf",
            "rb"
        ) as pdf_file:

            st.download_button(
                label="⬇ Download PDF Report",
                data=pdf_file,
                file_name="Firewall_Audit_Report.pdf",
                mime="application/pdf"
            )

        st.success(
            "Firewall_Audit_Report.pdf generated successfully!"
        )
    
else:

    st.info(
        "Upload a firewall rules CSV file to begin analysis."
    )

st.markdown("---")

st.caption(
    "Developed by Mewada Kavya | Firewall Rule Analyzer Pro v1.0"
)
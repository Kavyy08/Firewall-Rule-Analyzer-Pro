from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    PageBreak,
    Table,
    TableStyle
)

from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime


def generate_report(
    filename,
    firewall_score,
    critical,
    high,
    medium,
    low
):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    content = []

    # ==========================
    # COVER PAGE
    # ==========================

    content.append(
        Paragraph(
            "🛡 FIREWALL RULE ANALYZER PRO",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 40))

    content.append(
        Paragraph(
            " Firewall Security Audit Report",
            styles["Heading1"]
        )
    )

    content.append(Spacer(1, 35))

    content.append(
        Paragraph(
            f"Generated Date: {datetime.now().strftime('%d-%m-%Y')}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Analyst: Mewada Kavya",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            "Version: 1.0",
            styles["BodyText"]
        )
    )

    content.append(PageBreak())

    # ==========================
    # EXECUTIVE SUMMARY
    # ==========================

    content.append(
        Paragraph(
            "Executive Summary",
            styles["Heading1"]
        )
    )

    if firewall_score >= 90:
        grade = "A"
    elif firewall_score >= 80:
        grade = "B"
    elif firewall_score >= 60:
        grade = "C"
    elif firewall_score >= 40:
        grade = "D"
    else:
        grade = "F"

    if critical > 0:
        risk = "HIGH"
    elif high > 0:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    summary = f"""
    Firewall Health Score: <b>{firewall_score:.0f}%</b><br/><br/>
    Security Grade: <b>{grade}</b><br/><br/>
    Overall Risk Level: <b>{risk}</b><br/><br/>
    Critical Findings: <b>{critical}</b><br/>
    High Findings: <b>{high}</b><br/>
    Medium Findings: <b>{medium}</b><br/>
    Low Findings: <b>{low}</b>
    """

    content.append(
        Paragraph(
            summary,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 25))

    # ==========================
    # RISK TABLE
    # ==========================

    content.append(
        Paragraph(
            "Risk Assessment Summary",
            styles["Heading1"]
        )
    )

    risk_table = Table(
        [
            ["Severity", "Count"],
            ["Critical", str(critical)],
            ["High", str(high)],
            ["Medium", str(medium)],
            ["Low", str(low)]
        ],
        colWidths=[200, 120]
    )

    risk_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), colors.darkblue),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ("BACKGROUND", (0, 1), (-1, 1), colors.red),
            ("TEXTCOLOR", (0, 1), (-1, 1), colors.white),
            ("BACKGROUND", (0, 2), (-1, 2), colors.orange),
            ("BACKGROUND", (0, 3), (-1, 3), colors.yellow),
            ("BACKGROUND", (0, 4), (-1, 4), colors.lightgreen),
            ("ALIGN", (0, 0), (-1, -1), "CENTER")
        ])
    )

    content.append(risk_table)

    content.append(PageBreak())

    # ==========================
    # RECOMMENDATIONS
    # ==========================

    content.append(
        Paragraph(
            "Security Recommendations",
            styles["Heading1"]
        )
    )

    recommendations = """
    • Restrict Any-to-Any firewall rules<br/><br/>
    • Replace Telnet with SSH<br/><br/>
    • Follow Least Privilege principles<br/><br/>
    • Review firewall rules quarterly<br/><br/>
    • Enable centralized logging and monitoring<br/><br/>
    • Remove unused and legacy services<br/><br/>
    • Maintain firewall change management process
    """

    content.append(
        Paragraph(
            recommendations,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 30))

    # ==========================
    # PROJECT INFO
    # ==========================

    content.append(
        Paragraph(
            "Project Information",
            styles["Heading1"]
        )
    )

    project_info = """
    Tool Name: Firewall Rule Analyzer Pro<br/><br/>

    Technology Stack:<br/>
    Python<br/>
    Streamlit<br/>
    Pandas<br/>
    Plotly<br/>
    ReportLab<br/><br/>

    Purpose:<br/>
    Automated Firewall Security Assessment and Risk Analysis
    """

    content.append(
        Paragraph(
            project_info,
            styles["BodyText"]
        )
    )

    content.append(Spacer(1, 40))

    # ==========================
    # FOOTER
    # ==========================

    content.append(
        Paragraph(
            "Generated by Firewall Rule Analyzer Pro",
            styles["Italic"]
        )
    )

    content.append(
        Paragraph(
            "Developed by Mewada Kavya",
            styles["Italic"]
        )
    )

    doc.build(content)
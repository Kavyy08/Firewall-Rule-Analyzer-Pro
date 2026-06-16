def calculate_risk(rule):

    score = 0
    reasons = []
    recommendations = []

    source = str(rule["Source"]).strip()
    destination = str(rule["Destination"]).strip()
    service = str(rule["Service"]).strip()

    # Source Any

    if source.lower() == "any":
        score += 30
        reasons.append("Source is Any")
        recommendations.append("Restrict source network")

    # Destination Any

    if destination.lower() == "any":
        score += 30
        reasons.append("Destination is Any")
        recommendations.append("Restrict destination network")

    # Service Any

    if service.lower() == "any":
        score += 35
        reasons.append("Service is Any")
        recommendations.append("Allow only required services")

    # Any -> Any Critical Rule

    if source.lower() == "any" and destination.lower() == "any":
        score += 20
        reasons.append("Any-to-Any rule detected")
        recommendations.append("Avoid broad Any-to-Any access")

    # Telnet

    if service.lower() == "telnet":
        score += 25
        reasons.append("Telnet detected")
        recommendations.append("Replace Telnet with SSH")

    # FTP

    if service.lower() == "ftp":
        score += 20
        reasons.append("FTP detected")
        recommendations.append("Use SFTP or FTPS instead")

    # RDP

    if service.lower() == "rdp":
        score += 25
        reasons.append("RDP exposed")
        recommendations.append("Restrict RDP access to trusted IPs")

    # SMB

    if service.lower() == "smb":
        score += 25
        reasons.append("SMB exposed")
        recommendations.append("Restrict SMB to internal networks")

    # HTTP

    if service.lower() == "http":
        score += 10
        reasons.append("Unencrypted HTTP detected")
        recommendations.append("Use HTTPS instead of HTTP")

    # Cap score

    if score > 100:
        score = 100

    # Severity

    if score >= 80:
        severity = "Critical"

    elif score >= 50:
        severity = "High"

    elif score >= 20:
        severity = "Medium"

    else:
        severity = "Low"

    # No findings

    if len(reasons) == 0:
        reasons.append("No issues detected")
        recommendations.append("No action required")

    return score, severity, reasons, recommendations
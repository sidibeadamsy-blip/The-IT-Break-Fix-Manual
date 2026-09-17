import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def update_triage_manual():
    pdf_path = "The_IT_Break_Fix_Manual.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, title="The IT Break-Fix Manual")
    story = []
    
    primary_color = colors.HexColor("#1A252C")
    secondary_color = colors.HexColor("#2C3E50")
    bg_light = colors.HexColor("#ECF0F1")
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', parent=styles['Heading1'], fontName='Helvetica-Bold', fontSize=22, textColor=primary_color, spaceAfter=4)
    sub_style = ParagraphStyle('DocSub', parent=styles['Normal'], fontName='Helvetica-Oblique', fontSize=10, textColor=colors.HexColor("#7F8C8D"), spaceAfter=12)
    h1_style = ParagraphStyle('SectionH1', parent=styles['Heading2'], fontName='Helvetica-Bold', fontSize=14, textColor=secondary_color, spaceBefore=14, spaceAfter=6)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=10, textColor=colors.HexColor("#2C3E50"), leading=14, spaceAfter=8)
    code_style = ParagraphStyle('CodeBox', parent=styles['Code'], fontName='Courier', fontSize=9, textColor=colors.HexColor("#F8F9FA"), backColor=colors.HexColor("#2C3E50"), borderPadding=6, spaceBefore=4, spaceAfter=6)
    
    story.append(Paragraph("🛠️ THE IT BREAK-FIX MANUAL: LIVE OPERATIONS LOG", title_style))
    story.append(Paragraph("<b>Lead Tier-2 Systems Specialist:</b> Abdoulaye Sidibe | <b>Portfolio:</b> ://substack.com", body_style))
    story.append(Paragraph("<i>A comprehensive operational log detailing real-world root-cause analysis, hardware failure isolation, and system recovery procedures.</i>", sub_style))
    story.append(Spacer(1, 6))
    
    story.append(Paragraph("📋 INCIDENT TRIAGE ARCHIVE MATRIX", h1_style))
    triage_data = [
        [Paragraph("<b>Incident Code</b>", body_style), Paragraph("<b>Target Subsystem</b>", body_style), Paragraph("<b>Root Cause &amp; Resolution Metric</b>", body_style)],
        [Paragraph("INC-001 (Resolved)", body_style), Paragraph("Network Layer<br/>(Linux/Windows DHCP)", body_style), Paragraph("Simulated adapter outages. Applied physical layer check logic. Restored connectivity parameters natively via administrative lease terminations and renewals (<code>ipconfig /release</code> and <code>/renew</code>).", body_style)],
        [Paragraph("INC-002 (Resolved)", body_style), Paragraph("Identity Management<br/>(Active Directory)", body_style), Paragraph("Resolved user account brute-force protection lockout failures. Used targeted command line parameters (<code>net user [username] /active:yes /unlock</code>) to break security blocks without modifying credential configurations.", body_style)],
        [Paragraph("INC-003 (Resolved)", body_style), Paragraph("Storage &amp; File Systems<br/>(Disk Subsystem)", body_style), Paragraph("Audited logical partitioning tracks and hard volume boundaries using <code>diskpart</code>. Deployed deep structural file system repair scans via volume parameters (<code>chkdsk C: /f /r</code>).", body_style)],
        [Paragraph("INC-004 (Resolved)", body_style), Paragraph("Operating System<br/>(Bare-Metal Deployment)", body_style), Paragraph("Diagnosed critical system image file corruption. Flashed a verified Windows 11 Pro ISO onto storage using Rufus. Executed complete destructive drive re-partitioning and clean OS deployment.", body_style)],
        [Paragraph("INC-005 (Resolved)", body_style), Paragraph("Peripherals / Print Stack<br/>(Logical Spooler Lock)", body_style), Paragraph("Remediated local print job freeze blocks. Executed administrative service terminations (<code>net stop spooler</code>), purged corrupted spool data directories via system root controls, and re-initialized the print queue engine successfully.", body_style)]
    ]
    
    # Explicit pixel column dimensions to force a perfect fit layout
    t1 = Table(triage_data, colWidths=[110, 130, 300])
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), bg_light),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#BDC3C7")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    
    story.append(Paragraph("💻 MASTER TECHNICAL REMEDIATION COMMANDS LOGGED:", h1_style))
    story.append(Paragraph("ipconfig /release && ipconfig /renew", code_style))
    story.append(Paragraph("net user [username] /active:yes /unlock", code_style))
    story.append(Paragraph("diskpart -> list disk -> list volume -> chkdsk C: /f /r", code_style))
    story.append(Paragraph("Rufus -> Windows 11 Pro ISO Bare-Metal Flashing &amp; Deployment", code_style))
    story.append(Paragraph("net stop spooler -> del /Q /F /S spool\\PRINTERS\\* -> net start spooler", code_style))
    
    doc.build(story)

if __name__ == "__main__":
    update_triage_manual()

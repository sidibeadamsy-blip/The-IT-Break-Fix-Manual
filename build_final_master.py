import os
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

def generate_master_manual():
    pdf_path = "The_Unified_IT_Break_Fix_Manual.pdf"
    doc = SimpleDocTemplate(pdf_path, pagesize=letter, leftMargin=36, rightMargin=36, topMargin=36, bottomMargin=36)
    story = []
    
    primary_color = colors.HexColor("#1E293B")
    secondary_color = colors.HexColor("#475569")
    bg_table_header = colors.HexColor("#E2E8F0")
    code_bg = colors.HexColor("#F1F5F9")
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('DocTitle', fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=primary_color, spaceAfter=6)
    sub_style = ParagraphStyle('DocSub', fontName='Helvetica-Oblique', fontSize=10, leading=14, textColor=secondary_color, spaceAfter=14)
    h1_style = ParagraphStyle('SectionH1', fontName='Helvetica-Bold', fontSize=13, leading=17, textColor=primary_color, spaceBefore=14, spaceAfter=6)
    body_style = ParagraphStyle('BodyDark', fontName='Helvetica', fontSize=9.5, leading=13, textColor=primary_color)
    header_text_style = ParagraphStyle('HeaderText', fontName='Helvetica-Bold', fontSize=9.5, leading=13, textColor=primary_color)
    code_style = ParagraphStyle('CodeBox', fontName='Courier', fontSize=8.5, leading=12, textColor=primary_color, backColor=code_bg, borderPadding=6, spaceBefore=4, spaceAfter=4)
    
    story.append(Paragraph("THE IT BREAK-FIX MANUAL: MASTER OPERATIONS LOG", title_style))
    story.append(Paragraph("<b>Lead Systems Specialist:</b> Nosstra Damis | <b>Portfolio:</b> ://substack.com", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("A comprehensive enterprise archive documenting end-to-end root-cause analysis, system recovery, and perimeter firewall remediation across virtual laboratory network interfaces.", sub_style))
    
    story.append(Paragraph("MASTER INCIDENT TRIAGE MATRIX", h1_style))
    
    # 0.5" column 1, 1.25" column 2, 5.75" column 3
    fixed_widths = [36, 90, 414]
    
    data = [
        [Paragraph("<b>Code</b>", header_text_style), Paragraph("<b>Subsystem</b>", header_text_style), Paragraph("<b>Unified Triage &amp; Multi-Path Remediation Methodology</b>", header_text_style)],
        [Paragraph("INC-001", body_style), Paragraph("Network Layer<br/>(DHCP Outage)", body_style), Paragraph("<b>CLI Path:</b> Executed <code>ipconfig /release</code> and <code>/renew</code> to flush corrupted temporary software configuration layers.<br/><b>GUI Path:</b> Toggled 'Cable Connected' options inside VirtualBox network properties to reset physical links cleanly.", body_style)],
        [Paragraph("INC-004", body_style), Paragraph("Security Ops<br/>(Scareware Script)", body_style), Paragraph("<b>Root Cause:</b> Isolated a malicious browser full-screen script generating fake antivirus alerts to induce unauthorized telemetry downloads.<br/><b>Remediation:</b> Enforced strict network layer isolation by physically decoupling the Cat6 Ethernet link. Executed process termination via <code>taskkill /f /im chrome.exe</code>.", body_style)],
        [Paragraph("INC-005", body_style), Paragraph("SecOps / Triage<br/>(Persistence)", body_style), Paragraph("<b>Root Cause:</b> Identified a hidden startup loop disguised as <code>updater.exe</code> in <code>AppData\Local\PulseSoftware</code> forcing full-screen kiosk popups.<br/><b>Remediation:</b> Disabled the startup entry via Task Manager, terminated active process memory rails via CLI, and shift-deleted the execution binary directories.", body_style)],
        [Paragraph("INC-006", body_style), Paragraph("Perimeter Security<br/>(Host Firewall CLI)", body_style), Paragraph("<b>Objective:</b> Fortified Windows Server 2022 perimeter defenses against malicious network scanning and ransomware lateral movement vectors.<br/><b>Remediation:</b> Imported network security dependencies via <code>Import-Module NetSecurity</code>. Deployed an inbound port rule targeting TCP Port 445 (SMB) using <code>New-NetFirewallRule</code> to completely drop ransomware traffic paths. Implemented a host containment rule to block a malicious attacker IP address (192.168.1.99) from communicating with the server.", body_style)]
    ]
    
    t1 = Table(data, colWidths=fixed_widths)
    t1.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), bg_table_header),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E1")),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t1)
    
    story.append(Paragraph("💻 MASTER SECURE REGISTRY REMEDIATION COMMANDS LOG:", h1_style))
    story.append(Paragraph("<b>[Host Firewall Port Lockdown]</b> New-NetFirewallRule -DisplayName 'LAB_Block_SMB_Malware' -Direction Inbound -LocalPort 445 -Protocol TCP -Action Block", code_style))
    story.append(Paragraph("<b>[Host Firewall Host Containment]</b> New-NetFirewallRule -DisplayName 'LAB_Block_Rogue_Attacker' -Direction Inbound -RemoteAddress '192.168.1.99' -Action Block", code_style))
    story.append(Paragraph("<b>[Host Firewall Verification Pass]</b> Get-NetFirewallRule -DisplayName 'LAB_Block_SMB_Malware' | Select-Object Name, Action, Enabled", code_style))
    
    doc.build(story)

if __name__ == "__main__":
    generate_master_manual()

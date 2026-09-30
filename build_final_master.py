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
    story.append(Paragraph("<b>Lead Systems Specialist:</b> Abdoulaye Sidibe | <b>Portfolio:</b> ://substack.com", body_style))
    story.append(Spacer(1, 4))
    story.append(Paragraph("A comprehensive enterprise archive documenting end-to-end root-cause analysis, system recovery, and infrastructure triage mapped across both Command-Line Interfaces (CLI) and Graphical User Interfaces (GUI).", sub_style))
    
    story.append(Paragraph("MASTER INCIDENT TRIAGE MATRIX", h1_style))
    
    # Safe explicit array widths to prevent formatting glitches
    fixed_widths = [60, 110, 370]
    
    data = [
        [Paragraph("<b>Code</b>", header_text_style), Paragraph("<b>Subsystem</b>", header_text_style), Paragraph("<b>Unified Triage &amp; Multi-Path Remediation Methodology</b>", header_text_style)],
        [Paragraph("INC-001", body_style), Paragraph("Network Layer<br/>(DHCP Outage)", body_style), Paragraph("<b>CLI Path:</b> Executed <code>ipconfig /release</code> and <code>/renew</code> (Windows) to flush corrupted temporary software configuration layers.<br/><b>GUI Path:</b> Access VirtualBox <code>Devices -> Network -> Network Settings</code> to toggle 'Cable Connected' state to isolate hardware boundary links.", body_style)],
        [Paragraph("INC-002", body_style), Paragraph("Identity/Access<br/>(AD / RBAC)", body_style), Paragraph("<b>CLI Path:</b> Provisioned secure domain containers via PowerShell using <code>New-ADGroup</code> and complex user profiles via <code>New-ADUser</code> with complexity rules, linking identity loops cleanly via <code>Add-ADGroupMember</code> parameters.<br/><b>GUI Path:</b> Expand <code>nosstradamis.local</code> tree ➡️ Expand <code>Users</code> container ➡️ Right-click target security group ➡️ Select <code>Properties</code> ➡️ Open <code>Members</code> tab ➡️ Click <code>Add</code> to bridge accounts visually (Bill Fof &amp; N'dia Malick).", body_style)],
        [Paragraph("INC-003", body_style), Paragraph("Storage &amp; Volume<br/>(Disk Partition)", body_style), Paragraph("<b>CLI Path:</b> Launched low-level partitioning tracks via <code>diskpart -> list volume</code>, executing structural file system validation and recovery sequences using <code>chkdsk C: /f /r</code>.<br/><b>GUI Path:</b> Managed volumes via <code>Disk Management (diskmgmt.msc)</code> to format raw space visually.", body_style)],
        [Paragraph("INC-004", body_style), Paragraph("Operating System<br/>(Bare-Metal OS)", body_style), Paragraph("<b>Remediation:</b> Resolved critical environment image file corruption. Deployed external installation infrastructure using Rufus to flash a verified Windows 11 Pro ISO onto storage. Executed complete destructive drive re-partitioning and clean OS deployment.", body_style)],
        [Paragraph("INC-005", body_style), Paragraph("Peripherals<br/>(Print Queue)", body_style), Paragraph("<b>CLI Path:</b> Forced print queue terminations via <code>net stop spooler</code>, manually purging the corrupted spool data cache via root delete commands, and restarting the engine via <code>net start spooler</code>.<br/><b>GUI Path:</b> Navigated via <code>Services.msc -> Print Spooler -> Restart</code> to clear data blocks.", body_style)],
        [Paragraph("INC-006", body_style), Paragraph("Name Resolution<br/>(DNS Transport)", body_style), Paragraph("<b>CLI Path:</b> Cleared domain translation bottlenecks using <code>ipconfig /flushdns</code>, verifying name resolution routing paths using <code>nslookup</code> queries.<br/><b>GUI Path:</b> Navigated via <code>Network and Sharing Center -> Change Adapter Settings -> IPv4 Properties</code>.", body_style)]
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
    
    story.append(Paragraph("💻 KEY TECHNICAL REMEDIATION STRINGS:", h1_style))
    story.append(Paragraph("<b>[DHCP Triage]</b> ipconfig /release && ipconfig /renew", code_style))
    story.append(Paragraph("<b>[AD Group Deployment]</b> New-ADGroup -Name 'Finance_Dept_SG' -GroupScope Global -GroupCategory Security", code_style))
    story.append(Paragraph("<b>[AD User Complexity Provisioning]</b> New-ADUser -Name 'Bill Fof' -SamAccountName 'bfof' -AccountPassword $SecurePassword -Enabled $true", code_style))
    story.append(Paragraph("<b>[AD Member Nesting]</b> Add-ADGroupMember -Identity 'Finance_Dept_SG' -Members 'bfof', 'nmalick'", code_style))
    story.append(Paragraph("<b>[Printer Spooler Purge]</b> net stop spooler -> del /Q /F /S spool\\PRINTERS\\* -> net start spooler", code_style))
    story.append(Paragraph("<b>[DNS Flush]</b> ipconfig /flushdns -> nslookup [domain]", code_style))
    
    doc.build(story)

if __name__ == "__main__":
    generate_master_manual()

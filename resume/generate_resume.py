#!/usr/bin/env python3
"""
Generate EstebanMorenoResume.pdf  →  ../images/EstebanMorenoResume.pdf
        EstebanMorenoResume.docx  →  ./EstebanMorenoResume.docx

Usage:  python3 resume/generate_resume.py
"""

import os, sys
from pathlib import Path

RESUME_DIR = Path(__file__).parent
PDF_OUT    = RESUME_DIR.parent / "images" / "EstebanMorenoResume.pdf"
DOCX_OUT   = RESUME_DIR / "EstebanMorenoResume.docx"

# ── Content ────────────────────────────────────────────────────────────────────

NAME    = "Esteban Moreno"
TITLE   = "DevOps Team Lead"

CONTACT_LINE_1 = "morenoramirezesteban@gmail.com  |  linkedin.com/in/estebanmorenoramirez  |  github.com/estebanmorenoit"
CONTACT_LINE_2 = "blog.estebanmoreno.link  |  estebanmoreno.link  |  London, UK"

PROFILE = (
    "DevOps Team Lead at X-Tention, responsible for the architecture and technical planning of the "
    "Kubernetes platform behind MACH, a healthcare integration platform, on AWS EKS and "
    "on-premises in customer environments. "
    "Specialising in Kubernetes platform engineering, GitOps delivery with Argo CD, Terraform "
    "infrastructure as code and production observability. Came up through IT support and network "
    "infrastructure at Amazon and chapmanbdsp. Published 108 technical posts on AWS and DevOps, "
    "including a 90-day DevOps series."
)

# Skills: (category, value) — rendered as "Category: value" inline
SKILLS = [
    ("Cloud",                  "AWS \u2014 EKS, Lambda, EC2, S3, DynamoDB, CloudFront, CloudWatch, IAM, VPC, Route\u00a053"),
    ("Infrastructure as Code", "Terraform, Terraform Cloud, HCL; Ansible (lab experience)"),
    ("Containers & Kubernetes","Kubernetes (EKS, K3s, MicroK8s), Docker, Docker Compose, Helm, Argo CD, Harbor, Traefik, CloudNativePG, Tanzu, Zarf"),
    ("CI/CD",                  "GitLab CI/CD, GitHub Actions, Argo CD (GitOps); Jenkins (lab experience)"),
    ("Observability",          "Prometheus, Grafana, Thanos, Loki, Tempo, Alloy, Promtail, Fluent Bit, Alertmanager, OpenTelemetry, OpenSearch"),
    ("Security & Identity",    "Keycloak (OIDC/SSO), External Secrets Operator, cert-manager, AWS IAM"),
    ("OS & Scripting",         "Linux (RHEL, Ubuntu, Debian), Bash, Python"),
]

# (name, issuer, dates)
CERTS = [
    ("AWS Certified Solutions Architect \u2013 Associate", "Amazon Web Services", "2023\u20132026"),
    ("HashiCorp Certified: Terraform Associate (003)",     "HashiCorp",           "2023\u20132025"),
    ("Linux Professional Institute Linux Essentials",      "LPI",                 "2023"),
    ("Network Technician Career Path",                     "Cisco",               "2023"),
    ("Junior Cybersecurity Analyst Career Path",           "Cisco",               "2023"),
    ("Terraform Beginner Bootcamp (Terraformer)",          "ExamPro",             "2023"),
]

# (job title, "Company  ·  Location  ·  Dates", bullets)
EXPERIENCE = [
    ("DevOps Team Lead", "X-Tention  \u00b7  UK, remote  \u00b7  Apr 2026 \u2013 Present", [
        "Responsible for the architecture and technical planning of the Kubernetes platform behind "
        "MACH, X-Tention's healthcare integration platform, on AWS EKS and on-premises.",
        "Own GitOps delivery with Argo CD, Helm and GitLab CI/CD, including EKS and Argo CD "
        "major-version upgrades.",
        "Deliver on-premises installations of MACH Orchestra into customer environments, covering "
        "certificate trust, registry access and installer reliability.",
        "Set the technical direction for observability across both platforms, including Thanos "
        "design decisions, and lead production incident response.",
        "Migrated the platform from MicroK8s to K3s and from the Zalando Postgres operator to "
        "CloudNativePG; now leading the move from NGINX to Traefik ingress.",
        "Integrate Harbor with Keycloak OIDC and manage AWS infrastructure through Terraform.",
        "Harden workloads to run as non-root under restricted security profiles.",
    ]),
    ("Senior DevOps Engineer", "X-Tention  \u00b7  UK, remote  \u00b7  Feb 2024 \u2013 Apr 2026", [
        "Managed production EKS clusters with Helm and Argo CD for GitOps-driven, declarative "
        "deployments across multiple environments.",
        "Built and maintained GitLab CI/CD pipelines with the team, shaped to each project's "
        "requirements: building Docker images, running tests, packaging Helm charts, publishing "
        "to Harbor and deploying through Argo CD.",
        "Managed the MACH observability platform: Prometheus and Alertmanager for metrics and "
        "alerting, OpenSearch with Fluent Bit for logs, and Grafana for dashboards.",
        "Helped deploy Thanos for long-term metrics storage, then ran it on my own.",
        "Set up the Grafana observability stack for a second X-Tention product: Loki for logs, "
        "Tempo for traces, and Alloy with OpenTelemetry for collection.",
        "Helped deploy and configure Keycloak as the identity provider for the MACH product and "
        "internal team tools, providing OIDC-based SSO, then ran its operations on my own.",
        "Wrote, extended and maintained the Terraform code for all of our AWS infrastructure, with "
        "state in S3, including application configuration (OpenSearch, Keycloak) and core EKS "
        "add-ons such as Argo CD and cert-manager.",
        "Worked daily on the MicroK8s and K3s platform behind our product's infrastructure "
        "tooling, together with Zarf for air-gapped packaging, making improvements and changes "
        "as needed.",
        "Ran proofs of concept on a VMware Tanzu Kubernetes cluster, doing most of the work myself.",
    ]),
    ("IT Support Engineer", "Amazon  \u00b7  London  \u00b7  Mar 2022 \u2013 Feb 2024", [
        "Provided IT support for Amazon's London offices, including the UK headquarters, and was "
        "responsible for building infrastructure and uptime.",
        "Supported the rollout of Amazon's global migration from commodity switches to Cisco "
        "across the London sites.",
        "Set up network connectivity for new areas in the AWS offices: switches, access points, "
        "firewall updates and new line installations.",
        "Acted as the main contact between building infrastructure and the AWS support team.",
        "Trained new hires on AWS, Linux and the processes and company requirements of the role.",
    ]),
    ("Senior IT Support Engineer", "chapmanbdsp  \u00b7  London  \u00b7  Jan 2019 \u2013 Mar 2022", [
        "Managed the international helpdesk team across 6 sites in the UK and UAE.",
        "Led the move of the whole workforce to remote working, rolling out VPN, VoIP and Ivanti.",
        "Led the standards and policy work behind Cyber Essentials Plus certification.",
    ]),
    ("1st Line IT Support Engineer", "chapmanbdsp  \u00b7  London  \u00b7  Mar 2018 \u2013 Jan 2019", []),
    ("IT Support Engineer", "Fluid Design Ltd  \u00b7  Aug 2017 \u2013 Mar 2018", [
        "Provided 1st and 2nd line IT support, resolving hardware, software, and network incidents "
        "across a design consultancy environment.",
        "Maintained workstations, managed user accounts, and supported day-to-day IT operations.",
    ]),
]

EDUCATION = [
    (
        "BEng Telecommunications Engineering",
        "Miguel Hern\u00e1ndez University, Alicante, Spain",
        "2010 \u2013 2016",
        "Final project: Design, simulation and measurement of Voltage Controlled Oscillators on "
        "ISM Band \u2014 graded 9.5/10. Modules included Computer Networks, Analog & Digital "
        "Electronics, Programming Fundamentals, and Engineering Electromagnetics.",
    ),
]

PROJECTS = [
    (
        "DevOps Learning Lab",
        "K3s  |  Argo CD  |  Prometheus  |  Grafana  |  External Secrets Operator  |  Python  |  Docker",
        "Self-hosted, interactive DevOps course across 14 topics, from Linux to GitOps, security and "
        "observability. Each lesson pairs theory with an in-browser terminal connected to a real K3s "
        "cluster running in Docker, pre-loaded with Argo CD, Prometheus, Grafana and External Secrets Operator.",
        "github.com/estebanmorenoit/devops-learning-lab",
    ),
    (
        "Production-Grade Self-Hosted Home Lab on Raspberry Pi",
        "Docker Compose  |  Prometheus  |  Grafana  |  Loki  |  Tailscale  |  GitHub Actions",
        "Full self-hosted infrastructure stack on a Raspberry Pi: Docker Compose services, "
        "monitored via Prometheus/Grafana/Loki/Uptime Kuma, Caddy as reverse proxy, Tailscale for "
        "secure remote access, and automated deployments via GitHub Actions.",
        "github.com/estebanmorenoit/rpi-home-lab",
    ),
    (
        "Cloud Resume Challenge \u2014 Serverless Portfolio on AWS",
        "AWS  |  Terraform  |  Lambda  |  DynamoDB  |  CloudFront  |  GitHub Actions",
        "Serverless portfolio site on AWS: Lambda + DynamoDB visitor counter, CloudFront CDN, S3 "
        "static hosting, Route 53, full Terraform IaC, and a GitHub Actions CI/CD pipeline. "
        "Documented across a 6-part blog series.",
        "github.com/estebanmorenoit/estebanmoreno-portfolio",
    ),
]

WRITING = (
    "Published 108 technical posts on Kubernetes, Terraform, AWS, CI/CD and observability at "
    "blog.estebanmoreno.link, including a 90-day DevOps series (#90DaysOfDevOps) and a "
    "Cloud Resume Challenge series."
)


# ══════════════════════════════════════════════════════════════════════════════
# PDF  (reportlab)
# ══════════════════════════════════════════════════════════════════════════════

def build_pdf():
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors
    from reportlab.lib.units import mm
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
    from reportlab.platypus import (
        SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
    )

    W, H = A4
    ACCENT  = colors.HexColor("#047857")
    DARK    = colors.HexColor("#111827")
    MID     = colors.HexColor("#374151")
    MUTED   = colors.HexColor("#6b7280")
    RULE    = colors.HexColor("#d1d5db")
    WHITE   = colors.white

    # ── Paragraph styles ──────────────────────────────────────────────────
    def ps(name, **kw):
        return ParagraphStyle(name, **kw)

    S_NAME     = ps("name",    fontName="Helvetica-Bold",    fontSize=24, textColor=DARK,   leading=28, spaceAfter=3)
    S_TITLE    = ps("title",   fontName="Helvetica",         fontSize=12, textColor=ACCENT, leading=16, spaceAfter=3)
    S_CONTACT  = ps("contact", fontName="Helvetica",         fontSize=8.5,textColor=MUTED,  leading=13, spaceAfter=2)
    S_SEC      = ps("sec",     fontName="Helvetica-Bold",    fontSize=9,  textColor=ACCENT, leading=12,
                               spaceBefore=10, spaceAfter=4,
                               textTransform="uppercase", letterSpacing=0.8)
    S_BODY     = ps("body",    fontName="Helvetica",         fontSize=9,  textColor=MID,    leading=14,
                               spaceAfter=4, alignment=TA_JUSTIFY)
    S_SKILL    = ps("skill",   fontName="Helvetica",         fontSize=8.5,textColor=MID,    leading=13, spaceAfter=3)
    S_JOB      = ps("job",     fontName="Helvetica-Bold",    fontSize=10, textColor=DARK,   leading=14,
                               spaceBefore=8, spaceAfter=1)
    S_META     = ps("meta",    fontName="Helvetica-Oblique", fontSize=8.5,textColor=MUTED,  leading=12, spaceAfter=4)
    # ── Hanging indent bullet — "• " is part of the text string ─────────
    S_BUL      = ps("bul",     fontName="Helvetica",         fontSize=8.5,textColor=MID,    leading=13,
                               leftIndent=10, firstLineIndent=-10,
                               spaceAfter=2)
    S_PROJ_T   = ps("projt",   fontName="Helvetica-Bold",    fontSize=9,  textColor=DARK,   leading=13,
                               spaceBefore=7, spaceAfter=1)
    S_PROJ_S   = ps("projs",   fontName="Helvetica-Oblique", fontSize=8,  textColor=ACCENT, leading=12, spaceAfter=2)
    S_PROJ_L   = ps("projl",   fontName="Helvetica",         fontSize=8,  textColor=MUTED,  leading=12, spaceAfter=2)
    S_CERT     = ps("cert",    fontName="Helvetica",         fontSize=8.5,textColor=MID,    leading=13, spaceAfter=2)

    def hr(color=RULE, thickness=0.6, before=2, after=4):
        return HRFlowable(width="100%", thickness=thickness, color=color,
                          spaceBefore=before, spaceAfter=after)

    def section(title):
        return [Paragraph(title, S_SEC), hr()]

    def bul(text):
        """Hanging-indent bullet — no XML <bullet> tag, so ATS parses cleanly."""
        return Paragraph("\u2022\u00a0" + text, S_BUL)

    # ── Document ──────────────────────────────────────────────────────────
    doc = SimpleDocTemplate(
        str(PDF_OUT),
        pagesize=A4,
        leftMargin=18*mm, rightMargin=18*mm,
        topMargin=16*mm,  bottomMargin=16*mm,
    )

    story = []

    # Header ──────────────────────────────────────────────────────────────
    story.append(Paragraph(NAME, S_NAME))
    story.append(Paragraph(TITLE, S_TITLE))
    story.append(hr(color=colors.HexColor("#047857"), thickness=1.5, before=0, after=5))
    story.append(Paragraph(CONTACT_LINE_1, S_CONTACT))
    story.append(Paragraph(CONTACT_LINE_2, S_CONTACT))
    story.append(Spacer(1, 6))

    # Professional Profile ────────────────────────────────────────────────
    story += section("Professional Profile")
    story.append(Paragraph(PROFILE, S_BODY))

    # Core Skills ─────────────────────────────────────────────────────────
    story += section("Core Skills")
    for label, value in SKILLS:
        story.append(Paragraph(
            f"<b>{label}:</b>\u00a0\u00a0{value}",
            S_SKILL
        ))

    # Certifications ──────────────────────────────────────────────────────
    story += section("Certifications")
    for cert_name, issuer, dates in CERTS:
        story.append(Paragraph(
            f"\u2022\u00a0<b>{cert_name}</b> \u2014 <i>{issuer}</i>, {dates}",
            S_BUL
        ))

    # Work Experience ─────────────────────────────────────────────────────
    story += section("Work Experience")

    # Keep each role's heading with its first bullets so it never orphans at a page break
    for job, meta, bullets in EXPERIENCE:
        story.append(KeepTogether([
            Paragraph(job, S_JOB),
            Paragraph(meta, S_META),
            *[bul(b) for b in bullets[:2]],
        ]))
        story += [bul(b) for b in bullets[2:]]

    # Education ───────────────────────────────────────────────────────────
    story += section("Education")
    for degree, institution, dates, detail in EDUCATION:
        story.append(KeepTogether([
            Paragraph(degree, S_JOB),
            Paragraph(f"{institution}  \u00b7  {dates}", S_META),
            Paragraph(detail, S_BODY),
        ]))

    # Selected Projects ───────────────────────────────────────────────────
    story += section("Selected Projects")
    for ptitle, pstack, pdesc, plink in PROJECTS:
        story.append(KeepTogether([
            Paragraph(ptitle, S_PROJ_T),
            Paragraph(pstack, S_PROJ_S),
            Paragraph(pdesc,  S_BODY),
            Paragraph(plink,  S_PROJ_L),
        ]))

    # Writing & Community ─────────────────────────────────────────────────
    story += section("Writing & Community")
    story.append(Paragraph(WRITING, S_BODY))

    doc.build(story)
    print(f"PDF  \u2192 {PDF_OUT}")


# ══════════════════════════════════════════════════════════════════════════════
# DOCX  (python-docx)
# ══════════════════════════════════════════════════════════════════════════════

def build_docx():
    from docx import Document
    from docx.shared import Pt, RGBColor, Cm
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml.ns import qn
    from docx.oxml import OxmlElement

    ACCENT_RGB = RGBColor(0x04, 0x78, 0x57)
    DARK_RGB   = RGBColor(0x11, 0x18, 0x27)
    MID_RGB    = RGBColor(0x37, 0x41, 0x51)
    MUTED_RGB  = RGBColor(0x6b, 0x72, 0x80)

    doc = Document()
    for sec in doc.sections:
        sec.left_margin   = Cm(1.8)
        sec.right_margin  = Cm(1.8)
        sec.top_margin    = Cm(1.6)
        sec.bottom_margin = Cm(1.6)

    def add_run(para, text, bold=False, italic=False, size=10, color=None, font_name="Arial"):
        run = para.add_run(text)
        run.bold = bold
        run.italic = italic
        run.font.size = Pt(size)
        run.font.name = font_name
        if color:
            run.font.color.rgb = color
        return run

    def para(space_before=0, space_after=2):
        p = doc.add_paragraph()
        pf = p.paragraph_format
        pf.space_before = Pt(space_before)
        pf.space_after  = Pt(space_after)
        return p

    def add_hr(p=None):
        if p is None:
            p = para(space_before=0, space_after=3)
        pBdr = OxmlElement("w:pBdr")
        bot = OxmlElement("w:bottom")
        bot.set(qn("w:val"),   "single")
        bot.set(qn("w:sz"),    "4")
        bot.set(qn("w:space"), "1")
        bot.set(qn("w:color"), "D1D5DB")
        pBdr.append(bot)
        p._p.get_or_add_pPr().append(pBdr)
        return p

    def section_heading(title):
        p = para(space_before=8, space_after=1)
        add_run(p, title.upper(), bold=True, size=9, color=ACCENT_RGB)
        add_hr()

    def bullet_item(text, size=8.5):
        p = doc.add_paragraph(style="List Bullet")
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after  = Pt(2)
        add_run(p, text, size=size, color=MID_RGB)

    # Header
    p = para(space_after=2)
    add_run(p, NAME, bold=True, size=22, color=DARK_RGB)

    p = para(space_after=2)
    add_run(p, TITLE, size=12, color=ACCENT_RGB)

    add_hr()

    p = para(space_after=1)
    add_run(p, CONTACT_LINE_1, size=8.5, color=MUTED_RGB)

    p = para(space_after=5)
    add_run(p, CONTACT_LINE_2, size=8.5, color=MUTED_RGB)

    # Profile
    section_heading("Professional Profile")
    p = para(space_after=4)
    add_run(p, PROFILE, size=9, color=MID_RGB)

    # Skills
    section_heading("Core Skills")
    for label, value in SKILLS:
        p = para(space_after=2)
        add_run(p, label + ":  ", bold=True, size=8.5, color=DARK_RGB)
        add_run(p, value, size=8.5, color=MID_RGB)

    # Certs
    section_heading("Certifications")
    for cert_name, issuer, dates in CERTS:
        bullet_item(f"{cert_name} \u2014 {issuer}, {dates}")

    # Experience
    section_heading("Work Experience")

    for i, (job, meta, bullets) in enumerate(EXPERIENCE):
        p = para(space_before=4 if i == 0 else 6, space_after=1)
        add_run(p, job, bold=True, size=10, color=DARK_RGB)

        p = para(space_after=3)
        add_run(p, meta, italic=True, size=8.5, color=MUTED_RGB)

        for b in bullets:
            bullet_item(b)

    # Education
    section_heading("Education")
    for degree, institution, dates, detail in EDUCATION:
        p = para(space_before=4, space_after=1)
        add_run(p, degree, bold=True, size=10, color=DARK_RGB)

        p = para(space_after=3)
        add_run(p, f"{institution}  \u00b7  {dates}", italic=True, size=8.5, color=MUTED_RGB)

        p = para(space_after=4)
        add_run(p, detail, size=8.5, color=MID_RGB)

    # Projects
    section_heading("Selected Projects")
    for ptitle, pstack, pdesc, plink in PROJECTS:
        p = para(space_before=4, space_after=1)
        add_run(p, ptitle, bold=True, size=9, color=DARK_RGB)

        p = para(space_after=1)
        add_run(p, pstack, italic=True, size=8, color=ACCENT_RGB)

        p = para(space_after=1)
        add_run(p, pdesc, size=8.5, color=MID_RGB)

        p = para(space_after=3)
        add_run(p, plink, size=8, color=MUTED_RGB)

    # Writing
    section_heading("Writing & Community")
    p = para(space_after=4)
    add_run(p, WRITING, size=9, color=MID_RGB)

    doc.save(str(DOCX_OUT))
    print(f"DOCX \u2192 {DOCX_OUT}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    RESUME_DIR.mkdir(parents=True, exist_ok=True)

    errors = []
    try:
        build_pdf()
    except Exception as e:
        errors.append(f"PDF: {e}")
        import traceback; traceback.print_exc()

    try:
        build_docx()
    except Exception as e:
        errors.append(f"DOCX: {e}")
        import traceback; traceback.print_exc()

    if errors:
        print("ERRORS:", errors); sys.exit(1)
    print("Done.")

# utils.py
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import tempfile


def generate_cv_pdf(data):
    # Create a temporary PDF file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp_file.name, pagesize=A4)

    width, height = A4
    x = 50
    y = height - 50

    # Name
    c.setFont("Helvetica-Bold", 18)
    c.drawString(x, y, data["name"])
    y -= 25

    # Contact
    c.setFont("Helvetica", 10)
    c.drawString(x, y, data["contact"])
    y -= 30

    def draw_section(title, items):
        nonlocal y
        if not items or items == [""]:
            return

        c.setFont("Helvetica-Bold", 12)
        c.drawString(x, y, title)
        y -= 15

        c.setFont("Helvetica", 10)
        for item in items:
            c.drawString(x + 10, y, f"- {item}")
            y -= 12

        y -= 10

    draw_section("EDUCATION", data["education"])
    draw_section("EXPERIENCE", data["experience"])
    draw_section("PROJECTS", data["projects"])
    draw_section("SKILLS", data["skills"])
    draw_section("CERTIFICATIONS", data["certificates"])

    c.save()
    return temp_file.name

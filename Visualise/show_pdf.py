from __future__ import annotations
from typing import List
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter


def show_pdf(data: List, file_name: str):
    """
    Show the report PDF
    """

    file_name = file_name + ".pdf"

    pdf = SimpleDocTemplate(
        file_name,
        pagesize=letter,
        leftMargin=0,
        rightMargin=0,
        topMargin=5
    )

    pdf.build(data)





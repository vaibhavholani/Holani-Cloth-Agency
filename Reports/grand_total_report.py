from __future__ import annotations
from typing import List, Tuple
from Visualise import create_pdf
from Database import retrieve_register_entry, retrieve_indivijual
from Visualise import show_pdf


def grand_total_report(party_ids: List[int], supplier_ids: List[int], start_date: str, end_date: str) -> List:

    """
    Return a 2D list of all pdf elements for grand total Report
    """

    table_header = ("Party Name", "Total Work", "Total GR")

    hr_line = create_pdf.create_horizontal_line()

    master_elements = [create_pdf.create_h1("Grand Total"), hr_line]

    table_data = [table_header]

    for party_id in party_ids:
        party_name = retrieve_indivijual.get_party_name_by_id(party_id)
        total_work = 0
        total_gr = 0
        for supplier_id in supplier_ids:
            grand_total_work = retrieve_register_entry.grand_total_work(party_id, supplier_id, start_date, end_date)
            grand_total_gr = retrieve_register_entry.grand_total_gr(party_id, supplier_id, start_date, end_date)
            total_work += int(grand_total_work)
            total_gr += int(grand_total_gr)
        table_data.append((party_name, total_work, total_gr))

    table_data.append(total_bottom_column(table_data))
    table = create_pdf.create_table(table_data)
    create_pdf.add_table_border(table)
    create_pdf.add_alt_color(table, len(table_data))
    create_pdf.add_padded_header_footer_columns(table, len(table_data))
    create_pdf.add_table_font(table, "Courier")
    master_elements.append(table)
    return master_elements


def total_bottom_column(data: List) -> List[Tuple]:
    """
    Add up all the values
    """
    total_sum = 0
    pending_sum = 0
    partial_sum = 0
    gr_sum = 0

    for elements in data:
        total_sum += int(elements[2])
        partial_sum += int(elements[3])
        gr_sum += int(elements[4])
        pending_sum += int(elements[5])

    return [("Total", "", total_sum, partial_sum, gr_sum, pending_sum)]


def execute(party_ids: List[int], supplier_ids: List[int], start_date: str, end_date: str):
    """
    Show the Report
    """
    data = grand_total_report(party_ids, supplier_ids, start_date, end_date)
    show_pdf.show_pdf(data, "grand_total_report")


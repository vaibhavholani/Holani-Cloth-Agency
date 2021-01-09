from __future__ import annotations
from typing import List, Tuple
from Visualise import create_pdf
from Database import retrieve_register_entry, retrieve_indivijual
from Visualise import show_pdf


def payment_list_summary(party_ids: List[int], supplier_ids: List[int], start_date: str, end_date: str) -> List:

    """
    Return a 2D list of all pdf elements for payment list Report
    """

    table_header = ("Supplier Name", "Total Amount", "Total Paid Amount", "Total Pending Amount")

    hr_line = create_pdf.create_horizontal_line()

    master_elements = [create_pdf.create_h1("Payment List Summary"), hr_line]

    for party_id in party_ids:
        elements = []
        party_name = retrieve_indivijual.get_party_name_by_id(party_id)
        h2text = "Party Name: " + party_name
        elements.append(create_pdf.create_h2(h2text))
        elements.append(hr_line)
        table_data = [table_header]
        for supplier_id in supplier_ids:
            add_table = True
            pl_summary_data = retrieve_register_entry.get_payment_list_summary_data(party_id, supplier_id, start_date, end_date)
            if len(pl_summary_data) == 0:
                add_table = False
            if add_table:
                supplier_name = retrieve_indivijual.get_supplier_name_by_id(supplier_id)
                pl_summary_insert = [(" ",) + x for x in pl_summary_data]
                temp = pl_summary_insert[0]
                pl_summary_insert[0] = (supplier_name, temp[1], temp[2], temp[3])
                table_data = table_data + pl_summary_insert
        table = create_pdf.create_table(table_data)
        create_pdf.add_table_border(table)
        create_pdf.add_alt_color(table, len(table_data))
        create_pdf.add_padded_header_footer_columns(table, len(table_data))
        # create_pdf.add_status_colour(table, table_data, 7)
        create_pdf.add_days_colour(table, table_data)
        create_pdf.add_table_font(table, "Courier")
        elements.append(table)
        master_elements = master_elements + elements
        master_elements.append(create_pdf.new_page())

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
    data = payment_list_summary(party_ids, supplier_ids, start_date, end_date)
    show_pdf.show_pdf(data, "payment_list_summary")


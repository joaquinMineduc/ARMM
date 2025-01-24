from Backend.inserts_to_excel.ins_cover_report import ins_data_to_report
from Backend.inserts_to_excel.ins_panel import insert_data_panel
from Backend.inserts_to_excel.ins_status_NC import insert_status_NC
from Backend.inserts_to_excel.ins_status_reg import insert_data_reg
from Backend.inserts_to_excel.ins_eval_internal import insert_data_prov
from Backend.inserts_to_excel.ins_adp import insert_data_adp
from Backend.inserts_to_excel.ins_risk import insert_data_risk
from Backend.inserts_to_excel.ins_programs import insert_data_programs
from Backend.inserts_to_excel.ins_anexo import insert_data_anexo


# Intentar mejorar con multihilo para optimizar performance
def call_all_inserts():
    ins_data_to_report()
    insert_data_panel()
    insert_status_NC()
    insert_data_reg()
    insert_data_prov()
    insert_data_adp()
    insert_data_risk()
    insert_data_programs()
    insert_data_anexo()
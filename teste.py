#from src.controller.cora.cora_api import CoraInvoicesManager

#response =  CoraInvoicesManager().check_invoice_status('inv_GpW5PHX4T1atZ99EvRvj99cw')
#print(response)

#from src.controller.routines.routine_update_repayment import UpdateNewPaymentRepayment
#from src.service.tokio.service_settings_headers_tmj import ServiceSettingsHeaders

#UpdateNewPaymentRepayment(ServiceSettingsHeaders.settings()).update()

#from src.controller.inter.inter_api import InterInvoicesManager
#from src.model.inter.entity_extract import DataExtract
#from src.utilities.utility import Utility

#response = InterInvoicesManager().get_extract(data= DataExtract(
#    START_DATE = Utility.convert_string_to_date_american('2024-11-06'),
#    END_DATE = Utility.convert_string_to_date_american('2024-11-07')
#))
#print(response)

'''from src.controller.routines.routine_update_invoice_status import PaymentUpdateRoutine
PaymentUpdateRoutine().update()'''

from src.controller.routines.routine_update_invoice_status_inter import PaymentUpdateInterRoutine
PaymentUpdateInterRoutine().update()

#from src.controller.routines.routine_get_extract_inter import GetExtractInterRoutine
#GetExtractInterRoutine().get()

#from src.utilities.utility import  Utility

#ipca = Utility().valor_ipca()
#print(ipca)

#from src.controller.routines.routine_update_agreement_delayed_cora import UpdateAgreementDelayedCoraRoutine
#UpdateAgreementDelayedCoraRoutine().delayed()

#from src.controller.itau.itau_api import ItauInvoicesManager
#from src.model.invoice.entity_invoice import DataCreateInvoiceInter

#data = DataCreateInvoiceInter(
#    ID_INSTALLMENT="94325ee1-c824-4da3-b6cb-f3ce6f033345"
#)

#ItauInvoicesManager().create_invoice(data)

#from src.controller.routines.routine_update_agreement_delayed import UpdateAgreementDelayedRoutine
#UpdateAgreementDelayedRoutine().delayed()
#from requests import Session
#from src.controller.routines.routine_tabulations import TabulationsTk
#TabulationsTk(Session()).manager()

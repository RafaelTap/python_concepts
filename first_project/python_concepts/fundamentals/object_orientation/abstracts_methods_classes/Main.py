from CommonAccount import CommonAccount
from VipAccount import VipAccount

ca_1 = CommonAccount(4455, 0.8, 0.7, 3000, 0.5)

vc_1 = VipAccount(5544, 0.8, 0.6, 3000, 1)

ca_1.performance_calculation()
vc_1.performance_calculation()

ca_1.extract()
vc_1.extract()
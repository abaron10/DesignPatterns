
from AuditTrail import  AuditTrail
class GenerateReportTask():
    def __init__(self, auditTrail):
        self.__auditTrail = auditTrail

    def _execute(self):
        self.__auditTrail.record()

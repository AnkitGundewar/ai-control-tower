from sns_client import SNSClient


class NotificationService:

    def __init__(self):

        self.sns = SNSClient()

    def send(self, event: dict):

        shipment = event["shipmentId"]
        response = event["response"]

        risk = response["risk"]["riskAnalysis"]
        recommendation = response["recommendation"]["recommendation"]
        summary = response["executiveSummary"]["executiveSummary"]

        message = f"""
        AI CONTROL TOWER ALERT

        Shipment
        --------
        {shipment}

        Priority
        --------
        {summary['priority']}

        Risk Level
        ----------
        {risk['riskLevel']}

        Recommendation
        --------------
        {recommendation['recommendations'][0]}

        Executive Summary
        -----------------
        {summary['summary']}
        """

        self.sns.publish(
            subject=f"Shipment Alert - {shipment}",
            message=message,
        )
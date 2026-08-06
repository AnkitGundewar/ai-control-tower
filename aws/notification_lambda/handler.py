import logging

from notification_service import NotificationService

logger = logging.getLogger()
logger.setLevel(logging.INFO)

service = NotificationService()


def handler(event, context):

    logger.info("Received notification event.")

    service.send(event)

    logger.info("Notification processing completed.")

    return {
        "statusCode": 200
    }
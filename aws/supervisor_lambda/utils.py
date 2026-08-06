def is_modify_event(record: dict) -> bool:
    """
    Returns True only for MODIFY events.
    """
    return record.get("eventName") == "MODIFY"


def is_metadata_record(record: dict) -> bool:
    """
    Returns True only for the shipment METADATA record.
    """

    try:
        return (
            record["dynamodb"]["Keys"]["SK"]["S"]
            == "METADATA"
        )
    except KeyError:
        return False


def extract_shipment_id(record: dict) -> str:
    """
    Extracts the shipment ID from the DynamoDB partition key.

    Example:
        PK = SHIPMENT#SHP-20034
        returns SHP-20034
    """

    try:
        pk = record["dynamodb"]["Keys"]["PK"]["S"]
    except KeyError as error:
        raise ValueError(
            "Partition key not found in DynamoDB stream record."
        ) from error

    if not pk.startswith("SHIPMENT#"):
        raise ValueError(
            f"Invalid partition key: {pk}"
        )

    return pk.replace(
        "SHIPMENT#",
        "",
        1,
    )
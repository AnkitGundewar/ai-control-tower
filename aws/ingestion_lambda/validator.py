REQUIRED_METADATA_FIELDS = [
    "PK",
    "SK",
    "shipmentId",
    "origin",
    "destination",
    "carrier",
    "status",
    "currentLocation",
    "eta",
    "slaDeadline",
    "slaRisk",
    "delayReason",
]

REQUIRED_EVENT_FIELDS = [
    "PK",
    "SK",
    "shipmentId",
    "timestamp",
    "eventType",
    "location",
    "details",
]


def validate_items(
    items: list[dict],
) -> list[dict]:

    validated_items = []

    seen = set()

    for index, item in enumerate(items):

        if not isinstance(item, dict):
            raise ValueError(
                f"Item {index} is invalid."
            )

        sk = item.get("SK")

        if sk == "METADATA":
            required = REQUIRED_METADATA_FIELDS

        elif sk.startswith("EVENT#"):
            required = REQUIRED_EVENT_FIELDS

        else:
            raise ValueError(
                f"Unknown SK: {sk}"
            )

        for field in required:

            if field not in item:

                raise ValueError(
                    f"Item {index} missing '{field}'."
                )

            if item[field] is None:

                raise ValueError(
                    f"Item {index} has null '{field}'."
                )

            if (
                isinstance(item[field], str)
                and not item[field].strip()
                and field != "delayReason"
            ):

                raise ValueError(
                    f"Item {index} has empty '{field}'."
                )

        key = (
            item["PK"],
            item["SK"],
        )

        if key in seen:

            raise ValueError(
                f"Duplicate item {key}"
            )

        seen.add(key)

        validated_items.append(item)

    return validated_items
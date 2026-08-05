import json


def parse_items(
    file_contents: str,
) -> list[dict]:
    """
    Parses the uploaded JSON file into
    DynamoDB items.
    """

    items = json.loads(file_contents)

    if not isinstance(items, list):
        raise ValueError(
            "Expected a JSON array."
        )

    return items
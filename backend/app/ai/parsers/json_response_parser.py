import json
import re


class JsonResponseParser:
    """
    Converts raw LLM responses into Python dictionaries.
    Handles:
    - Markdown code fences
    - Leading explanations
    - Trailing explanations
    - Plain JSON
    """

    @staticmethod
    def parse(text: str) -> dict:

        text = text.strip()

        # Remove ```json fences
        text = re.sub(r"^```json", "", text, flags=re.IGNORECASE)
        text = re.sub(r"^```", "", text)
        text = re.sub(r"```$", "", text)

        text = text.strip()

        # Try parsing directly
        try:
            return json.loads(text)

        except json.JSONDecodeError:
            pass

        # Extract first JSON object
        match = re.search(
            r"\{.*\}",
            text,
            re.DOTALL,
        )

        if match:

            return json.loads(
                match.group(0),
            )

        raise ValueError(
            "LLM did not return valid JSON."
        )
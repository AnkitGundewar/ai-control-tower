from pathlib import Path

class PromptLoader:
    """
    Loads prompt templates from the prompts directory.

    - Bedrock Prompt Management
    """

    PROMPT_DIRECTORY = (
        Path(__file__).resolve().parent.parent
        / "prompts"
    )

    @classmethod
    def load(
        cls,
        filename: str,
    ) -> str:

        prompt_path = cls.PROMPT_DIRECTORY / filename

        if not prompt_path.exists():
            raise FileNotFoundError(
                f"Prompt not found: {filename}"
            )

        return prompt_path.read_text(
            encoding="utf-8",
        )
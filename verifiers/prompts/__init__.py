from .system_prompts import (
    SIMPLE_PROMPT, CODE_PROMPT,
    DEFAULT_TOOL_PROMPT_TEMPLATE
)
from .few_shots import (
    MATH_FEW_SHOT, DOUBLECHECK_FEW_SHOT, CODE_FEW_SHOT, 
    TOOL_FEW_SHOT, COMMONSENSE_FEW_SHOT, SEARCH_FEW_SHOT,
    CALCULATOR_FEW_SHOT
)

__all__ = [
    "SIMPLE_PROMPT", "MATH_FEW_SHOT", "DOUBLECHECK_FEW_SHOT", 
    "CODE_FEW_SHOT", "CODE_PROMPT", "TOOL_FEW_SHOT",
    "COMMONSENSE_FEW_SHOT", "DEFAULT_TOOL_PROMPT_TEMPLATE",
    "SEARCH_FEW_SHOT", "CALCULATOR_FEW_SHOT"
]
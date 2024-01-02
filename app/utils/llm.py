import tiktoken
from app.config.config import MODEL_NAME, INPUT_COST, OUTPUT_COST

encoding = tiktoken.encoding_for_model(MODEL_NAME)

def count_tokens(text: str) -> int:
    return len(encoding.encode(text))

def cost(input: str, output:str) -> float:
    return count_tokens(input)*INPUT_COST + count_tokens(output)*OUTPUT_COST
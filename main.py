from dotenv import load_dotenv
load_dotenv()

from src.evaluate import evaluate_epic

if __name__ == "__main__":
    result = evaluate_epic("EPC-001")
    print(result.model_dump_json(indent=2))

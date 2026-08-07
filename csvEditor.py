from pathlib import Path

import pandas as pd

CSV_PATH = Path(__file__).resolve().parent / "csvFolder" / "testCSV.csv"
COUNTER_PATH = Path(__file__).resolve().parent / "csvFolder" / "simulation_counter.txt"
CSV_COLUMNS = [
    "Simulation Number",
    "Current Agent ID",
    "Transferred From Agent ID",
    "Role",
    "Message",
    "Similarity To Previous",
    "Global Similarity To Original",
    "Sentiment Analysis",
    "Propagation Depth"
]

_current_simulation_number = None


def _read_counter(counter_path):
    if not counter_path.exists():
        return 0

    try:
        return int(counter_path.read_text(encoding="utf-8").strip())
    except ValueError:
        return 0


def _write_counter(counter_path, value):
    counter_path.parent.mkdir(parents=True, exist_ok=True)
    counter_path.write_text(str(value), encoding="utf-8")


def createCSV(file_path=CSV_PATH, counter_path=COUNTER_PATH):
    global _current_simulation_number

    file_path = Path(file_path)
    counter_path = Path(counter_path)
    file_path.parent.mkdir(parents=True, exist_ok=True)

    if _current_simulation_number is None:
        next_simulation_number = _read_counter(counter_path) + 1
        _write_counter(counter_path, next_simulation_number)
        _current_simulation_number = next_simulation_number

    if not file_path.exists() or file_path.stat().st_size == 0:
        pd.DataFrame(columns=CSV_COLUMNS).to_csv(file_path, index=False)

    return _current_simulation_number


def addToCSV(current_agent_id, transferred_from_agent_id, role, message, similarity_to_previous, global_similarity_to_original, sentiment_analysis, depth, file_path=CSV_PATH):
    global _current_simulation_number

    file_path = Path(file_path)

    if _current_simulation_number is None:
        createCSV(file_path)

    if not file_path.exists() or file_path.stat().st_size == 0:
        createCSV(file_path)

    csv_loader = pd.DataFrame([{
        "Simulation Number": _current_simulation_number,
        "Current Agent ID": current_agent_id,
        "Transferred From Agent ID": transferred_from_agent_id,
        "Role": role,
        "Message": message,
        "Similarity To Previous": similarity_to_previous,
        "Global Similarity To Original": global_similarity_to_original,
        "Sentiment Analysis": sentiment_analysis,
        "Depth": depth
    }])

    csv_loader.to_csv(file_path, mode='a', header=False, index=False)
"""
Gate 1 schema validator for fingerprint YAML files.
Usage: python validate_schema.py
Requires: pyyaml (no other external dependencies)
"""

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: pyyaml not installed. Run: pip install pyyaml")
    sys.exit(1)

REQUIRED_LAYERS = [
    "identity",
    "translation_artifacts",
    "structural_formatting",
    "lexical_preferences",
    "risk_and_review",
    "drift",
]

FINGERPRINT_ROOT = Path(__file__).parent
TEMPLATE_PATH = FINGERPRINT_ROOT / "_template.yaml"
MB_PATH = FINGERPRINT_ROOT / "reporters" / "MB.yaml"


def load_yaml(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def check_file(label: str, path: Path, check_layers: bool = False) -> bool:
    print(f"\n--- {label} ---")
    print(f"Path: {path}")

    if not path.exists():
        print(f"FAIL: file not found at {path}")
        return False

    try:
        data = load_yaml(path)
    except yaml.YAMLError as e:
        print(f"FAIL: YAML parse error — {e}")
        return False

    if data is None:
        print("FAIL: file parsed as empty (None)")
        return False

    print("OK: parses as valid YAML")

    if not check_layers:
        return True

    # Check all six top-level layer keys
    missing_layers = [k for k in REQUIRED_LAYERS if k not in data]
    if missing_layers:
        print(f"FAIL: missing top-level layer keys: {missing_layers}")
        return False
    print(f"OK: all six layer keys present {REQUIRED_LAYERS}")

    # Check each layer has both observed and inferred subkeys
    failures = []
    for layer in REQUIRED_LAYERS:
        layer_data = data[layer]
        if not isinstance(layer_data, dict):
            failures.append(f"{layer}: expected dict, got {type(layer_data).__name__}")
            continue
        for subkey in ("observed", "inferred"):
            if subkey not in layer_data:
                failures.append(f"{layer}.{subkey}: missing")

    if failures:
        for f in failures:
            print(f"FAIL: {f}")
        return False

    print("OK: all layers have both 'observed' and 'inferred' subkeys")
    return True


def main():
    results = {}
    results["template"] = check_file("_template.yaml", TEMPLATE_PATH, check_layers=False)
    results["MB.yaml"] = check_file("reporters/MB.yaml", MB_PATH, check_layers=True)

    print("\n=== SUMMARY ===")
    all_pass = all(results.values())
    for label, passed in results.items():
        status = "PASS" if passed else "FAIL"
        print(f"  {status}  {label}")

    if all_pass:
        print("\nGATE 1: PASS")
        sys.exit(0)
    else:
        print("\nGATE 1: FAIL")
        sys.exit(1)


if __name__ == "__main__":
    main()

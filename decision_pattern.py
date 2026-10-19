
def evaluate_request(risk_level):
    """Demonstrate a simple allow, review, or reject decision."""

    if risk_level == "low":
        return "ALLOW"
    elif risk_level == "medium":
        return "REVIEW"
    else:
        return "REJECT"


if __name__ == "__main__":
    examples = ["low", "medium", "high"]

    for risk in examples:
        decision = evaluate_request(risk)
        print(f"Risk: {risk} -> Decision: {decision}")



def calculate_accuracy(y_true, y_pred):
    """
    Calculate classification accuracy.
    """

    # Step 1: Validate input lengths
    if len(y_true) != len(y_pred):
        raise ValueError("Input lengths must match.")

    # Step 2: Validate non-empty input
    if len(y_true) == 0:
        raise ValueError("Input lists cannot be empty.")

    # Step 3: Calculate accuracy
    correct = 0

    for x, y in zip(y_true, y_pred):
        if x == y:
            correct += 1

    return correct / len(y_true)

    
import sys

def process_input(threshold, limit):

    # Read input from input.txt
    inputs = sys.stdin.read().splitlines()

    cumulative_sum = 0.0
    outputs = []

    for value in inputs:
        value = float(value)

        if value > threshold:
            output = value - threshold
        else:
            output = 0.0

        if cumulative_sum + output > limit:
            output = limit - cumulative_sum

        cumulative_sum += output

        outputs.append(output)

    for output in outputs:
        print(f"{output:.1f}")

    return cumulative_sum




if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Usage: compute.py <threshold> <limit> <  <inputData.txt>")
        sys.exit(1)

    threshold = float(sys.argv[1])
    limit = float(sys.argv[2])

    # Final cumulative sum to output (n+1th output)
    print(f"{process_input(threshold, limit):.1f}")
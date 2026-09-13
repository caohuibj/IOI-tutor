# Complexity Review

Use for TLE/MLE, optimization questions, or when claimed complexity may be wrong.

## Review order

1. Reconstruct the algorithm independently from the code.
2. State the student's claimed complexity if supplied.
3. Derive actual time and space complexity, including repeated work, state count, amortization assumptions, recursion depth and container costs.
4. Separate asymptotic failure from constant-factor failure.
5. For partial-score tasks, identify the largest constraint/subtask the current complexity should handle.
6. Record a `CMP.*` root cause only when complexity is causal; otherwise keep complexity as secondary evidence.

## Coaching

At H0-H3, expose the bottleneck or adversarial input shape without giving the target optimization. H4 may reveal the key optimization direction. H5 may give pseudocode. H6 may show a complete optimal approach.

Prefer transitions such as brute force -> partial solution -> full solution rather than jumping directly to the editorial solution.

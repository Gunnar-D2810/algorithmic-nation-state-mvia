import numpy as np

def monte_carlo(base_prob=0.75, std=0.05, n=1000):
    samples = np.random.normal(base_prob, std, n)
    samples = np.clip(samples, 0, 1)
    return {
        "mean": np.mean(samples),
        "ci": np.percentile(samples, [2.5, 97.5])
    }
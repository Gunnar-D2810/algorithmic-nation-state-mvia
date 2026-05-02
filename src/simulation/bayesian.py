def bayesian_update(prior, likelihood, alt=0.2):
    return (likelihood * prior) / (
        likelihood * prior + alt * (1 - prior)
    )
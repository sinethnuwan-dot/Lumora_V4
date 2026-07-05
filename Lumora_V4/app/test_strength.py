from app.signal_strength import signal_strength


scores = [
    25,
    45,
    67,
    82,
    97,
]

print("=" * 40)

for score in scores:

    print(
        score,
        "->",
        signal_strength.get(score)
    )

print("=" * 40)
# Insert only to certain parts of Prince's code
# Do not delete Prince's unique code: Comparison of Trials (up to 3 rolls per total number of rolls)
# Retain Main Menu for option choosing
# Include the option to what is user's preferred bar chart design to display (2 options only)

# Coders' unqiue codes:

# Kay Caballes: Bar Chart Design (Two Bars, diff color)
# (To be inserted by Nathan)
# Create the graph
faces = [1, 2, 3, 4, 5, 6]

x = [0, 1, 2, 3, 4, 5]
width = 0.35

plt.figure(figsize=(8, 5))

# Experimental bars
plt.bar(
    [i - width/2 for i in x],
    experimental_probs,
    width,
    label="Experimental"
)
# Theoretical bars
plt.bar(
    [i + width/2 for i in x],
    theoretical_probs,
    width,
    label="Theoretical"
)

plt.xticks(x, faces)
plt.xlabel("Dice Face")
plt.ylabel("Probability")
plt.title("Dice Roll Probability Simulator")
plt.legend()

plt.show()


# Kay Quitollo: Difference from Theory (Console)
# (To be inserted by Yuri)
print("\nSUMMARY:")
    print(f"Total Trials (N): {n}")
    print("Face\tCount\tExperimental\tTheoretical\tDifference from Theory")

    for f in faces:
        prob = counts[f] / n
        percentage = prob * 100
        theoretical_percentage = theoretical_prob * 100
        difference = percentage - theoretical_percentage


# Kay Edmark: Difference from Theory (Bar Chart)
# (To be inserted by Lay Anne)
# Label each bar with its probability value
    for bar, p in zip(bars, exp_prob):
        plt.text(
            bar.get_x() + bar.get_width() / 2, p + 0.005,
            f"{p:.3f}", ha="center", fontsize=9
        )


# Kay Charmie: Difference from Theory (Console)
# (To be inserted by Alliyah)
for face in faces:
        print(
            f"\nFace {face} appeared {counts[face]} times."
            f"\nExperimental Probability = {counts[face]} / {n}"
            f"\n = {counts[face]/n:.4f}"
            f"\n = {(counts[face]/n)*100:.2f}%\n"
            )


# Kay Julie: 
# 1. Bar Chart Design (Legend)
# (To be inserted by Erika)
 # Bar graph for experimental probabilities
    plt.bar(
        faces,
        exp_prob,
        alpha=0.75,
        label=f"Experimental Probability (n={n})",
        zorder=2
    )
    # Reference line for theoretical probability
    plt.axhline(
        y=theoretical_prob,
        color="red",
        linestyle="--",
        linewidth=2,
        label="Theoretical Probability (1/6)",
        zorder=3
    )
#2. Console display (table like and others)
# Show simulation results
    print(f"\nTheoretical Probability for each face = 1/6 ≈ 0.1667 (16.67%)")

    print(f"\nResults for {n} Rolls\n")

    print(f"{'Face':<10}{'Frequency':<15}{'Experimental Probability':<35}{'Theoretical Probability'}")
    print("-" * 110)
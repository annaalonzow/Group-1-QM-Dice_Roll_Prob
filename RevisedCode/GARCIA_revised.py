# ==============================================================================
# DICE ROLL PROBABILITY SIMULATOR
# Developed by: Group 1
#
# AI ASSISTANCE DISCLAIMER:
# This program was developed with the assistance of AI to enhance the code
# structure, user input validation, and graph visualization layouts. :D
# ==============================================================================

import random
import collections
import matplotlib.pyplot as plt
import sys

#simulates the rolls.
def simulate_rolls(n):

    # Simulates "n" dice rolls and stores the result of each roll.
    rolls = [random.randint(1, 6) for _ in range(n)]

    # Counts how many times each die face appears in the simulation.
    counts = collections.Counter(rolls)

    # Stores the frequency and experimental probability for each die face.
    sim_data = {}
    for face in range(1, 7):
        face_count = counts.get(face, 0)
        sim_data[face] = {
            'frequency': face_count,
            'probability': face_count / n
        }

    return sim_data

# the display itself it is the second option itself.
def display_graphs(simulations):

    num_sims = len(simulations)

    # Creates subplots so multiple simulation results can be displayed side-by-side.
    fig, axes = plt.subplots(1, num_sims, figsize=(5 * num_sims, 5), squeeze=False)
    axes = axes.flatten()

    faces = list(range(1, 7))

    # Loops through each simulation and generates its probability graph. "Line 15-33"
    for i, sim in enumerate(simulations):
        n = sim['n']
        data = sim['data']
        probabilities = [data[face]['probability'] for face in faces]
        ax = axes[i]

        # Displays the experimental probabilities as a bar chart.
        ax.bar(faces, probabilities, color='skyblue', edgecolor='black',
               label=f"Experimental", alpha=0.8)

        # Displays the theoretical probability (1/6 ≈ 16.67%) as a reference line.
        ax.axhline(1 / 6, color="red", linestyle="--", linewidth=2,
                   label="Theoretical (1/6)")

        # labels and texts inside the figure
        ax.set_xlabel("Die Face", fontsize=10)
        ax.set_ylabel("Probability", fontsize=10)
        ax.set_title(f"Trial {i + 1} (N={n})", fontsize=12, fontweight='bold')
        ax.set_xticks(faces)
        ax.set_ylim(0, max(probabilities) + 0.05)  # Add a tiny space above the tallest bar
        ax.legend(loc="upper right", fontsize=8)

    plt.suptitle("Dice Roll Probability Convergence Comparison", fontsize=14, fontweight='bold', y=1.02)
    plt.tight_layout()
    plt.show()

# Displays the frequency and probability results for each simulation. "3" option
def display_percentages(simulations):
    theoretical_prob = (1 / 6) * 100

    for i, sim in enumerate(simulations):
        n = sim['n']
        data = sim['data']

        print(f"\n================ [ TRIAL {i + 1}: N = {n} ROLLS ] ================")
        print(f"{'Face':<8} | {'Frequency (Count)':<18} | {'Experimental %':<16} | {'Theoretical %':<15}")
        print("-" * 68)

        for face in range(1, 7):
            freq = data[face]['frequency']
            exp_pct = data[face]['probability'] * 100
            print(f"Dice {face:<3} | {freq:<18} | {exp_pct:>13.2f}% | {theoretical_prob:>13.2f}%")

        print("-" * 68)

        # Displays a simple observation based on the number of rolls.
        if n < 100:
            print("Observation: The numbers are completely wild and random...")
        elif n < 5000:
            print("Observation: Things are starting to settle down and steady out.")
        else:
            print(
                "Observation: woah, big numbers and it almost all the die faces hits the theoretical probability")

    print("=================================================================\n")

# Displays an explanation of the Law of Large Numbers.
def explain_law_of_large_numbers():

    print("\n" + "=" * 60)
    print(" " * 15 + "THE LAW OF LARGE NUMBERS (LLN)")
    print("=" * 60)
    print("The Law of Large Numbers is a fundamental theorem in probability.")
    print("It states that as an experiment is repeated many times, the")
    print("average of the results (the experimental probability) will")
    print("increasingly approach the expected value (the theoretical")
    print("probability).\n")

    print("IN THE CONTEXT OF THIS SIMULATOR:")
    print("• Theoretical Probability: Mathematically, a perfectly fair")
    print("  6-sided die has exactly a 1 in 6 chance (≈ 16.67%) of")
    print("  landing on any specific face.\n")

    print("• Small N (e.g., 10 rolls): In the short term, chaos rules.")
    print("  You might roll three 6s and zero 1s. The experimental")
    print("  probability will not match the math.\n")

    print("• Large N (e.g., 10,000 rolls): In the long term, randomness")
    print("  irons itself out. If you roll the die enough times, every")
    print("  single face will appear almost exactly 16.67% of the time.")
    print("=" * 60 + "\n")

# the menu itself
def main():

    # Stores the current simulation results for later viewing.
    current_simulations = []

    while True:
        print("\n======================")
        print("1. Simulate")
        print("2. Show Graph")
        print("3. Show Percentage")
        print("4. What is the Law of Large Numbers?")
        print("5. End")
        print("======================")

        choice = input("Select an option (1-5): ").strip()

        if choice == '1':

            # Clears previous simulation data before running a new set of simulations.
            current_simulations.clear()

            # data validation and ask the user how many times they want to roll the dice,
            while True:
                user_input = input("How many times would you like to roll the dice per trial? ")
                try:
                    rolls_count = int(user_input)
                    if rolls_count <= 0:
                        print("Please enter a positive number greater than 0.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole positive integer.")

            # Ask how many separate simulation to simulate (up to 3) to compare them
            while True:
                comp_input = input("How many comparison trials would you like to run? (Maximum of 3): ")
                try:
                    num_trials = int(comp_input)
                    if num_trials < 1 or num_trials > 3:
                        print("System constraint warning: You must choose between 1 and 3 trials.")
                        continue
                    break
                except ValueError:
                    print("Invalid input. Please enter a whole number between 1 and 3.")

            # Runs the requested number of dice roll simulations.
            print(f"\nProcessing {num_trials} independent simulations of {rolls_count} rolls each...")
            for _ in range(num_trials):
                result_dataset = simulate_rolls(rolls_count)
                current_simulations.append({
                    'n': rolls_count,
                    'data': result_dataset
                })
            print("Simulations successfully saved to temporary program memory!")

        elif choice == '2':
            # if no simulation yet, they would be back in menu otherwise it would generate the graph.
            if not current_simulations:
                print("\n[Error] No data available. Please run a simulation (Option 1) first!")
            else:
                print("\nGenerating unified multi-plot window dashboard...")
                display_graphs(current_simulations)

        elif choice == '3':
            # if no simulation yet, they would be back in menu otherwise it would generate the percentage.
            if not current_simulations:
                print("\n[Error] No data available. Please run a simulation (Option 1) first!")
            else:
                display_percentages(current_simulations)

        elif choice == '4':
            # the book-math explanation text
            explain_law_of_large_numbers()

        elif choice == '5':
            #  shut down the script sooo bye bye
            print("\nEnding program. Thank you for using the simulator! :D")
            sys.exit()

        else:
            print("\nInvalid choice. Please select a valid option menu key (1-5).")


if __name__ == "__main__":
    main()
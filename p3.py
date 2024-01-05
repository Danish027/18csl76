# Importing necessary library
import csv

# Function to implement Candidate-Elimination algorithm
def candidate_elimination(dataarr):
    # Number of attributes
    cols = len(dataarr[0])

    # Initialize Specific Hypothesis (most specific hypothesis)
    shypo = [['0']*(cols-1)]

    # Initialize General Hypothesis (most general hypothesis)
    ghypo = [['?']*(cols-1)]

    # Printing initial hypotheses
    print("Initial Specific Hypothesis:", shypo)
    print("Initial General Hypothesis:", ghypo)

    # Process each example in the data
    for x in range(1, len(dataarr)):
        lst = dataarr[x]

        # If the example is positive
        if lst[cols-1] == "1":
            for i in range(0, cols-1):
                # Update specific hypothesis
                if shypo[i] == lst[i]:
                    continue
                shypo[i] = '?' if shypo[i] != '0' else lst[i]

            # Update general hypothesis
            ghypo = [g for g in ghypo if all(g[i] in ['?', lst[i]] for i in range(cols-1))]

        # If the example is negative
        elif lst[cols-1] == "0":
            ghypo.clear()
            for i in range(0, cols-1):
                # Update general hypothesis
                if lst[i] != shypo[i] and shypo[i] != '?':
                    temp_list = ['?']*i + [shypo[i]] + ['?']*(cols-2-i)
                    if temp_list not in ghypo:
                        ghypo.append(temp_list)

        # Print the hypotheses after processing each row
        print("S Hypothesis after row", x, "=", shypo)
        print("G Hypothesis after row", x, "=", ghypo)

    # Print the final hypotheses
    print("Final Specific Hypothesis:", shypo)
    print("Final General Hypothesis:", ghypo)

# Reading data from CSV file
dataarr = []
with open('data/enjoysport.csv') as f:
    csv_reader = csv.reader(f)
    for line in csv_reader:
        dataarr.append(line)

# Calling the Candidate-Elimination function
candidate_elimination(dataarr)

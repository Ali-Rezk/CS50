import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(argv) > 3 or len(argv) < 3:
        print("commandline error")

    database = sys.argv[1]
    sequence = sys.argv[2]

    # TODO: Read database file into a variable
    with open("large.csv") as file:
        data = csv.DictReader(file)

    # TODO: Read DNA sequence file into a variable
    with open("sequences/5.txt") as file:
        seq = sequence.read()

    # TODO: Find longest match of each STR in DNA sequence
    agatc = longest_match(seq, "AGATC")
    aatg = longest_match(seq, "AATG")
    tatc = longest_match(seq, "TATC")

    # TODO: Check database for matching profiles
    for row in data:
        if row["AGATC"] == agatc and row["AATG"] == aatg and row["TATC"] == tatc:
            print(row["name"])
            return
    else:
        print("no match")



def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


main()

import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) > 3 or len(sys.argv) < 3:
        print("commandline error")

    # TODO: Read database file into a variable
    file = open(sys.argv[1])
    data = csv.DictReader(file)

    # TODO: Read DNA sequence file into a variable
    file1 = open(sys.argv[2])
    seq = file1.read()

    # TODO: Find longest match of each STR in DNA sequence
    AGATC = longest_match(seq, "AGATC")
    AATG = longest_match(seq, "AATG")
    TATC = longest_match(seq, "TATC")

    if sys.argv[2] == "databases/large.csv":
        TTTTTTCT = longest_match(seq, "TTTTTTCT")
        TCTAG = longest_match(seq, "TCTAG")
        GATA = longest_match(seq, "GATA")
        GAAA = longest_match(seq, "GAAA")
        TCTG = longest_match(seq, "TCTG")

    # TODO: Check database for matching profiles
    for row in data:
        if int(row["AGATC"]) == AGATC and int(row["AATG"]) == AATG and int(row["TATC"]) == TATC and int(row["GAAA"]) == GAAA:
            if int(row["TTTTTTCT"]) == TTTTTTCT and int(row["TCTAG"]) == TCTAG and int(row["GATA"]) == GATA and int(row["TCTG"]) == TCTG and int(row["GAAA"]) == GAAA:
                print(row["name"])
                file.close()
                file1.close()
                return
    else:
        print("No match")
        file.close()
        file1.close()



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

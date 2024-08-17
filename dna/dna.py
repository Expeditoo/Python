import csv
import sys

def read_csv(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        data = list(reader)
    strs = data[0][1:]
    profiles = {row[0]: list(map(int, row[1:])) for row in data[1:]}
    return strs, profiles

def read_txt(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        return file.read().strip()

def longest_match(sequence, subsequence):
    longest_run = 0
    subseq_length = len(subsequence)
    seq_length = len(sequence)

    for i in range(seq_length):
        count = 0

        while True:
            start = i + count * subseq_length
            end = start + subseq_length

            if sequence[start:end] == subsequence:
                count += 1
            else:
                break

        longest_run = max(longest_run, count)

    return longest_run

def main(csv_file_path, txt_file_path):
    strs, profiles = read_csv(csv_file_path)
    dna_sequence = read_txt(txt_file_path)
    
    dna_counts = [longest_match(dna_sequence, STR) for STR in strs]
    
    for name, profile_counts in profiles.items():
        if dna_counts == profile_counts:
            print(name)
            return
    
    print("No match")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python dna.py databases/small.csv sequences/1.txt")
    else:
        main(sys.argv[1], sys.argv[2])

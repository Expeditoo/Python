Background

DNA, the carrier of genetic information in living beings, has been used in criminal justice for decades. 
But how, exactly, does DNA profiling work? Given a DNA sequence, how can forensic investigators identify to whom it belongs?

Well, DNA is actually just a sequence of molecules called nucleotides, arranged in a particular shape (a double helix).
Each DNA nucleotide contains one of four different bases: adenine (A), cytosine (C), guanine (G), or thymine (T). Each human cell contains billions of these nucleotides arranged in sequence.
Some parts of this sequence (i.e., genome) are the same, or at least very similar, in almost all humans, but other parts of the sequence have greater genetic diversity and,
therefore, vary more in the population.

One place where DNA tends to have high genetic diversity is in Short Tandem Repeats (STRs).
An STR is a short sequence of DNA bases that tends to repeat consecutively numerous times at specific locations within a person's DNA.
The number of times a given STR repeats varies greatly between individuals.
In the DNA samples below, for example, Alice has the STR AGAT repeated four times in her DNA, while Bob has the same STR repeated five times.

Using multiple STRs, rather than just one, can improve the accuracy of DNA profiling.
If the probability of two people having the same number of repeats for a single STR is 5% and the analyst looks at 10 different STRs,
the probability of two DNA samples matching purely by chance is about 1 in 1 quadrillion (assuming all STRs are independent of each other).
Therefore, if two DNA samples match the number of repeats for each of the STRs, the analyst can be confident they came from the same person.
CODIS, the FBI’s DNA database, uses 20 different STRs as part of its DNA profiling process.

What would such a DNA database look like? Well, in its simplest form, you could imagine formatting a DNA database as a CSV file,
where each row corresponds to an individual and each column corresponds to a specific STR.


name,AGAT,AATG,TATC
Alice,28,42,14
Bob,17,22,19
Charlie,36,18,25

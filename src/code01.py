
if __name__ == '__main__': 
	s = "TGCGACAGAATTATTGTCCACATCCTAGGAGTGTTCCGCTGTGAGTTCACTCGCTGCCGATTTTCACCGTAAAGGATAGGTAACGGGCGGCCCCCGTAGGTACGGGTAGTTATATCGTTGTGTTTAGTAGCCAAAGGCTGTCGCGAAAATGATCGCGTCTTGGCAGATATACGCCAACGGTTCTGGTTATGGTACCTTATATTCTAAGTACCACCCGTAGATCTTCCGGATCCTTCCGGCGCAGTTATGACTACAAAGGTTACTAATGCCGCTCAACCATGTCTAACGCAGAGTAACAAACCAATATTCTCCGCTAGGACTACCTCGGTCGTAGCGTAACCCTAGGTAGACGCAGCTTGCCAGATATGGATCCGAGTACATTGCGAATGAGTGATCGTTGCGATCTAGAAGCGATCCAGCGATTCCGTTGTCCGCAGTACGTTCAATGAGCGGTAACAATTGGCAATAGTTACTGAACGTCCAATCGGATAGACATCTCGGCGGATTTGAGATTAGTGGCAACCGAAGACTATCTCCAATAGTAGATCCGCAGGAAGGAATGGGATCTCTCGTTACACCCGCACACCGCCAACTTATCGTACCGGGGAGAGTTCGACCCCCCAAGGGTAGTTGAACACTTGGTTGTACGTGCACTGAAATCGAATGAGTCATTTGGAAGAAAGATTACAACAAAGGGGACTCAAAAATCGTGTACCGTCCCCCATTATTACGCTCTTTATTCTAGCCGCTCGCGCACGACTTTAAACGGAGGCGCGTGGCTGCAAATACAACGAATTCGGCGCTGACAAGGCATGCAGTTACAACTCATTT"
	count = dict()
	for c in s:
		if (c in count):
			count[c] = count[c]+1
		else:
			count[c] = 1

	print str(count["A"]) + " " + str(count["C"]) + " " + str(count["G"]) + " " + str(count["T"])


"""
Steps:
1. Go to NCBI webiste.
2. Search for "NM_201917.1"  or "NM_207618.2" under Nucleotide.
3. Get the CDS range. CDS for NM_207618.2 - 21..938 (for python - 20..938) and NM_201917.1 - 111..2843 (for python - 110..2843)
4. Click on "FASTA" and then copy the DNA code into a notepad document and save in the same directory as the code file.
5. Run the below program.
"""
def DNA_Translate(input_file, start, end):
    """
    This funtion inports a DNA file and will return the type of the protein for every 3 sequence.
    """

    DNA_file = open(input_file, "r")
    seq = DNA_file.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    seq = seq[start: end]
    # print(len(seq))
    # print(seq)


    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T', 
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',                  
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P', 
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R', 
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A', 
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G', 
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L', 
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W', 
    } 
    #print(table)

    protein = []
    if len(seq) % 3 == 0:
        for code in range(0, len(seq), 3):
            codon = seq[code: code + 3]
            pro = table[codon]
            protein.append(pro)
    else:
        print(len(seq) % 3)
    print(protein[:-1])
    

#! Please enter the path of the input file as the first paramater.
#! Second paramater is start point and third parameter is end point.
DNA_Translate("", 110, 2843)
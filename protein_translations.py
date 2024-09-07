def proteins(strand:str)->list:
    codon_dict = {
        "Methionine": ["AUG"],
        "Phenylalanine": ["UUU", "UUC"],
        "Leucine": ["UUA", "UUG"],
        "Serine": ["UCU", "UCC", "UCA", "UCG"],
        "Tyrosine": ["UAU", "UAC"],
        "Cysteine": ["UGU", "UGC"],
        "Tryptophan": ["UGG"],
        "STOP": ["UAA", "UAG", "UGA"]
    }
    temp_codon = []
    for char in range(0, len(strand), 3):
       temp_codon.append(strand[char:char+3])
    protein_list = []   
    for codon in temp_codon:
        if codon in codon_dict.get("STOP"):
            break
        for protein, rna in codon_dict.items():
            if codon in rna:
                protein_list.append(protein)
    return protein_list
print(proteins("UGGUAGUGG"))
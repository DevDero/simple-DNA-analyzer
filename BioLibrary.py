
def CountPointMutation(stringS,stringT):

    if(len(stringS) != len(stringT)):
        return "Unvalid Strand!"
    pmAmount=0
    lenght=len(stringS)
    for i in range(lenght):
        if(stringS[i] != stringT[i]):
            pmAmount+=1
    return(pmAmount)
    
def Transcribing(_input):
    dna=list(_input)
    lenght=len(_input)
    for i in range(lenght):
        if(dna[i]=="T"):
            dna[i]="U"
    RNA = ''.join(dna)
    return(RNA)

def ComplementingDNA(_input):
    lenght=len(_input)
    dna=list(_input)
    for i in range(lenght):
        if(dna[i]=="A"):
            dna[i]="T"
        elif(dna[i]=="G"):
            dna[i]="C"
        elif(dna[i]=="T"):
            dna[i]="A"
        elif(dna[i]=="C"):
            dna[i]="G"
    dna.reverse()
    cDNA=''.join(dna)
    return(cDNA)
        
def CountNucleotides(_input):
    a=0
    t=0
    g=0
    c=0
    lenght=len(_input)
    for i in range(lenght):
        if(_input[i]=="A"):
            a+=1
        if(_input[i]=="T"):
            t+=1
        if(_input[i]=="G"):
            g+=1
        if(_input[i]=="C"):
            c+=1
    return(a,c,g,t)

def EnumeratingGeneOrder(_input):
    firstGene=[]
    totalGenes=[]
    """Create first gene"""
    for i in range(1,_input+1):
        firstGene.append(i)
    leadGene=firstGene
    if(_input%2==0):
        """Gene is even so Swap i->k-1"""
        for i in range(_input-1): 
            _genes=Permutate(leadGene)
            totalGenes.append(_genes)
            leadGene=HeapsSwapEven(leadGene,i)
    else:
        """Gene is odd so Swap 0->k-1"""
        for i in range(_input-1): 
            _genes=Permutate(leadGene)
            leadGene=HeapsSwapOdd(_genes[_input-1])
            totalGenes.append(_genes)
    return((totalGenes))

def HeapsSwapEven(Gene,kVal):
    lenght=len(Gene)
    k=Gene[kVal]
    last=Gene[lenght-1]
    Gene[kVal]=last
    Gene[lenght-1]=k
    return Gene

"""Swap last element with first element"""
def HeapsSwapOdd(Gene):
    newGene=Gene.copy()
    lastElement=len(newGene)-1
    newGene[0]=Gene[lastElement]
    newGene[lastElement]=Gene[0]
    return newGene

"""Returns a list of permetated genes"""
def Permutate(Inputgene):
    permutatedGenes=[]
    currentGene=Inputgene
    lenght=len(Inputgene)
    permutatedGenes.append(currentGene)
    for j in range(lenght-1):
        newGene=[]
        newGene.append(currentGene[(lenght-1)])
        for i in range(lenght-1):
            newGene.append(currentGene[i])
        permutatedGenes.append(newGene)
        currentGene=newGene
    return permutatedGenes

def flatten_list(nested_list):
    """flatten list of genes."""
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten_list(item))
        else:
            flat_list.append(item)
    return flat_list
    
def heaps_algorithm(count, sequence, result):
    if count == 1:
        result.append(sequence.copy())
    else:
        for i in range(count):
            heaps_algorithm(count - 1, sequence, result)
            if count % 2 == 0:  # If n is even
                sequence[i], sequence[count - 1] = sequence[count - 1], sequence[i]
            else:  # If n is odd
                sequence[0], sequence[count - 1] = sequence[count - 1], sequence[0]

def print_arrays(array_of_arrays):
    """Prints each sub-array of integers with one space between elements and a new line after each sub-array."""
    for array in array_of_arrays:
        print(" ".join(map(str, array)))
    
def NumberofPermutation(count):
    a=1
    for i in range(1,count+1):
        a = a*i
    return a
  
def main():
    """
    CountNucleotides("ATGC")
    Transcribing("ATGC")
    ComplementingDNA("ATGC")
    CountPointMutation("ATGCG",)
    """
    """EnumeratingGeneOrder(5)"""
    l=[]
    heaps_algorithm(5,[1,2,3,4,5],l)
    print(NumberofPermutation(5))
    print_arrays(l)

if __name__ == "__main__":
    main()
import sid_functionalizedAptamerBreeder as ab
import hairpins as hp
import mutate as mt

#Function List:
# mt.mutate(sequence)
# hp.hairpin(sequence, max_hp_len)
# hp.striplist(list, stripval)
# hp.create_hairpin_dict(txtfile)
# hp.inverted_repeat(sequence)
# ab.generateAptamer(length)
# ab.genPool(pool_size)
# ab.computeChildFitnes(parent1, parent2, child)
# ab.crossover(parent1, parent2)
# ab.breed(sortedAptamerList, topcutoff, offspring)
'''
Order of how to do thing:

create pool
[
breed pool
for p in pool:
    cutoff = getbestFitnessScoringMembers(poolP) # cutoff is top 10%, can be adjusted
    if isElite(p) == True: # elite is top 2%, can be adjusted
         new_pool.append(p)
    while len(new_pool) < len(pool):
         new_pool.append(crossover(cutoff[randint], cutoff[randint]))
    for member in new_pool:
          new_pool.append(mutate(cutoff[randint])) 
    new_pool = removeChildrenWithHairpins(new_pool)
pool = new_pool
]
repeat [...] for x generations

'''
# generation member: ['seq_1', 'asdasdasdasd', 45]
def runGeneticAlgorithim(populationsize, generations):
    firstGen = ab.genPool(populationsize)
    for gen in range(generations):
        if gen == 0:
            lastGen = ab.breed(firstGen, gen)
        else:
            lastGen = ab.breed(lastGen, gen)
        for aptamer in lastGen:
            if hp.hairpin(aptamer[1]) != 0:
                lastGen.remove(aptamer)
        for aptamer in lastGen:
            aptamer[1] = mt.mutate(aptamer[1])
    return [firstGen, lastGen] 


#is a list where each element is in the format [offspring_1, 'asdasdasda', 69]
def simulateAptamerGA(optFileName, pop_size, gens):
    firstAndlast = runGeneticAlgorithim(pop_size, gens) 
    for gen in range(len(firstAndlast)):
        sorting = firstAndlast[gen]
        tmp = []
        for aptamer in sorting:
            tmp.append([aptamer[0], aptamer[1], aptamer[2]])
        tmp = sorted(tmp, key=lambda x: x[2], reverse=True)
        firstAndlast[gen] = tmp
    
    with open(optFileName, 'w') as opt:
        opt.write('\t\t\t\tFirst Generation\t\t\t\t\t\t\t\t\t\tLast Generation\n')
        opt.write('Aptamer #\tAptamer Sequence\t\tFitness Score\t\tFitness Score\tAptamer Sequence\t\tAptamer #\n')
        for linum in range(len(firstAndlast[0])):
            opt.write(firstAndlast[0][linum][0]+'\t'+firstAndlast[0][linum][1]+'\t'+str(firstAndlast[0][linum][2])+'\t\t\t\t\t'+str(firstAndlast[1][linum][2])+'\t\t\t'+firstAndlast[1][linum][1]+'\t'+firstAndlast[1][linum][0]+'\n')
    opt.close()

#    with open(optFileName, 'w') as opt:
#        opt.write('Aptamer #\tAptamer Sequence\tFitness Score\n')
#        for aptamer in lines:
#            opt.write(str(aptamer[0]) + '\t' + str(aptamer[1]) + '\t' + str(aptamer[2]) + '\n')
# potentialy useful statistics, but not sure where to output them, can add more if desired
#    totalApts = len(final_gen)
#    avgLength = average([len(x[0] for x in final_gen])
#    avgFitness = average([x[2] for x in final_gen])
    

simulateAptamerGA('test.GA', 100, 50)




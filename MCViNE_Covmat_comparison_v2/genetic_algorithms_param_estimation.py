# The purpose of this program is to test one or more genetic algorithms for parameter estimation

import numpy as np
import matplotlib.pyplot as plt



# first, define the model equation and vector of real parameters
real_params = [1.3, 2.4]
param_constraints = [[0.0, 5.0], [0.0, 5.0]]

def get_noise(dataset_size):
	mean = 0.0
	sigma = 0.4
	additive_noise = np.random.normal(mean, sigma, dataset_size)
	return additive_noise




# create function to compute total cost as a function only of parameters
def model_least_squares_cost(params):
	#theory = model_equation(x1v, x2v, params)
	t, Erange, theory = mourigal_model.compute_model_grid(params)
	#data = noisy_data
	data = mourigal_noisy_data
	#data = pure
	sum_squares_cost = pixel_by_pixel_least_squares_cost(data, theory)
	avg_square_cost = sum_squares_cost / (dataset_size[0]*dataset_size[1])
	return avg_square_cost

# inverse of cost (because pyevolve wants "benefit" rather than cost)
def model_benefit(params):
	cost = model_least_squares_cost(params)
	benefit = 1.0 / cost
	return benefit

# specify genetic algorithm parameters and run
#rand_seed = 1204929329098
p_mut = 0.1
p_crossover = 0.7
pop_size = 10
num_save = 1
breeding_percent = 0.6
num_gens = 10
# from pyevolve import G1DList
# from pyevolve import GSimpleGA

# genome = G1DList.G1DList(2)
# genome.evaluator.set(model_benefit)
# ga = GSimpleGA.GSimpleGA(genome)
# ga.evolve(freq_stats=10)
# print ga.bestIndividual()
'''
Inputs:
	chromosome = list (lenght N) of parameters (genes) to be optimized
	chromosome_constraints = list (length N) of length 2 lists; each sublist contains the upper and lower bounds on each parameter
	p_mut = probability of mutation
Return:
	chromosome (possibly mutated)
'''
def mutate(chromosome, chromosome_constraints, p_mut):
	rand_num = np.random.uniform(0.0, 1.0)
	if rand_num < p_mut:
		#select random gene from chromosome and mutate it by a random amount
		N = len(chromosome)
		gene = np.random.random_integers(0,(N-1))  # select randomly a gene from the chromosome
		new_gene_allele = np.random.uniform(chromosome_constraints[gene][0], chromosome_constraints[gene][1])  # now, randomly select a new value for the gene allele within the constraints
		chromosome[gene] = new_gene_allele  # mutate the selected gene
	return chromosome


'''
Inputs:
	chromosome_1,2 = lists (length N) of parameters (genes)
	p_crossover = probability of crossover
Return:
	[chromosome_1, chromosome_2] (possibly crossed)
'''
def single_crossover(chromosome_1, chromosome_2, p_crossover):
	rand_num = np.random.uniform(0.0, 1.0)
	if rand_num < p_crossover:
		N = len(chromosome_1)
		gene = np.random.random_integers(1,N)  # select randomly a gene position for the crossover to take place
		child_1 = chromosome_1[:]
		child_1[0:gene] = chromosome_2[0:gene]
		child_2 = chromosome_2[:]
		child_2[0:gene] = chromosome_1[0:gene]
		chromosome_1 = child_1[:]
		chromosome_2 = child_2[:]

	return [chromosome_1, chromosome_2]


def init_pop(pop_size, chromosome_length, chromosome_constraints):
	pop = []
	for i in range(pop_size):
		individual = []
		for x in range(chromosome_length):
			gene_x = np.random.uniform(chromosome_constraints[x][0], chromosome_constraints[x][1])  # randomly select a viable initial allele value for the gene in position x of the chromosome
			individual.append(gene_x)
		pop.append(individual)  # add this new initialized individual to the population
	return pop


def rank_pop_by_cost(pop, cost_function):
	# sort the population list according to the cost function specified (from lowest cost to highest cost)
	sorted_pop = sorted(pop, key=cost_function)
	return sorted_pop


def iterate_generation(sorted_pop, pop_size, num_save, breeding_percent, p_mut, p_crossover, chromosome_constraints):
	num_breeders = int(round(pop_size * breeding_percent))  # specify the number of individuals to engage in breeding

	# extract first 'num_save' individuals (most fit individuals) to save, unaltered, until the next round
	pop0 = sorted_pop[0:num_save]

	# extract breeders based on fitness (lowest cost)
	pop1 = sorted_pop[0:num_breeders]
	# extract non-breeders (leaving off the last num_save least fit individuals)
	pop2 = sorted_pop[num_breeders:pop_size-num_save]

	# breed
	for i in range(num_breeders):
		# select the index of two parents (i.e. two numbers) from 0 to num_breeders-1, inclusive
		parent_1_index = np.random.random_integers(0,num_breeders-1)
		parent_2_index = np.random.random_integers(0,num_breeders-1)
		# get parent individuals from population
		p1 = pop1[parent_1_index]
		p2 = pop1[parent_2_index]
		# perform probabilistic crossover
		p1, p2 = single_crossover(p1, p2, p_crossover)
		# return crossed individuals to fit population
		pop1[parent_1_index] = p1
		pop1[parent_2_index] = p2

		
	new_pop = pop1 + pop2

	# mutate everyone, except the first num_save individuals
	for i in range(len(new_pop)):
		individual = new_pop[i]
		individual = mutate(individual, chromosome_constraints, p_mut)	
		new_pop[i] = individual

	new_pop = pop0 + new_pop
	# return new population, mutated and crossed
	return new_pop


def run_ga(pop_size, breeding_percent, num_save, p_mut, p_crossover, chromosome_constraints, cost_function, num_gens, true_params):

	# initialize population
	length_chromosome = len(chromosome_constraints)
	pop = init_pop(pop_size, length_chromosome, chromosome_constraints)

	# create convergence check list
	err_convergence = []
	cost_convergence = []

	# iterate through generations
	for gen in range(num_gens):
		ranked_pop = rank_pop_by_cost(pop, cost_function)

		# check convergence (by Euclidean distance to true parameters)
		#error = np.sqrt((true_params[0] - ranked_pop[0][0])**2 + (true_params[1] - ranked_pop[0][1])**2)
		error = np.sqrt((true_params[0] - ranked_pop[0][0])**2 + (true_params[1] - ranked_pop[0][1])**2 + (true_params[2] - ranked_pop[0][2])**2 + (true_params[3] - ranked_pop[0][3])**2)
		err_convergence.append(error)

		cost_convergence.append(cost_function(ranked_pop[0]))

		# TEST -- this code is to monitor output from each generation
		# plot convergence (error of best individual)
		bestIndividual = ranked_pop[0]
		bestErrors = err_convergence
		best_costs = cost_convergence
		plt.figure(1)
		plt.subplot(231)
		gens = np.array(range(gen+1))
		gens = gens + 1
		besterr = np.array(bestErrors)
		plt.plot(gens, bestErrors)
		plt.xlabel("generation")
		plt.ylabel("best Individual error")

		plt.subplot(232)
		plt.plot(gens, best_costs)
		plt.xlabel("generation")
		plt.ylabel("cost of best individual")

		plt.subplot(233)
		plt.xlabel("pure")
		#plt.pcolormesh(x1v, x2v, pure)
		plt.pcolormesh(t, Erange, mourigal_true_convolved)

		plt.subplot(234)
		plt.xlabel("noisy_data")
		#plt.pcolormesh(x1v, x2v, noisy_data)
		plt.pcolormesh(t, Erange, mourigal_noisy_data)

		plt.subplot(235)
		#best_fit = model_equation(x1v, x2v, bestIndividual)
		#best_fit = model_equation(t, Erange, bestIndividual)
		T, E, best_fit = mourigal_model.compute_model_grid(bestIndividual)
		plt.xlabel("best_fit")
		#plt.pcolormesh(x1v, x2v, best_fit)
		plt.pcolormesh(t, Erange, best_fit)

		plt.show()

		print("starting generation:  " + str(gen) + "\n")
		print(bestIndividual)
		# END OF TEST

		# evolve generation
		pop = iterate_generation(ranked_pop, pop_size, num_save, breeding_percent, p_mut, p_crossover, chromosome_constraints)




	# select most fit individual
	rank_pop = rank_pop_by_cost(pop, cost_function)
	bestIndividual = rank_pop[0]

	return [bestIndividual, err_convergence, cost_convergence]



if __name__ == '__main__':


	# bestIndividual, bestErrors, best_costs = run_ga(pop_size, breeding_percent, num_save, p_mut, p_crossover, param_constraints, model_least_squares_cost, num_gens, real_params)

	bestIndividual, bestErrors, best_costs = run_ga(pop_size, breeding_percent, num_save, p_mut, p_crossover, mourigal_param_constraints, model_least_squares_cost, num_gens, mourigal_real_params)

	# plot convergence (error of best individual)
	plt.figure(1)
	plt.subplot(231)
	gens = np.array(range(num_gens))
	gens = gens + 1
	besterr = np.array(bestErrors)
	plt.plot(gens, bestErrors)
	plt.xlabel("generation")
	plt.ylabel("best Individual error")

	plt.subplot(232)
	plt.plot(gens, best_costs)
	plt.xlabel("generation")
	plt.ylabel("cost of best individual")

	plt.subplot(233)
	plt.xlabel("pure")
	#plt.pcolormesh(x1v, x2v, pure)
	plt.pcolormesh(t, Erange, mourigal_true_convolved)

	plt.subplot(234)
	plt.xlabel("noisy_data")
	#plt.pcolormesh(x1v, x2v, noisy_data)
	plt.pcolormesh(t, Erange, mourigal_noisy_data)

	plt.subplot(235)
	#best_fit = model_equation(x1v, x2v, bestIndividual)
	best_fit = model_equation(t, Erange, bestIndividual)
	plt.xlabel("best_fit")
	#plt.pcolormesh(x1v, x2v, best_fit)
	plt.pcolormesh(t, Erange, best_fit)

	plt.show()

	print(bestIndividual)
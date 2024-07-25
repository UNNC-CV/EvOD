
class Env(model):
    def __init__(self):
        self.init_data = init 
        self.result_data = result
        self.data = None
        self.obsevation = []
        self.step_n = 0 
        self.action = 0
        self.scale = 0 
        self.result = None 
        self.base = None 
        self.reward = 0 
        self.t = 0
        self.q = 0
        self.detect_model = model
    def convertAction(self):
        if self.action == 0:
            self.scale = 0.8
        elif self.action ==5:
            self.scale = 6
        else:
            self.scale = self.action
    def getReward(self): 
        r0 = self.result.avg_correct  - self.data.avg_correct 
        try:
            k =  self.result.avg_correct/self.result.obj_num 
        except:
            k =  self.result.avg_correct 
        try:
            k1 =  self.data.avg_correct/self.data.obj_num 
        except:
            k1 = self.data.avg_correct 
        r1 = k - k1
        
        r2 = self.result.true_rate - self.data.true_rate 
       

        self.reward  = r1 + r2
    def step(self,action):
        self.step_n +=1
        self.action = action
        # self.result = self.result_data[self.action][self.q][self.t]
        self.result = self.detect_model.detect(self.scale,self.obsevation) 
        self.convertAction()
     
        done = False 
        if self.t >= len(self.init_data[1][self.q])-1:
            done = True
        else:
            self.getObs()
        return self.obsevation, self.result,done 
    def getObs(self):
        self.t =self.step_n
        self.data = self.init_data[1][self.q][self.t]
        self.base =  self.result_data[1][self.q][self.t]  
        self.obsevation = self.data.getObs()

    def reset(self,q):
        self.t = 0
        self.q = q
        self.data = self.init_data[1][q][self.t] 
        self.base =  self.result_data[1][q][self.t]  
        self.obsevation = self.data.getObs()
        self.step_n = 0
        self.action = 0
        self.scale = 0
        self.reward = 0 

        return self.obsevation

class EvolutionaryStrategy:
    def __init__(self, population_size, mutation_rate, crossover_rate, action_dim):
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.action_dim = action_dim
        self.history = []

    def initialize_population(self, current_actions): 
        population = [current_actions] + self.history[-(self.population_size-1):]
        return np.array(population)

    def mutate(self, individual): 
        if np.random.rand() < self.mutation_rate:
            mutation = np.random.randint(self.action_dim)
            individual = np.copy(individual)
            individual[mutation] = np.random.rand()
        return individual

    def crossover(self, parent1, parent2): 
        if np.random.rand() < self.crossover_rate:
            crossover_point = np.random.randint(self.action_dim)
            child1 = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            child2 = np.concatenate((parent2[:crossover_point], parent1[crossover_point:]))
            return child1, child2
        return parent1, parent2

    def select_new_population(self, population, rewards): 
        indices = np.argsort(rewards)[::-1]
        return population[indices[:self.population_size]]

    def update_history(self, best_individual): 
        self.history.append(best_individual)
        if len(self.history) > self.population_size:
            self.history.pop(0)




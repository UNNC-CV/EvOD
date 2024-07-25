import pickle
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.distributions import Categorical
import matplotlib.pyplot as plt
import numpy as np 
import json
import numpy as np
import random
import numpy as np 
from patch import PatchInfo,get
init,result = get()
random.seed(1)

EPISODES = 1000
lr = 0.001
gamma = 0.98
lmbda = 0.95
epochs = 3
eps_clip = 0.2
MAX_STEPS = 2835
action_dim = 50


def main():
    evolution_strategy = EvolutionaryStrategy(
    population_size=50,  
    mutation_rate=0.1,   
    crossover_rate=0.5,  
    action_dim=action_dim  
    )
    env = Env()  
    env.reset()
    model = PPO(len(env.obsevation),action_dim) 
    model.train()
    n_epi =0
    rewards = []
    ys = []
    ys2 = []
    xs = []
    while(1):
        n_epi +=1
        s = env.reset() # observation
        done = False
        t = 0
        while(done != True):
            t = t+1 
            prob = model.pi(torch.from_numpy(s).float() )
            prob = prob.view(-1)
            try:
                m = Categorical(prob)
            except:
                exit()
            action = m.sample().item()
            # action = 1
            population = evolution_strategy.initialize_population(action)
            for _ in range(10): 
                offspring = [evolution_strategy.mutate(ind) for ind in population]
                parents = np.random.choice(range(len(population)), size=(len(offspring), 2), replace=False)
                children = [evolution_strategy.crossover(population[p[0]], population[p[1]]) for p in parents]
                offspring.extend(children)
                offspring = np.array(offspring)
 
                rewards = []
                for individual in offspring:
                    action = np.random.choice(len(individual), p=individual)
                    _, reward, _ = env.step(action)
                    rewards.append(reward)
                rewards = np.array(rewards)
 
                population = evolution_strategy.select_new_population(offspring, rewards)
 
            best_individual = population[0]
            evolution_strategy.update_history(best_individual)
            next_s, r, done = env.step(best_individual)
            rewards.append(r)  
            s = next_s
            if done:
                break
        print("# of episode :{} steps :{} reward : {}".format(n_epi,t,r)) 
        model.train_net()
        ys.append(sum([r>0 for r in rewards])/n_epi)
        ys2.append(sum([r>=0 for r in rewards])/n_epi)
        xs.append(n_epi)
        if  n_epi% 100 == 0:
            if (ys[-1] >= ys[-2] and ys2[-1] >= ys2[-2]):
                model_name = './model/tr' + '.pkl'
                pickle.dump(model, open(model_name, 'wb')) 
                
            elif n_epi%1000 == 0:
                model_name = './model/tr' +str(n_epi)+ '.pkl'
                pickle.dump(model, open(model_name, 'wb')) 
            plt.clf() 
            plt.plot(xs,ys)
            plt.plot(xs,ys2)
            # plt.savefig("./figtrbase"+ '.jpg' )
    env.close()

if __name__ == "__main__":
    main()

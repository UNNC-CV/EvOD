class PPO(nn.Module):
    def __init__(self,input_size,action_num):
        super(PPO, self).__init__()
        self.data = []
        
        self.fc1   = nn.Linear(input_size,128)
        self.fc2  = nn.Linear(128,64)
        self.fc_pi = nn.Linear(64,action_num)
        self.fc_v  = nn.Linear(64,1)
        self.optimizer = optim.Adam(self.parameters(), lr=lr)


    def pi(self, x , softmax_dim=0):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x)) 
        x = self.fc_pi(x)
        prob = F.softmax(x, dim=softmax_dim)
        return prob 
    
    def v(self, x):
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x)) 
        v = self.fc_v(x)
        return v

    def put_data(self, transition):
        self.data.append(transition)

    def make_batch(self):
        s_lst, a_lst, r_lst, next_s_lst, prob_a_lst, done_lst = [], [], [], [], [], []
        for t in self.data:
            s, a, r, next_s, prob_a, done = t
            s_lst.append(s)
            a_lst.append([a])
            r_lst.append([r])
            next_s_lst.append(next_s)
            prob_a_lst.append([prob_a])  # prob_a 是一个list
            done_mask = 0 if done else 1  # 二值化
            done_lst.append([done_mask])
        s, a, r, next_s, done_mask, prob_a = torch.tensor(s_lst, dtype=torch.float), torch.tensor(a_lst), \
                                             torch.tensor(r_lst), torch.tensor(next_s_lst, dtype=torch.float), \
                                             torch.tensor(done_lst, dtype=torch.float), torch.tensor(prob_a_lst)
        self.data = []
        return s, a, r, next_s, done_mask, prob_a
        


    def train_net(self):
        s, a, r, next_s, done_mask, prob_a = self.make_batch()

        for i in range(epochs):
            td_target = r + gamma * self.v(next_s) * done_mask
            delta = td_target - self.v(s)  
            delta = delta.detach().numpy()       

            advantage_lst = []
            advantage = 0.0
            for delta_t in delta[::-1]:
                advantage = gamma * lmbda * advantage + delta_t[0]   # gae
                advantage_lst.append(advantage)
            advantage_lst.reverse()
            advantage = torch.tensor(advantage_lst, dtype=torch.float)

            pi = self.pi(s, softmax_dim=1)
            pi_a = pi.gather(1, a)  
            ratio = torch.exp(torch.log(pi_a) - torch.log(prob_a))  # a/b == exp(log(a)-log(b))

            surr1 = ratio * advantage
            surr2 = torch.clamp(surr1, 1 - eps_clip, 1 + eps_clip) * advantage
            loss = -torch.min(surr1, surr2).mean() + F.mse_loss(self.v(s), td_target.detach())
                         
            self.optimizer.zero_grad()
            loss.mean().backward()
            self.optimizer.step()

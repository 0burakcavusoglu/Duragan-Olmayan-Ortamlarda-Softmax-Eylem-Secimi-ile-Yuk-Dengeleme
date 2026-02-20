import numpy as np
import matplotlib.pyplot as plt


import numpy as np
import matplotlib.pyplot as plt

class LoadBalancerSim:
    def __init__(self, k=5, steps=1000, tau=0.1, alpha=0.1):
        self.k = k
        self.steps = steps
        self.tau = tau      # Sıcaklık parametresi
        self.alpha = alpha  # Öğrenme oranı (step-size)
        
        # Sunucuların başlangıç ortalama gecikmeleri (ms)
        self.true_latencies = np.array([50, 70, 40, 90, 60], dtype=float)
        self.q_estimates = np.zeros(k) # Tahmin edilen ödüller (1/latency)

    def get_reward(self, server_idx):
        # Gürültülü ve değişken gecikme simülasyonu
        noise = np.random.normal(0, 5) 
        latency = self.true_latencies[server_idx] + noise
        
        # Non-stationary: Her adımda sunucu performansları rastgele biraz değişir
        self.true_latencies += np.random.normal(0, 0.1, self.k)
        
        return 1.0 / max(latency, 1), latency

    def softmax_select(self):
        # Softmax formülü: P(a) = exp(Q(a)/tau) / sum(exp(Q(i)/tau))
        exp_q = np.exp(self.q_estimates / self.tau)
        probs = exp_q / np.sum(exp_q)
        return np.random.choice(self.k, p=probs)

    def run(self, strategy="softmax"):
        rewards = []
        total_latencies = []
        
        for i in range(self.steps):
            if strategy == "softmax":
                idx = self.softmax_select()
            elif strategy == "round-robin":
                idx = i % self.k
            else: # Random
                idx = np.random.choice(self.k)
                
            reward, lat = self.get_reward(idx)
            
            # Değer Güncelleme (Incremental Update)
            self.q_estimates[idx] += self.alpha * (reward - self.q_estimates[idx])
            
            rewards.append(reward)
            total_latencies.append(lat)
            
        return np.cumsum(total_latencies) / (np.arange(self.steps) + 1)

# Simülasyonu çalıştır
sim_steps = 2000
soft = LoadBalancerSim(steps=sim_steps, tau=0.01).run("softmax")
rand = LoadBalancerSim(steps=sim_steps).run("random")
rr = LoadBalancerSim(steps=sim_steps).run("round-robin")

# Görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(soft, label='Softmax Selection')
plt.plot(rand, label='Random Selection')
plt.plot(rr, label='Round-Robin')
plt.xlabel('İstek Sayısı')
plt.ylabel('Ortalama Bekleme Süresi (ms)')
plt.title('Yük Dengeleme Algoritmaları Performans Analizi')
plt.legend()
plt.grid(True)
plt.show()



if __name__ == "__main__":
    print("Simülasyon başlatılıyor...")
    
    sim_steps = 2000
    # Farklı stratejileri çalıştır
    soft = LoadBalancerSim(steps=sim_steps, tau=0.01).run("softmax")
    rand = LoadBalancerSim(steps=sim_steps).run("random")
    rr = LoadBalancerSim(steps=sim_steps).run("round-robin")

    # Grafik Oluşturma
    plt.figure(figsize=(12, 7))
    plt.plot(soft, label='Softmax Selection (Zeki Yaklaşım)', linewidth=2)
    plt.plot(rand, label='Random Selection (Rastgele)', linestyle='--')
    plt.plot(rr, label='Round-Robin (Sıralı)', linestyle=':')
    
    plt.title('Sunucu Yük Dengeleme: Algoritma Analizi')
    plt.xlabel('Gelen İstek Sayısı')
    plt.ylabel('Ortalama Gecikme Süresi (ms)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    
    plt.show() 
    
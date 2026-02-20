

# Non-Stationary Load Balancing with Softmax Action Selection
Hazırlayan: Burak Çavuşoğlu  Yazılım Mühendisliği 3.sınıf Öğrencisi 5230505068                                     

Ders: Algoritma Analizi ve Tasarımı

Bu proje, **Algoritma Analizi ve Tasarımı** dersi kapsamında, dağıtık sistemlerde yük dengeleme (load balancing) problemini çözmek amacıyla geliştirilmiştir. Proje, klasik algoritmaların aksine, sunucu performanslarının zamanla değiştiği (**non-stationary**) senaryolarda **Softmax Action Selection** (Multi-Armed Bandit tabanlı) algoritmasının başarısını analiz eder.

#  Problem Tanımı
Bir dağıtık sistem mühendisi olarak, $K$ adet farklı sunucudan oluşan bir kümeye gelen istekleri dağıtmamız gerekmektedir. Sunucuların yanıt süreleri (latency) sabit değildir, gürültülüdür ve zamanla değişir. 

Amacımız:
* Toplam bekleme süresini (**latency**) minimize etmek.
* Toplam ödülü (**reward**) maximize eden bir istemci taraflı yük dengeleme mekanizması kurmak.



#  Kullanılan Algoritmalar

Projede üç farklı yaklaşım karşılaştırılmıştır:
1.  **Round-Robin:** Sunucuları sırayla seçer. Performans değişimlerine duyarsızdır.
2.  **Random Selection:** Sunucuları tamamen rastgele seçer.
3.  **Softmax Action Selection:** Sunucuların geçmiş performans verilerine (latency) dayanarak olasılıksal bir seçim yapar.

### Softmax Formülü
Seçim olasılığı $P_t(a)$ şu formülle hesaplanır:
$$P_t(a) = \frac{e^{Q_t(a) / \tau}}{\sum_{i=1}^{K} e^{Q_t(i) / \tau}}$$

* **$\tau$ (Temperature):** Keşif (exploration) ve faydalanma (exploitation) arasındaki dengeyi ayarlar.
* **$Q_t(a)$:** Sunucunun o ana kadar tahmin edilen performans değeridir ($1/latency$).


 Analiz ve Çıkarımlar

 Yapılan simülasyonlarda Softmax algoritmasının;Sunucu performanslarındaki dalgalanmalara hızlı uyum sağladığı,Statik olmayan (non-stationary) ortamlarda Round-Robin'den daha düşük ortalama gecikme sunduğu,$\tau$ parametresi optimize edildiğinde "en hızlı sunucuyu bulma" konusunda yüksek doğruluk oranına ulaştığı gözlemlenmiştir.





 

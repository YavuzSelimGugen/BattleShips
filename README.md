## Amiral Battı (Battle Ships)

Amiral Battı, çift kişilik oynanan, kullanıcıların, karelerden oluşan 10x10’luk bir
düzleme, dikeyde ya da yatayda herahangi bir kare grubuna birbirinden gizli bir
şekilde eklediği gemilerin koordinatlarını tahmin ederek batırmaya çalıştığı bir
oyundur.

Projemizde üç adet .py uzantılı dosya kullanılmıştır ve bunlardan iki tanesinde class
yapısı oluşturulmuştur. PlayerMap.py, Ship.py ve Main.py.

Main.py içinde sınıf yapılarında oluşturulan fonksiyonlar oyunun gerçekleşmesi için
kullanılmıştır.

PlayerMap.py içinde PlayerMap sınıfı bulunmaktadır. İçinde 10x10’luk oyun alanı
oluşturulur, gemiler yerleştirilir, düşman gemisine ateş edilir, ve rakip oyuncunun
tahminlerinin gözüktüğü ayrı bir harita daha içerir. Bunun sebebi, karşı tarafın
gemilerin koordinatlarını bilmeden tahmin yapması içindir.

Ship.py dosyası içinde Ship sınıfı bulunmaktadır. Bir gemide olması gereken
değişkenler __init__() fonksiyonunda yazılmıştır.

Main.py dosyası içinde kullanıcıdan gerekli inputlar aşağıda oynayış başlığında
bahsettiğimiz gibi alınırken, exception handling yapılmıştır. Hatalı girişlerde
tekrardan kullanıcıdan input istenmektedir.

**Oynayış**

Başlangıçta adlarını giren kullanıcılar sırayla gemilerinin yerlerini oyun alanınta x, y
koordinatlarını vererek tanımlar, aynı zamanda geminin kuzey, güney, doğu, batı
yönünde olmasına da karar verir. Böylece gemiler hem dikey hem de yatay bir
şekilde yerleştirilmiş olur.

Ardından sıra atış kısmına gelir, iki kullanıcı sırayla atışlarını yapar, kullanıcılardan
birinin haritasında gemi kalmayana dek bu şekilde devam eder, sonrasında kazanan
belli olur.

Ayrıca, kullanıcılar atış gerçekleştirdikten sonra, karşılarındaki harita güncellenir,
kaçırılan vuruşlar konsolda * ile gösterilirken, başarılı atışlar X ile gösterilir. Henüz
atış yapılmamış yerlerde is? bulunur.

**Dışarıdan alınan kodlar**
clear() ile time.sleep() fonksiyonlarını konsol ekranındaki karmaşıklığı önlemek için
dışarıdan aldık.


Örnek ekran görüntüleri:

1-
![Screenshot1](img/bs1.png)

### 2-

3- Üstteki inputlara göre yerleştirilen gemi, her bir parçası O olarak gösteriliyor.



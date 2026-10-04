# Goktug+

**Goktug+**, Türkçe sözdizimi ve komutları sunan; kaynak kodunu güvenli biçimde token düzeyinde dönüştürüp yerel çalışma zamanı dil motorunda çalıştıran bir programlama dili projesidir. Kaynak dosyalarının uzantısı `.tpg`, çalıştırıcısı `trp`, paket komutu `tpg`'dir.

> Goktug+ bağımsız bir Türkçe parser/VM değildir. Yerel dil motorunun grameri, nesne modeli ve standart kütüphaneleri kullanılır; Türkçe adlar lexer/tokenizer seviyesinde dönüştürülür. Bu mimari geniş uyumluluk sağlar ancak Türkçe karşılıkları eklenmiş her yapı, ayrı bir Goktug+ dil özelliği olduğu anlamına gelmez.

## Özellikler

- Yorum ve string sabitlerini bozmayan `tokenize` tabanlı sözcük dönüşümü.
- Türkçe anahtar sözcükler, sık kullanılan yerleşik adları ve seçilmiş standart modül/fonksiyon alias'ları.
- `.tpg` dosyalarını çalıştıran `trp`; sürüm, yardım ve programa argüman iletme desteği.
- Gerçek paket yükleme/kaldırma/güncelleme/listeleme işlemleri için `tpg` komutları.
- Yerel dil motorunun sınıflar, fonksiyonlar, decorator, generator, async, comprehension, type annotation, exception ve pattern matching gibi özelliklerine erişim.
- UTF-8 kaynak, Türkçe karakterli identifier'lar ve kaynak dosyası satır konumlu Türkçe hata raporları.
- Ek Python paketi gerektirmez; çalıştırmak için Python 3.10+ gerekir. Paket kurma komutları internet bağlantısı kullanır.

## Gereksinimler ve kurulum

Goktug+ 1.0.3, **3.10 veya üzeri** bir Python çalışma zamanı ister. Kaynak deposunda:

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
trp --version
tpg --help
```

Geliştirme testleri için:

```bash
python -m unittest discover -s tests -v
```

### Windows Setup Wizard

`installer/GoktugPlusSetup.exe` Windows için kullanıcı profiline kurulum sihirbazıdır. Önceki kurulum `Program Files` altındaysa Setup yeni sürümü otomatik olarak kullanıcı klasörüne yönlendirir ve eski PATH girdisini kaldırır; yönetici izni istemez. Kurucu önce mevcut Python 3.10+ ortamını kullanmaya çalışır. Uyumlu ortam bulunmazsa Python 3.14.8'in resmî Windows kurucusunu indirir, SHA-256 ve dijital imzasını doğrular ve çalışma ortamını yalnızca Goktug+ klasörüne kurar; diğer Python kurulumlarına, başlatıcıya veya Python'un PATH ayarlarına dokunmaz. `trp`/`tpg` komutları için Goktug+ klasörü kullanıcı PATH'ine eklenir. İlk indirme için internet bağlantısı gerekir. Kurucu ayrıca `.tpg` dosyalarının açıklamasını **Goktug+ Kaynak Dosyası** olarak kaydeder ve özel kırmızı X simgesi atar. Kurulumdan sonra `.tpg` dosyasına çift tıklamak, o dosyanın klasöründe CMD açıp `trp dosya.tpg` komutunu çalıştırır; konsol sonuçları görebilmeniz için açık kalır. Türkçe çalışma hataları kaynak dosyasının satırını gösterir; kullanıcı kesintisi İngilizce traceback olmadan bildirilir. Kaldırıcı uygulamanın bilinen dosyalarını siler; kurulum klasörüne eklediğiniz diğer dosyaları, özel Python ortamına sonradan eklediğiniz paketleri ve değiştirdiğiniz runtime dosyalarını korur. Önceki `.tpg` ilişkilendirmesini de geri yükler; korunmuş dosyalar varsa kurulum klasörü kalabilir.

Setup dosyasının özelliklerinde ve Windows yüklü uygulamalar listesinde yayımlayıcı bilgisi **Goktug Software** olarak görünür. Bu, kod imzası değildir: EXE dijital olarak imzalanmadığından Windows SmartScreen yine uyarı gösterebilir. Microsoft'a göre doğrulanmış yayımlayıcı için sertifika gerekir; yeni imzalı dosyalarda da SmartScreen itibarı oluşana kadar uyarı görülebilir. Kurulum kaydı **Ayarlar → Uygulamalar → Yüklü uygulamalar** bölümündedir.

Kurulum sihirbazının NSIS kaynakları `installer/` altındadır. NSIS kurulu bir geliştirici makinesinde Windows: `installer\build_windows_setup.bat`; Linux: `./installer/build_windows_setup.sh` komutlarıyla yeniden derlenebilir.

## İlk program

`merhaba.tpg`:

```text
isim = "Dünya"
yazdir("Merhaba", isim)
```

Çalıştırma:

```bash
trp merhaba.tpg
```

Beklenen çıktı:

```text
Merhaba Dünya
```

Örneklerin tümü `examples/` dizinindedir. Örneğin hesap makinesini `trp examples/hesap_makinesi.tpg`, factorial örneğini `trp examples/hesaplama.tpg` komutuyla çalıştırabilirsiniz.

## Sözdizimi

Goktug+ girintiye duyarlı sözdizimi kullanır. Türkçe adlar yalnızca kod tokenlarında eşlenir; tırnak içindeki metinler ve yorumlar değiştirilmez.

```text
sayi = 10
eger sayi > 5:
    yazdir("Sayı 5'ten büyük")
degilse:
    yazdir("Sayı 5 veya daha küçük")

fonksiyon topla(a, b):
    dondur a + b

sonuc = topla(10, 20)
```

Türkçe karakterlerle isim tanımlanabilir:

```text
öğrenci = "Çağrı"
yazdir(öğrenci)
```

### Anahtar sözcükler

| Goktug+ | Yerel karşılığı | Goktug+ | Yerel karşılığı |
|---|---|---|---|
| `eger` | `if` | `degilseeger` | `elif` |
| `degilse` | `else` | `icin` | `for` |
| `iken` | `while` | `icinde` | `in` |
| `degil` | `not` | `ve` | `and` |
| `veya` | `or` | `Dogru` | `True` |
| `Yanlis` | `False` | `Hic` | `None` |
| `fonksiyon` | `def` | `dondur` | `return` |
| `sinif` | `class` | `iceaktar` | `import` |
| `den` | `from` | `olarak` | `as` |
| `dene` | `try` | `hata_yakala` | `except` |
| `sonunda` | `finally` | `hata_olustur` | `raise` |
| `gec` | `pass` | `dur` | `break` |
| `devam` | `continue` | `uret` | `yield` |
| `asenkron` | `async` | `bekle` | `await` |
| `ile` | `with` | `dogrula` | `assert` |
| `sil` | `del` | `genel` | `global` |
| `yerel_olmayan` | `nonlocal` | `ayni` | `is` |
| `kendim` | `self` | | |
| `islev` | `lambda` | `eslestir` | `match` |
| `eslesme` | `case` | | |

`lambda`, `match` ve `case` yapılarının hem yerel yazımı hem tabloda belirtilen Türkçe alias'ları kullanılabilir. `match`/`case`, kullanılan çalışma zamanı sürümü tarafından desteklenmelidir.

### Türkçe yerleşik adlar

| Goktug+ | Yerel karşılığı | Goktug+ | Yerel karşılığı |
|---|---|---|---|
| `yazdir` | `print` | `girdi` | `input` |
| `aralik` | `range` | `uzunluk` | `len` |
| `tip` | `type` | `donustur` | `str` |
| `tamsayi` | `int` | `ondalik` | `float` |
| `liste` | `list` | `demet` | `tuple` |
| `sozluk` | `dict` | `kume` | `set` |
| `mantiksal` | `bool` | `mutlak` | `abs` |
| `en_buyuk` | `max` | `en_kucuk` | `min` |
| `toplam` | `sum` | `sirala` | `sorted` |
| `ters` | `reversed` | `say` | `enumerate` |
| `birlesik` | `zip` | `herhangi` | `any` |
| `tum` | `all` | `ac` | `open` |
| `super_sinif` | `super` | `ozellik` | `property` |
| `statik_yontem` | `staticmethod` | `sinif_yontem` | `classmethod` |
| `isinstance_mi` | `isinstance` | `alt_sinif_mi` | `issubclass` |
| `derle` | `compile` | `degerlendir` | `eval` |
| `calistir` | `exec` | `istisna` | `Exception` |

Ek alias'lar arasında `bayt`, `bayt_dizisi`, `karmasik`, `sabit_kume`, `bellek_gorunumu`, `dilim`, `yineleyici`, `sonraki`, `esle_her_birine`, `suz`, `temsili`, `ascii_gosterim`, `ikili_yazim`, `sekizlik_yazim`, `onaltilik_yazim`, `cagrilabilir_mi`, `adlar`, `ozellik_al`, `ozellik_ata`, `ozellik_var_mi`, `ozellik_sil`, `degiskenler`, `genel_degiskenler`, `yerel_degiskenler` ve `duraklat` bulunur. Yerel yerleşik adlarının tamamı da kullanılabilir; alias'lar aynı zamanda ayrılmış isimlerdir. Örneğin `uzunluk` adlı kendi fonksiyonunuzu tanımlarsanız çağrıları yine yerleşik `len` adına çevrilecektir. Tam liste `src/goktug/mappings.py` içindedir.

### Fonksiyonlar ve sınıflar

```text
fonksiyon faktoriyel(n):
    eger n <= 1:
        dondur 1
    dondur n * faktoriyel(n - 1)

sinif Kisi:
    fonksiyon __init__(kendim, ad):
        kendim.ad = ad
```

Python uyumlu parametreler, varsayılan değerler, `*args`, `**kwargs`, annotation, decorator, miras ve magic method adları desteklenir. Magic method'lar (`__init__` gibi) aynen yazılır.

### Döngüler ve koleksiyonlar

```text
icin i icinde aralik(5):
    yazdir(i)

kareler = [x * x icin x icinde aralik(6)]
```

List/set/dict comprehension, tuple, dictionary, set, lambda, generator ve iterator özellikleri yerel gramer üzerinden çalışır.

### Hata yönetimi ve dosyalar

```text
dene:
    sonuc = 10 / 0
hata_yakala ZeroDivisionError olarak hata:
    yazdir("İşlem başarısız:", hata)
sonunda:
    yazdir("Bitti")

ile ac("veri.txt", "r", encoding="utf-8") olarak dosya:
    icerik = dosya.read()
```

Hatalar mümkün olduğunca Türkçe ad ve `.tpg` konumuyla gösterilir; ham traceback gösterilmez. Python seviyesindeki her hata mesajının tüm ayrıntıları Türkçeleştirilmiş değildir.

### Modüller ve standart kütüphane

Seçilmiş Türkçe modül alias'ları ve fonksiyon/özellik adları mevcuttur:

```text
iceaktar matematik
sonuc = matematik.karekok(25)
yazdir(sonuc)
```

Modül eşlemeleri: `matematik` → `math`, `rastgele` → `random`, `zaman` → `time`, `tarih` → `datetime`, `isletim` → `os`, `sistem` → `sys`, `yol` → `pathlib`, `duzenli_ifade` → `re`, `istatistik` → `statistics`, `koleksiyonlar` → `collections`, `is_parcalari` → `threading`, `surecler` → `multiprocessing`, `alt_surec` → `subprocess`, `soket` → `socket`, `asenkron_io` → `asyncio`, `veri_siniflari` → `dataclasses` ve diğerleri. Tam liste `src/goktug/mappings.py` dosyasındadır.

Eşlemeye alınmamış standart modüller ve üçüncü parti paketler yerel adlarıyla import edilebilir. Bazı Türkçe fonksiyon alias'ları tüm modüllerde aynı ismi dönüştürdüğünden çakışma olasılığı vardır; karışıklıkta modülün yerel fonksiyon adını kullanın.

## `trp` çalıştırıcısı

```bash
trp program.tpg
trp --version
trp --help
trp program.tpg arg1 arg2
```

`trp`, kaynak dosyasının dizinini import arama yoluna ekler, `sys.argv` değerini programa göre ayarlar ve çalıştırma sonunda geri yükler. Bu ilk sürüm doğrudan dosya çalıştırmayı hedefler; paketleme/derleme seçenekleri sunmaz.

## `tpg` paket komutları

```bash
tpg yukle requests
tpg kaldir requests
tpg guncelle requests
tpg liste
tpg --help
```

Komutlar **Goktug+ kurulumunun yapıldığı aynı ortamda** paket işlemi yapar ve gerçek paket yöneticisini çağırır. Bir sanal ortam kullanmak tavsiye edilir. `tpg guncelle paket` yalnızca belirtilen paketi günceller; tüm paketleri güncelleme işlemi bilerek yapılmaz.

## Mimari

1. `.tpg` metni UTF-8 olarak okunur.
2. Standart tokenizer metni tokenlara ayırır.
3. Yalnızca `NAME` tokenlarının eşlemeleri yapılır; yorum ve stringler aynı kalır.
4. Token akışı çalışma zamanı derleyicisine aktarılır. Python AST'si/grameri ve çalışma zamanı özellikleri böylece yeniden uygulanmaz.
5. Oluşan program `.tpg` dosya adıyla derlenir ve çalıştırılır; böylece hata satırı kaynak dosyasına işaret eder.

Dizinler: `src/goktug/` runtime, tokenizer dönüşümü, CLI, hata eşlemeleri ve paket komutları; `tests/` otomatik testler; `examples/` çalıştırılabilir programlar.

## Testler

```bash
python -m unittest discover -s tests -v
```

Testler token dönüşümünü, string/yorum korumasını, Unicode identifier'ları, kontrol akışını, recursion, sınıf/miras, comprehension, generator, exception, annotation/decorator, async/await, pattern matching, CLI ve Türkçe hata/konum bildirimini doğrular.

## Geliştirici rehberi ve katkı

1. Depoyu klonlayıp sanal ortam oluşturun ve `python -m pip install -e .` ile kurun.
2. Değişiklik için regresyon testi ekleyin; tüm testleri çalıştırın.
3. Token dönüşümünde metin üzerinde global değiştirme kullanmayın. Söz dizimi veya reserved alias değişikliği README ve testlere birlikte yansıtılmalıdır.
4. Hata raporlarının kaynak konumunu ve Türkçe kullanıcı deneyimini koruyun.
5. Değişiklikleri küçük, açıklayıcı commit'lerle gönderin.

Proje MIT lisanslıdır; lisans metni `LICENSE` dosyasındadır.

## Bilinen uyumluluk sınırları

- Bu sürüm ayrı bir Goktug+ parser/AST, bytecode formatı veya VM değildir. Üst düzeyde yerel gramer geçerlidir; yerel dil sürümüne göre farklılık gösterebilir.
- Alias dönüşümü bağlama duyarlı bir parser değil, token adı tabanlıdır. Bu nedenle eşlenmiş bir Türkçe yazım, aynı yazımı kullanan değişken/özellik adını da dönüştürür. Örneğin `liste` alias'ı `list` ile çakışır. Alias'ları özel isimler gibi ele alın.
- Modül ve attribute alias'ları küçük, elle seçilmiş bir listedir; bütün standart kütüphane API'si çevrilmiş değildir. Paket isimleri, fonksiyon imzaları, dokümantasyon ve üçüncü parti API'leri otomatik yerelleştirilmez.
- Hata sınıflarının yaygın olanları Türkçeleştirilir. Kaynak satırı korunur; sütun eşlemesi token uzunluğu değişimlerinde her durumda birebir olmayabilir.
- Güvenilmeyen `.tpg` kodu için sandbox değildir. Kod, kurulu ortamın normal izinleriyle çalışır; `eval`, dosya/ağ/işletim sistemi erişimleri kısıtlanmaz.
- Paket yöneticisi mevcut kurulum ortamını etkiler; proje/sanal ortam kullanın. Paket kurmak için ağ erişimi gerekebilir.
- Sınırsız “Python'daki her şey” uyumluluğu garanti edilmez. Hedef, dönüşüm yapılmayan sözdizimi için yerel dil özelliklerinden olabildiğince yararlanmaktır.

## Yol haritası

1. Sürümleme ve uyumluluk tablosunu CI ortamlarında farklı çalışma zamanı sürümleriyle genişletmek.
2. Import ve alias dönüşümlerini AST bağlam bilgisiyle daha hassas yapmak.
3. Daha geniş yerelleştirilmiş standart kütüphane katmanı ve tanılama kataloğu eklemek.
4. İsteğe bağlı biçimlendirici, linter ve paket proje metadata'sı geliştirmek.

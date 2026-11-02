# CS2 Technical Knowledge Base / Teknik Bilgi Arşivi

FRAGLITH'in CS2 eklenti, sunucu ve model geliştirme çalışmaları sırasında elde ettiği **genelleştirilmiş teknik notlar**.

> **Kapsam:** Bu arşiv; kişisel bilgiler, API anahtarları, bağlantı parolaları, sunucu adresleri, özel loglar, ticari kodlar, üçüncü kişilerin modelleri veya izin verilmeyen oyun varlıklarını içermez. Kodlar ve örnekler yeniden ve bağımsız yazılmalıdır.
>
> **Durum etiketleri:** **Log-backed** = önceki bir hata kaydında görüldü, her ortamda kesin çözüm olduğu anlamına gelmez. **Code-reviewed** = kaynakta/analizde sorun ve yaklaşım incelendi; canlı oyun testi yapılmamış olabilir. **Guidance** = önerilen iş akışı, kendi ortamında test edilmelidir. **Unresolved** = tamamlandığı doğrulanmayan konu.

| Konu | Bulgumuz / Öğrenim | Durum |
| --- | --- | --- |
| [CounterStrikeSharp DLL yükleme](css-plugin-load.md) | Bağımlılık çözümleme hatası için denetim sırası | Log-backed |
| [SteamCMD güncelleme ve depolama](steamcmd-storage.md) | `0x202` ile birlikte gelen `not enough disk space` satırının yorumu | Log-backed |
| [SwiftlyS2 / CSS göçü](framework-migration.md) | Eklentileri bire bir taşımak yerine bağımlılık ve yaşam döngüsünü uyarlama | Guidance |
| [Workshop içerik dağıtımı](workshop-deployment.md) | Yerelde çalışan modelin sunucuda niçin görünmeyebileceği | Guidance; server-side unresolved |
| [ModelDoc, AG2, VData](modeldoc-ag2-vdata.md) | Kaynak/derlenmiş asset, skeleton, world/view model ayrımı | Mixed; full AG2 port unresolved |
| [Oyun logu analizi](source2-logs.md) | Asset yükleme hatasını gerçek çökme belirtisinden ayırma | Log-backed |
| [Game mode eklenti tasarımı](plugin-architecture.md) | Timer, kredi ödemesi, thread, DB batch ve reload yaşam döngüsü | Code-reviewed; live unverified |
| [Spawn / takım doluluğu](spawn-capacity.md) | Harita spawn noktası ve takım kapasitesi için güvenli test planı | Guidance |
| [HUD ve yükleme ekranları](hud-loading.md) | Sunucu tarafından kontrol edilen UI ile istemci yükleme akışının sınırı | Guidance |
| [Güvenli log paylaşımı](../../tools/README.md) | Yerel log tarama ve sansürleme aracı | New example; not a game plugin |

## Şeffaflık

**Bir araç veya modelde sadece yerel görüntüleme başarılıysa, 'dedicated server'da çalışıyor' demiyoruz.** VData/AG2, custom weapon/equip ve Workshop dağıtımına ilişkin bazı konular çözülmeden kaldı. Bkz. [Open questions](OPEN-QUESTIONS.md).

### Contribute

Bu rehberlerin yanlış veya eski kalan yerlerini [Issue](https://github.com/HiztroFFM/FRAGLITH-Open-Source/issues) üzerinden sürüm ve log içermeyen örnekle düzeltebilirsin.

**Discord:** https://discord.gg/Aq8NgGswN

# Bab 8: Domain 5 (Bagian 1) — Keamanan Informasi, Kontrol Fisik, IAM & Biometrik, dan Keamanan Jaringan (Bobot 27%)

> **Cakupan Materi:** Bab ini membahas separuh pertama **Domain 5 CISA (Protection of Information Assets — 27% / ~40 soal, Domain Terbesar dalam Ujian CISA!)** yang mencakup Trias **CIA**, Peran Kepemilikan Data (**Data Owner vs. Custodian**), Keamanan Fisik & Lingkungan (*Mantrap*, Pemadam Api **FM-200 / Dry-Pipe**, UPS), **Identity & Access Management (IAM)** (*MAC, DAC, RBAC, ABAC*, Biometrik **FAR / FRR / CER**, **SSO Kerberos / SAML**), serta Keamanan Jaringan (**Model OSI 7 Layer**, **Firewall**, Arsitektur **DMZ**, **IDS vs. IPS**, **VPN IPsec/TLS**, Keamanan Nirkabel **WPA2/WPA3**, Virtualisasi, Cloud, BYOD/MDM, dan DLP).

---

## 8.1 Trias Keamanan Informasi (CIA Triad), Privasi, dan Kepemilikan Data

### A. Tiga Pilar Utama Keamanan Informasi (CIA Triad)
1. **Confidentiality (Kerahasiaan):** Memastikan informasi hanya dapat diakses oleh pihak yang berwenang (*authorized entities*). Dilindungi dengan: **Enkripsi (AES/TLS)**, **Access Control Lists (ACL)**, dan **Klasifikasi Data**.
2. **Integrity (Integritas):** Memastikan akurasi, kelengkapan, dan keaslian informasi serta melindungi data dari modifikasi tanpa otorisasi baik secara sengaja maupun tidak sengaja. Dilindungi dengan: **Hashing (SHA-256/512)**, **Digital Signatures**, **Input Validation / Check Digit**, dan **Segregation of Duties (SoD)**.
3. **Availability (Ketersediaan):** Memastikan informasi dan sistem selalu dapat diakses oleh pengguna yang berwenang pada saat dibutuhkan. Dilindungi dengan: **Redundansi (RAID, Clustering, Load Balancing)**, **Backup & DRP**, serta **Anti-DDoS**.

### B. Perbandingan Data Owner vs. Data Custodian vs. Security Administrator

| Peran Tata Kelola Data | Siapa yang Menjabat? | Tanggung Jawab Utama & Akuntabilitas CISA |
| :--- | :--- | :--- |
| **Data / Information Owner** *(Pemilik Data)* | **Manajer Senior Unit Bisnis** (misal: Direktur HRD untuk data gaji; Direktur Keuangan untuk data GL — **BUKAN CIO/Kepala TI!**). | • **Menentukan tingkat klasifikasi data** (*Public, Internal, Confidential, Restricted*).<br>• **Mengotorisasi / menyetujui secara tertulis pemberian dan pencabutan hak akses pengguna** terhadap data tersebut.<br>• Melakukan peninjauan ulang hak akses (*User Access Review* / UAR) secara berkala dan memikul akuntabilitas tertinggi atas perlindungan data. |
| **Data Custodian** *(Kustodian / Penjaga Data)* | **Departemen TI / Operasi Pusat Data / DBA / SysAdmin**. | • Mengimplementasikan kontrol teknis harian sesuai aturan yang ditetapkan oleh *Data Owner* (melakukan *backup* rutin, memelihara server, menerapkan enkripsi, menjaga ketersediaan database). |
| **Security Administrator** *(Administrator Keamanan)* | **Staf Keamanan TI**. | • Mengeksekusi pembuatan, pengubahan, atau penghapusan *user ID* dan profil akses di dalam sistem **HANYA SETELAH menerima persetujuan tertulis dari Data Owner**. |
| **Data Controller vs. Data Processor** *(Privasi / GDPR / UU PDP)* | **Organisasi Pemilik vs. Vendor Pemroses** | • **Data Controller:** Entitas yang menentukan **tujuan (*why*) dan cara (*how*)** pemrosesan data pribadi.<br>• **Data Processor:** Pihak ketiga (misal vendor *Cloud/Payroll*) yang memproses data pribadi **atas nama dan sesuai instruksi Data Controller**. |

---

## 8.2 Kontrol Keamanan Fisik dan Lingkungan (Physical & Environmental Controls)

### A. Kontrol Akses Fisik Pusat Data (Data Center Physical Security)
- **Lokasi Gedung:** Pusat data tidak boleh memasang papan nama mencolok di luar gedung; ruang server sebaiknya ditempatkan di lantai tengah gedung (menghindari banjir di ruang bawah tanah dan meminimalkan akses paksa dari lantai dasar/atap) serta tidak memiliki jendela kaca eksternal.
- **Mantrap / Deadman Door (Pintu Ganda Interlock):** Ruang antara kecil dengan **dua pintu terkunci elektronik** di mana pintu kedua baru bisa terbuka setelah pintu pertama tertutup rapat dan identitas pengunjung terverifikasi (kontrol **paling efektif untuk mencegah *Piggybacking / Tailgating***!).
- **Visitor Log & Escort:** Seluruh tamu/teknisi vendor wajib menyerahkan identitas, dicatat dalam *Visitor Log* (fisik/elektronik), mengenakan *badge* tamu yang mencolok, dan **dikawal secara fisik (*physically escorted*) sepanjang waktu** di dalam ruang server.

### B. Kontrol Lingkungan: Pemadam Kebakaran & Listrik Cadangan

| Komponen Lingkungan | Jenis Teknologi | Cara Kerja & Standar Rekomendasi CISA |
| :--- | :--- | :--- |
| **Sistem Deteksi Api** | **Ionization / Photoelectric Smoke Detector under Raised Floor** | Detektor asap wajib dipasang baik di plafon atas maupun **di bawah lantai panggung (*under the raised floor*)** tempat jalur kabel listrik melintas. |
| **Sistem Pemadam Api Air** | **Dry-Pipe vs. Wet-Pipe Sprinkler** | • **Wet-Pipe (Pipa Basah):** Pipa selalu berisi air bertekanan $\rightarrow$ **DILARANG untuk ruang server** karena jika pipa bocor atau terpicu tidak sengaja, air langsung menghancurkan perangkat keras!<br>• **Dry-Pipe / Pre-Action System (Pipa Kering):** Pipa hanya berisi udara bertekanan; katup air baru terbuka jika **detektor asap/panas mengonfirmasi kebakaran nyata** (*dual-trigger*), sehingga mencegah kebocoran air tidak sengaja. |
| **Sistem Pemadam Api Gas Bersih (Paling Direkomendasikan!)** | **FM-200 / Inergen / Novec 1230** *(Pengganti Gas Halon)* | • **Gas Halon:** Sangat efektif memadamkan api peralatan elektronik, namun **DILARANG secara internasional (Protokol Montreal)** karena **merusak lapisan ozon (CFC)** dan berbahaya bagi pernapasan manusia.<br>• **FM-200 / Inergen / Novec 1230:** Gas bersih (*clean agent*) yang memadamkan api secara kimiawi/mengurangi oksigen tanpa meninggalkan residu cair, **tidak merusak server elektronik**, dan **tidak merusak lapisan ozon**. |
| **Perlindungan Listrik** | **UPS (Uninterruptible Power Supply) + Diesel Generator** | • **UPS (Baterai):** Memberikan daya instan saat listrik PLN padam (**mencegah lonjakan/*surge*, *sag*, *brownout*, dan *blackout* singkat**) selama beberapa menit agar **Generator Diesel** sempat menyala dan stabil, atau agar server dapat melakukan **Graceful Shutdown** tanpa korupsi database. |
| **Kontrol Suhu & Kelembapan** | **CRAC / HVAC (Kelembapan $40\% - 60\%$)** | • Jika kelembapan **terlalu rendah ($< 30\%$ / terlalu kering)** $\rightarrow$ memicu **listrik statis (*static electricity*)** yang menghancurkan *microchip*.<br>• Jika kelembapan **terlalu tinggi ($> 60\%$ / terlalu lembap)** $\rightarrow$ memicu **kondensasi air dan korosi/karat** pada komponen sirkuit. |
| **Emergency Power-Off (EPO)** | **Tombol EPO dengan Penutup Pelindung** | Dipasang di dekat pintu keluar darurat untuk memutus seluruh aliran listrik saat kebakaran/sengatan listrik; wajib diberi **penutup kaca/plastik pelindung (*protective cover*)** agar tidak tertekan secara tidak sengaja oleh staf yang lewat. |

---

## 8.3 Identity and Access Management (IAM), Biometrik, dan Single Sign-On (SSO)

### A. Empat Model Kontrol Akses Logis
1. **MAC (Mandatory Access Control):** Akses ditentukan secara kaku oleh sistem berdasarkan label klasifikasi keamanan objek (*Top Secret, Secret*) dan izin keamanan (*clearance*) subjek. Pengguna tidak bisa mengubah izin file (umum di militer/pemerintahan).
2. **DAC (Discretionary Access Control):** Pemilik file/objek memiliki keleluasaan untuk memberikan hak akses (*read/write*) kepada pengguna lain. Fleksibel namun berisiko jika pengguna lalai.
3. **RBAC (Role-Based Access Control):** Hak akses dikelompokkan berdasarkan **Peran Jabatan (*Job Role*)** (misal: *Kasir*, *Analis Kredit*), bukan diberikan per individu secara langsung. Merupakan model **paling efisien untuk menegakkan *Least Privilege* dan *Segregation of Duties* (SoD)** pada perusahaan besar!
4. **ABAC (Attribute-Based Access Control):** Keputusan akses dievaluasi secara dinamis berdasarkan kombinasi atribut subjek, objek, tindakan, dan konteks lingkungan (misal: lokasi GPS, jam kerja, postur keamanan perangkat).

### B. Autentikasi Biometrik: FAR (Type II), FRR (Type I), dan CER/EER

Sistem biometrik (sidik jari, retina, iris, wajah, telapak tangan) memiliki dua jenis kesalahan statistik yang bergerak berlawanan arah saat sensitivitas sistem diubah:

```
Tingkat Kesalahan (%)
   ▲
   │  \                              /
   │   \  FRR (Type I Error)        /  FAR (Type II Error)
   │    \  (Menolak Orang Sah)     /  (Menerima Penyusup Palsu!)
   │     \                        /
   │      \          ●           /
   │       \      CER / EER     /
   │        \    (FAR = FRR)   /
   │         \      / \       /
   │          \    /   \     /
   │           \  /     \   /
   └────────────\/───────\─/────────────────────────► Tingkat Sensitivitas / Threshold
                         ▲
         (Untuk Ruang Server / Militer: Geser ke Kanan agar FAR = 0!)
```

| Metrik Biometrik | Nama Lain | Definisi Kesalahan | Dampak Bisnis / Keamanan |
| :--- | :---: | :--- | :--- |
| **FRR** *(False Rejection Rate)* | **Type I Error** | Sistem **menolak pengguna yang sah (*authorized user rejected*)**. | Mengganggu kenyamanan/produktivitas pengguna karena harus memindai ulang berkali-kali, namun **tidak membobol keamanan**. |
| **FAR** *(False Acceptance Rate)* | **Type II Error** *(Paling Berbahaya!)* | Sistem **menerima penyusup yang TIDAK sah (*unauthorized impostor accepted*)**. | **Pelanggaran Keamanan Fatal (*Critical Security Breach*)!** Untuk fasilitas sensitif (pusat data, brankas, militer), **FAR harus ditekan serendah mungkin** meskipun meningkatkan FRR! |
| **CER / EER** *(Crossover Error Rate / Equal Error Rate)* | Titik Potong $\text{FAR} = \text{FRR}$ | Titik persilangan di mana persentase **FAR sama dengan FRR** ($\text{FAR} = \text{FRR}$). | **Indikator Terbaik Kualitas Perangkat Biometrik:** Semakin **RENDAH nilai CER/EER**, semakin akurat dan unggul sistem biometrik tersebut (urutan akurasi tertinggi umumnya: **Retina / Iris $\rightarrow$ Sidik Jari / Vena Telapak $\rightarrow$ Wajah / Suara**). |

### C. Single Sign-On (SSO): Kerberos, SAML, dan OAuth/OIDC
- **Single Sign-On (SSO):** Memungkinkan pengguna cukup melakukan autentikasi **satu kali** untuk mengakses berbagai aplikasi yang terhubung.
  - **Keunggulan Utama SSO:** Pengguna tidak perlu menghafal banyak *password* (mencegah kebiasaan mencatat *password* di kertas *post-it*), administrasi pencabutan akses saat karyawan *resign* menjadi terpusat dan instan.
  - **Risiko Terbesar SSO (Single Point of Failure / "Keys to the Kingdom"):** Jika satu kredensial SSO berhasil dicuri oleh penyerang, penyerang langsung mendapatkan akses ke **seluruh aplikasi perusahaan**! Oleh karena itu, SSO **WAJIB dikombinasikan dengan Multi-Factor Authentication (MFA)**.
- **Arsitektur Kerberos:** Menggunakan **Key Distribution Center (KDC)** yang terdiri dari *Authentication Server (AS)* dan *Ticket-Granting Server (TGS)* untuk menerbitkan **Ticket-Granting Ticket (TGT)** dan *Service Ticket* berbasis kriptografi kunci simetris dan stempel waktu (*timestamp*). Kerentanan utama Kerberos adalah ketergantungan pada sinkronisasi jam sistem (*time synchronization*) dan perlindungan KDC sebagai *single point of failure*.

---

## 8.4 Keamanan Jaringan: Model OSI, Firewall, DMZ, IDS/IPS, VPN, dan Wireless

### A. Pemetaan Perangkat & Protokol pada 7 Lapisan Model OSI

| Layer OSI | Nama Layer | Satuan Data (PDU) | Protokol, Perangkat Jaringan, & Jenis Firewall |
| :---: | :--- | :---: | :--- |
| **Layer 7** | **Application** | Data / Message | HTTP/HTTPS, FTP, SMTP, DNS, SSH, Telnet; **Application-Level Gateway (Proxy Firewall)**, **WAF (Web Application Firewall)**. |
| **Layer 6** | **Presentation** | Data | Format data (ASCII, JPEG), kompresi, enkripsi tingkat aplikasi. |
| **Layer 5** | **Session** | Data | Pembukaan/penutupan sesi, NetBIOS, RPC; **Circuit-Level Gateway (SOCKS)**. |
| **Layer 4** | **Transport** | **Segment (TCP) / Datagram (UDP)** | **TCP** (*Connection-oriented, reliable, 3-way handshake*) vs. **UDP** (*Connectionless, fast/streaming*), TLS/SSL; **Stateful Inspection Firewall**. |
| **Layer 3** | **Network** | **Packet** | Pengalamatan logis **IP (IPv4/IPv6)**, **ICMP** (Ping), **IPsec**; perangkat **Router**; **Packet-Filtering Firewall**. |
| **Layer 2** | **Data Link** | **Frame** | Pengalamatan fisik **MAC Address**, ARP, **VLAN (802.1Q)**, PPP, L2TP; perangkat **Switch** & **Bridge**. |
| **Layer 1** | **Physical** | **Bits ($0/1$)** | Kabel UTP/Fiber Optic, gelombang radio; perangkat **Hub** & **Repeater**. |

### B. Perbandingan 4 Jenis Firewall & Arsitektur DMZ (Screened Subnet)

1. **Packet-Filtering Firewall (Layer 3/4 — Stateless):** Memeriksa *header* paket berdasarkan IP sumber/tujuan dan nomor *port* secara terpisah. Cepat namun mudah dikelabui oleh *IP spoofing* dan tidak memahami konteks sesi.
2. **Stateful Inspection Firewall (Layer 3/4/5):** Melacak status koneksi aktif dalam *State Table* (memastikan paket masuk merupakan balasan yang sah dari koneksi yang diminta dari dalam jaringan).
3. **Circuit-Level Gateway (Layer 5):** Memvalidasi sesi koneksi TCP/UDP (*handshake*) tanpa memeriksa isi paket aplikasi secara mendalam.
4. **Application-Level Gateway / Proxy Firewall / Next-Gen Firewall (Layer 7):** Bertindak sebagai perantara penuh yang memeriksa isi *payload* perintah aplikasi (misal memblokir perintah `HTTP POST` atau `FTP PUT` tertentu dan mencegah SQL Injection). Memberikan **keamanan tertinggi**, namun paling membebani kinerja/latensi.
5. **Arsitektur DMZ (Demilitarized Zone) — Screened Subnet:**
   - **JANGAN PERNAH** menempatkan **Database Server Produksi** yang berisi data sensitif di dalam zona **DMZ**!
   - Di dalam **DMZ** (yang dibatasi oleh *External Firewall* ke arah Internet dan *Internal Firewall* ke arah LAN Internal) hanya boleh ditempatkan **Web Server publik, Email Relay, atau DNS/Proxy Server**. Sementara **Database Server** wajib ditempatkan di **Jaringan Internal (Internal Protected Zone)** di belakang *Internal Firewall*!

### C. Perbandingan IDS (Intrusion Detection System) vs. IPS (Intrusion Prevention System)

| Karakteristik | IDS (Intrusion Detection System) | IPS (Intrusion Prevention System) |
| :--- | :--- | :--- |
| **Kategori Kontrol** | **Detective Control** *(Kontrol Detektif / Pasif)* | **Preventive & Corrective Control** *(Kontrol Preventif / Aktif)* |
| **Penempatan di Jaringan** | Dipasang di luar jalur utama (*Out-of-Band / Promiscuous Mode* melalui *SPAN port / Network Tap*). | Dipasang **langsung di jalur lalu lintas (*In-Line*)** seperti Firewall. |
| **Tindakan Saat Serangan** | Mengirim peringatan (*alert*) ke administrator/SIEM (dan opsional mengirim *TCP Reset*), tetapi paket pertama tetap lolos. | **Secara aktif memblokir dan menjatuhkan (*drop/block*) paket berbahaya secara *real-time* sebelum mencapai target!** |
| **Metode Deteksi** | • **Signature-Based (Statistical/Pattern):** Mencocokkan lalu lintas dengan database pola serangan yang sudah dikenal (efektif untuk serangan lama, **gagal mendeteksi serangan *Zero-Day***).<br>• **Anomaly-Based (Heuristic/Behavioral):** Membandingkan lalu lintas terhadap profil perilaku normal (*baseline*); mampu mendeteksi **serangan baru (*Zero-Day*)**, namun sering menghasilkan **False Positive** jika *baseline* berubah. | Menggabungkan *signature* dan *anomaly blocking*. Risiko utama IPS *In-Line*: Jika terjadi **False Positive**, IPS dapat **memblokir lalu lintas bisnis yang sah (*Self-Inflicted DoS*)**! |

### D. Honeypot, VPN, Wireless Security, Virtualization, dan Mobile/BYOD

- **Honeypot (Umpan Penyerang):** Sistem tiruan yang sengaja dibuat tampak menarik dan rentan di zona DMZ untuk **memancing penyerang menjauh dari server produksi nyata** serta mempelajari taktik penyerang. *(Aturan Hukum CISA: Honeypot hanya boleh digunakan untuk mengumpulkan intelijen pertahanan, **bukan untuk menjebak/membujuk (*entrapment*)** pihak yang awalnya tidak berniat menyerang).*
- **VPN (Virtual Private Network):** Membangun terowongan terenkripsi (*encrypted tunnel*) di atas jaringan publik (Internet) menggunakan **IPsec** (Layer 3 — *Tunnel Mode* mengenkripsi seluruh paket IP beserta *header* asli; *Transport Mode* hanya mengenkripsi *payload*) atau **TLS/SSL VPN** (Layer 4–7).
- **Wireless Security:** **WEP** sangat lemah dan dilarang; wajib menggunakan **WPA2-Enterprise / WPA3** dengan enkripsi **AES (CCMP)** dan autentikasi server **IEEE 802.1X / RADIUS (EAP-TLS)**. Menonaktifkan *SSID Broadcast* atau menggunakan *MAC Filtering* saja **bukanlah kontrol keamanan yang kuat** karena mudah disadap dan di-*spoof*!
- **Virtualization Risk:** Risiko paling kritis pada komputasi tervirtualisasi adalah kompromi pada lapisan **Hypervisor (*VM Escape*)** — jika penyerang berhasil mengambil alih *Hypervisor*, penyerang dapat menguasai seluruh *Virtual Machine (VM)* yang berjalan di atasnya!
- **BYOD (Bring Your Own Device) & MDM:** Mewajibkan instalasi **Mobile Device Management (MDM)** dengan fitur **Containerization** (memisahkan ruang penyimpanan data korporat dari data pribadi karyawan), enkripsi perangkat penuh, deteksi *jailbreak/rooting*, dan kemampuan **Remote Wipe (Selective Wipe)** untuk menghapus data perusahaan dari jarak jauh jika ponsel hilang/dicuri atau karyawan *resign*.

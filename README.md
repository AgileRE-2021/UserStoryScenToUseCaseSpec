# UserStoryScenToUseCaseSpec
> Generate dari User Stories Scenario ke Use Case Specification

[![Version](https://badge.fury.io/gh/tterb%2FHyde.svg)]()
[![GitHub Release](https://img.shields.io/badge/release-1.0-blue)]()

Repository ini merupakan Project milik Kelompok 2 dari kelas I2 Matakuliah Pembangunan Perangkat Lunak, dimana Project ini bertujuan dapat melakukan Generate dari User Story Scenario ke Use Case Specification

# Daftar Isi
* [Tentang Proyek](#tentang-proyek)
  * [Definisi](#definisi)
  * [Sistem Pembangun](#sistem-pembangun)
* [Petunjuk Instalasi](#petunjuk-instalasi)
* [Petunjuk Penggunaan](#petunjuk-penggunaan)
* [Informasi Lainnya](#informasi-lainnya)
  * [Anggota Proyek](#anggota-proyek)
  * [Tanggal Rilis](#tanggal-rilis)
  * [Kontak](#kontak)
* [Lisensi](#lisensi)

<!-- TENTANG PROYEK -->
# ✨ Tentang Proyek 
![logo](https://user-images.githubusercontent.com/77656059/123859443-db02c380-d94e-11eb-9076-c1e4374d3d8f.png)
### Definisi
USCG (*Use Case Specification Generator*) merupakan aplikasi yang bertujuan untuk mengubah User Stories Scenario menjadi Use Case Specification. Berikut adalah penjelasan dari masing-masing artefak yang dilibatkan dalam aplikasi ini. 
1. *User Stories Scenario* merupakan sebuah narasi yang menjelaskan urutan aktivitas yang dilakukan oleh user selama menggunakan aplikasi. User Stories Scenario mampu menggambarkan langkah-langkah, aksi atau tindakan pada kondisi tertentu tentang user saat berinteraksi dengan sebuah sistem.
2. *Use Case Specification* merupakan deskripsi singkat tentang langkah-langkah yang diperlukan untuk menggambarkan use case, lalu langkah-langkahnya dibuat untuk menambahkan lebih detail yang disebut dengan use case specification.

Secara garis besar, komponen pembentuk dari *User Stories Scenario* sebagai *output* yang dihasilkan terbentuk melalui komponen input, yaitu :
1. Use Case Name : Nama Use Case berdasarkan keperluan aktor.
2. Destination : Aktor yang menerima data dari sistem.
3. Description : Menggambarkan gambaran umum tentang fungsionalitas suatu proses yang didalamnya melibatkan sistem.
4. Initial Condition : Kondisi atau alternatif yang terjadi pada saat menjalankan suatu user stories.
5. Actor Action : Berisikan urutan aktivitas yang dilakukan oleh aktor untuk menjalankan proses yang ada pada sistem.
6. System Reaction : Berisikan urutan aktivitas yang dilakukan oleh sistem untuk menjalankan proses yang ada pada sistem.
7. Final condition : Kondisi akhir dari proses user stories.

Secara garis besar, komponen pembentuk dari *Use Case Specification* sebagai *output* yang dihasilkan terbentuk melalui komponen input, yaitu :
1. Use Case Name : Nama Use Case berdasarkan keperluan aktor.
2. Actor : Menggambarkan seseorang yang berinteraksi dengan sistem, dimana hanya bisa meng-input dan menerima informasi dari sistem.
3. Stakeholder Interests : Berisikan informasi tentang seseorang yang nantinya berkepentingan terhadap use case specification yang dibuat.
4. Pra-condition : Keadaan sistem yang diperlukan sebelum use case specification di mulai.
5. Scenario : Pesan atau tindakan yang dilakukan oleh sistem.
6. Alternative : Berisikan model use case specification.
7. Post-condition : Keadaan sistem yang diperlukan setelah use case specification di akhiri.

### Sistem Pembangun
Aplikasi Use Case Specification Generator dibangun dengan memanfaatkan *software*, *framework*, dan beberapa bahasa pemrograman, diantaranya adalah sebagai berikut :
- [VsCode Editor](https://code.visualstudio.com/)
- [SQLite Database](https://www.sqlite.org/index.html)
- [GitHub](https://github.com/)
- [Django Framework](https://www.djangoproject.com/) 
- [Bootstrap Framework](https://getbootstrap.com/)
- [Python](https://www.python.org/)
- [Javascript](javascript.com)

# 🚀 Petunjuk Instalasi 
Petunjuk mengenai prosedur instalasi untuk aplikasi dilakukan pada sesi terminal, berikut prosedur yang dapat dilakukan :
1. Lakukan *clone* pada repositori
   ```sh
   git clone https://github.com/AgileRE-2021/alamat.git
   ```
2. Masuk ke direktori/folder UserStoryScenario
   ```sh
   cd UserStoryScenario
   ```
3. Lakukan Installasi Django Framework
   ```sh
   py -m pip install Django  
   ```
4. Lakukan Installasi Semua Modul yang dibutuhkan
   ```sh
   pip install -r requirements.txt
   ```
5. Buat Migrasi untuk tabel pada database
   ```sh
   python manage.py makemigrations  
   ```
   ```sh
   python manage.py migrate
   ```
6. Proses Installasi Selesai
7. Jalankan Sistem/Run Server
   ```sh
   python manage.py runserver  
   ```
8. Akses Aplikasi pada local port melalui browser
   ```sh
   http://127.0.0.1:8000/ 
   ```

# 📖 Petunjuk Penggunaan
Petunjuk mengenai prosedur penggunaan aplikasi dapat dilihat pada bagian di bawah ini :
1. Klik "Create" apabila belum memiliki akun dan lakukan pembuatan akun
2. Input "Username" dan "Password" apabila telah memiliki akun, lalu klik "Login"
3. Untuk membuat project baru, input "Project Name" dan "Project Description" lalu klik "Submit"
4. Untuk membuat fitur baru, lihat pada bagian list project lalu klik "Detail"
5. Kemudian klik "Add Feature", input "Feature Name, Action, Actor, Feature Benefits", lalu klik "Add User Story Scenario Condition"
6. Untuk membuat User Story Scenario Condition, input "Scenario Name, Given, When, Then"
7. Untuk menambahkan User Story Scenario yang lain, maka scenario name akan menjadi "wrong password", kondisi pada scenario Then terbatas, sedangkan kondisi pada Given dan When dikumpulkan dari normal scenario atau skenario normal
8. Untuk melakukan generate dari User Story ke Use Case Specification, lihat pada halaman "Detail Project", lalu klik "Generate"

# 📌 Informasi Lainnya
### Anggota Proyek
Anggota pada proyek pengerjaan aplikasi *Use Case Specification Generator* terdiri dari 7 orang, meliputi :
1. Cerelia Devina Tantia V. N.
2. Luthfia Rachmawati
3. Hilmi Rafif Fajari
4. Pravadipta Riksadyani Pambudi
5. Muhammad Faisal Basuki
6. Boy Ardan Wiratama
7. Farhat		

### Tanggal Rilis 
Tanggal 7 Juli 2021

### Kontak 
Informasi kontak setiap anggota lebih detail dapat dilihat di bawah ini. 
1. Cerelia Devina Tantia V. N.    : cereliadevinaa@gmail.com
2. Luthfia Rachmawati             : luthfia.rachmawati@gmail.com
3. Hilmi Rafif Fajari             : hilmirf23@gmail.com
4. Pravadipta Riksadyani Pambudi  : riksadyani@gmail.com
5. Muhammad Faisal Basuki         : mfaisalbasuki@gmail.com
6. Boy Ardan Wiratama             : boyardan57@gmail.com
7. Farhat		                       : farhathmd0505@gmail.com

# 📝 Lisensi

Copyright © 2021 Universitas Airlangga

---
<br/>

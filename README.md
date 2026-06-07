# Student Stress Levels Classification

## 📌 Deskripsi

Proyek ini berfokus pada pemanfaatan pemodelan machine learning untuk mengklasifikasikan tingkat stres pada mahasiswa berdasarkan parameter akademik dan psikologis. Proses analisis dilakukan terhadap data masukan yang mencakup aspek kesehatan, hubungan sosial, capaian akademik, serta kondisi emosional mahasiswa. Hasil dari proyek ini dirancang sebagai alat bantu bagi pihak perguruan tinggi dalam memantau kondisi psikologis mahasiswa secara terukur untuk mempermudah pengambilan keputusan dan mendukung pengelolaan lingkungan kampus yang kondusif.

---

## 💾 Dataset

Dataset yang digunakan dalam proyek ini bersumber dari [Kaggle: Student Stress Monitoring Datasets](https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets). Data ini memuat hasil respons survei anonim dari 84 audiensi mahasiswa perguruan tinggi yang berada pada rentang usia 18 hingga 21 tahun. Pengumpulan data dilakukan menggunakan kuesioner skala Likert lima poin untuk memetakan pengalaman mahasiswa terkait tingkat stres, kondisi kesehatan, hubungan sosial, capaian akademik, serta kondisi emosional guna menganalisis korelasinya dengan performa belajar.

---

## 🛠️ Tech Stack

| Kategori                    | Teknologi yang Digunakan                                             |
| :-------------------------- | :------------------------------------------------------------------- |
| 🌐 **Programming Language** | `Python`                                                             |
| 🌱 **Environment**          | `Jupyter Notebook`                                                   |
| 🧩 **Framework**            | `Streamlit`                                                          |
| ⚛️ **Libraries**            | `NumPy`, `pandas`, `Matplotlib`, `seaborn`, `scikit-learn`, `Joblib` |
| ⚡ **Tool**                 | `Google Colab`                                                       |
| 🚀 **Deployment**           | `Streamlit Community Cloud`                                          |

---

## ⚙️ Petunjuk Pengaturan

1. **Prasyarat**
   - Python 3.11 atau lebih baru.
   - Git terinstal di komputer.

2. **Clone Repositori**

```bash
git clone https://github.com/Fikri-Rouzan/student-stress-levels-classification.git
cd student-stress-levels-classification
```

3. **Buat Virtual Environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

4. **Install Dependensi**

```bash
pip install -r requirements.txt
```

5. **Menjalankan Dashboard Streamlit**

```bash
streamlit run dashboard/dashboard.py
```

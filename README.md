# Student Stress Levels Classification

## 📌 Deskripsi

Proyek ini dirancang untuk mengklasifikasikan tingkat stres mahasiswa berdasarkan parameter akademik dan psikologis. Dengan memanfaatkan pemodelan machine learning, sistem ini memprediksi tingkat tekanan mental berdasarkan data input yang dimasukkan. Hasil dari proyek ini bertujuan membantu pihak perguruan tinggi dalam memantau kondisi psikologis mahasiswa guna mendukung pengambilan keputusan dan menciptakan lingkungan kampus yang kondusif.

---

## 💾 Dataset

Dataset yang digunakan dalam proyek ini bersumber dari [Kaggle: Student Stress Monitoring Datasets](https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets). Dataset ini berisi respons survei anonim dari 843 mahasiswa perguruan tinggi berusia 18 sampai 21 tahun mengenai tingkat stres, kesehatan, hubungan sosial, akademik, dan kondisi emosional. Respons dikumpulkan menggunakan skala Likert lima poin untuk menganalisis hubungan antara indikator stres dengan performa akademik serta faktor gaya hidup.

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

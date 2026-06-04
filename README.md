# Student Stress Levels Classification

## 📌 Deskripsi

Proyek ini dirancang untuk memetakan dan mengklasifikasikan tingkat stres mahasiswa berdasarkan berbagai parameter input yang memengaruhi kondisi akademik serta psikologis mereka. Dengan memanfaatkan pemodelan berbasis machine learning, sistem ini mampu memprediksi kecenderungan tekanan mental berdasarkan data yang dimasukkan. Hasil akhir ini bertujuan membantu pihak perguruan tinggi dalam memahami kesejahteraan psikologis mahasiswa secara terukur guna mendukung pengambilan keputusan yang tepat dan menciptakan lingkungan kampus yang lebih kondusif.

---

## 💾 Dataset

Dataset yang digunakan dalam proyek ini bersumber dari [Kaggle: Student Stress Monitoring Datasets](https://www.kaggle.com/datasets/mdsultanulislamovi/student-stress-monitoring-datasets). Dataset ini menyajikan gambaran mendalam mengenai pengalaman mahasiswa terkait tingkat stres, kesehatan, hubungan sosial, pencapaian akademik, serta kesejahteraan emosional mereka. Di dalamnya mencakup respons survei dari 843 mahasiswa berusia 18 hingga 21 tahun yang dikumpulkan secara anonim menggunakan kuesioner dengan skala Likert lima poin, sehingga memungkinkan analisis mendetail mengenai indikator tekanan fisik maupun emosional dan hubungannya dengan performa belajar serta faktor gaya hidup.

---

## 🛠️ Tech Stack

| Kategori                    | Teknologi yang Digunakan                                              |
| :-------------------------- | :-------------------------------------------------------------------- |
| 🌐 **Programming Language** | `Python`                                                              |
| 🌱 **Environment**          | `Jupyter Notebook`                                                    |
| 🧩 **Framework**            | `Streamlit`                                                           |
| ⚛️ **Libraries**            | `NumPy`, `pandas`, `Matplotlib`, `seaborn`, `scikit-learn`, `Joblib`, |
| ⚡ **Tool**                 | `Google Colab`                                                        |
| 🚀 **Deployment**           | `Streamlit Community Cloud`                                           |

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

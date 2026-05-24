import streamlit as st
import pandas as pd
import os
import joblib
import time
import math
from datetime import datetime

# Konfigurasi halaman streamlit
st.set_page_config(page_title="EduStress", page_icon="🧠", layout="wide")

# Session state untuk menyimpan riwayat prediksi
if "history" not in st.session_state:
    st.session_state.history = []


def delete_history(index):
    st.session_state.history.pop(index)


# Memuat model dengan caching
@st.cache_resource
def load_model():
    MODEL_DIR = "model"

    try:
        rf_model = joblib.load(os.path.join(MODEL_DIR, "student_stress_model.joblib"))
        return rf_model
    except Exception as e:
        st.error(f"Gagal memuat model. Error: {e}")
        return None


rf_model = load_model()

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/512/brain.png", width=120)
    st.title("Data Stres Mahasiswa")
    st.markdown("---")

    st.info("🌲 Model Aktif: Random Forest")

    st.markdown("---")
    st.caption(
        "Dashboard ini dibuat untuk menganalisis parameter psikologis, lingkungan, "
        "dan akademik guna memprediksi tingkat stres mahasiswa menggunakan Machine Learning."
    )

# Header
st.title("EduStress: Analisis Stres Mahasiswa 🧠")
st.markdown(
    "Menampilkan insight dan prediksi tingkat stres mahasiswa berdasarkan berbagai faktor kehidupan akademik dan personal."
)
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["🔍 Prediksi Stres", "📖 Panduan Parameter", "🕒 Riwayat"])

# Tab 1 untuk prediksi stres
with tab1:
    with st.container(border=True):
        st.subheader("Input Parameter Mahasiswa")
        st.markdown("Silakan isi nilai untuk setiap parameter di bawah ini:")

        col1, col2, col3, col4 = st.columns(4)
        # Kolom kesehatan mental
        with col1:
            anxiety_level = st.number_input(
                "Anxiety Level (0-30)", min_value=0, max_value=30, value=10
            )
            self_esteem = st.number_input(
                "Self Esteem (0-30)", min_value=0, max_value=30, value=15
            )
            mental_health_history = st.selectbox(
                "Mental Health History",
                options=[0, 1],
                format_func=lambda x: "Ya" if x == 1 else "Tidak",
            )
            depression = st.number_input(
                "Depression (0-30)", min_value=0, max_value=30, value=10
            )
            headache = st.number_input(
                "Headache (0-10)", min_value=0, max_value=10, value=2
            )

        # Kolom faktor fisik dan lingkungan
        with col2:
            blood_pressure = st.number_input(
                "Blood Pressure (0-5)", min_value=0, max_value=5, value=2
            )
            sleep_quality = st.number_input(
                "Sleep Quality (0-5)", min_value=0, max_value=5, value=3
            )
            breathing_problem = st.number_input(
                "Breathing Problem (0-5)", min_value=0, max_value=5, value=2
            )
            noise_level = st.number_input(
                "Noise Level (0-5)", min_value=0.0, max_value=5.0, value=2.0, step=0.5
            )
            living_conditions = st.number_input(
                "Living Conditions (0-5)",
                min_value=0.0,
                max_value=5.0,
                value=3.0,
                step=0.5,
            )

        # Kolom kebutuhan dan akademik
        with col3:
            safety = st.number_input("Safety (0-5)", min_value=0, max_value=5, value=3)
            basic_needs = st.number_input(
                "Basic Needs (0-5)", min_value=0, max_value=5, value=3
            )
            academic_performance = st.number_input(
                "Academic Performance (0-5)", min_value=0, max_value=5, value=3
            )
            study_load = st.number_input(
                "Study Load (0-5)", min_value=0.0, max_value=5.0, value=2.0, step=0.5
            )
            teacher_student_relationship = st.number_input(
                "Teacher-Student Relationship (0-5)", min_value=0, max_value=5, value=3
            )

        # Kolom sosial dan ekstrakurikuler
        with col4:
            future_career_concerns = st.number_input(
                "Future Career Concerns (0-5)", min_value=0, max_value=5, value=3
            )
            social_support = st.number_input(
                "Social Support (0-5)", min_value=0, max_value=5, value=2
            )
            peer_pressure = st.number_input(
                "Peer Pressure (0-5)", min_value=0, max_value=5, value=3
            )
            extracurricular_activities = st.number_input(
                "Extracurricular Activities (0-5)", min_value=0, max_value=5, value=2
            )
            bullying = st.number_input(
                "Bullying (0-5)", min_value=0, max_value=5, value=1
            )

    st.write("")

    # Button untuk menjalankan prediksi
    if st.button(
        "🔍︎ Analisis Tingkat Stres", type="primary", use_container_width=True
    ):
        if rf_model:
            with st.spinner("Menganalisis data..."):
                time.sleep(0.5)

                # data input untuk prediksi
                input_features = [
                    anxiety_level,
                    self_esteem,
                    mental_health_history,
                    depression,
                    headache,
                    blood_pressure,
                    sleep_quality,
                    breathing_problem,
                    noise_level,
                    living_conditions,
                    safety,
                    basic_needs,
                    academic_performance,
                    study_load,
                    teacher_student_relationship,
                    future_career_concerns,
                    social_support,
                    peer_pressure,
                    extracurricular_activities,
                    bullying,
                ]

                feature_names = [
                    "anxiety_level",
                    "self_esteem",
                    "mental_health_history",
                    "depression",
                    "headache",
                    "blood_pressure",
                    "sleep_quality",
                    "breathing_problem",
                    "noise_level",
                    "living_conditions",
                    "safety",
                    "basic_needs",
                    "academic_performance",
                    "study_load",
                    "teacher_student_relationship",
                    "future_career_concerns",
                    "social_support",
                    "peer_pressure",
                    "extracurricular_activities",
                    "bullying",
                ]

                features_df = pd.DataFrame([input_features], columns=feature_names)

                # Prediksi dengan model Random Forest
                prediction = rf_model.predict(features_df)[0]

                # Menentukan status berdasarkan hasil prediksi
                if prediction == 0:
                    status_text = "STRES RENDAH (LOW)"
                    status_icon = "✅"
                    alert_type = "success"
                elif prediction == 1:
                    status_text = "STRES SEDANG (MEDIUM)"
                    status_icon = "⚠️"
                    alert_type = "warning"
                else:
                    status_text = "STRES TINGGI (HIGH)"
                    status_icon = "🚨"
                    alert_type = "error"

                timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

                # Menyimpan hasil prediksi ke riwayat
                st.session_state.history.append(
                    {
                        "time": timestamp,
                        "model": "Random Forest",
                        "status": status_text,
                        "icon": status_icon,
                        "alert": alert_type,
                        "params": {
                            "Anxiety Level": anxiety_level,
                            "Self Esteem": self_esteem,
                            "Mental Health History": (
                                "Ya" if mental_health_history == 1 else "Tidak"
                            ),
                            "Depression": depression,
                            "Headache": headache,
                            "Blood Pressure": blood_pressure,
                            "Sleep Quality": sleep_quality,
                            "Breathing Problem": breathing_problem,
                            "Noise Level": noise_level,
                            "Living Conditions": living_conditions,
                            "Safety": safety,
                            "Basic Needs": basic_needs,
                            "Academic Performance": academic_performance,
                            "Study Load": study_load,
                            "Teacher-Student Relationship": teacher_student_relationship,
                            "Future Career Concerns": future_career_concerns,
                            "Social Support": social_support,
                            "Peer Pressure": peer_pressure,
                            "Extracurricular Activities": extracurricular_activities,
                            "Bullying": bullying,
                        },
                    }
                )

                st.markdown("---")
                st.subheader("Hasil Analisis")

                # Menampilkan notifikasi visual sesuai tingkat stres
                if alert_type == "success":
                    st.success(f"### {status_icon} STATUS: {status_text}")
                    st.write(
                        "Berdasarkan model klasifikasi, tingkat stres mahasiswa tergolong **Rendah**. Teruskan kebiasaan baik dan lingkungan yang suportif!"
                    )
                elif alert_type == "warning":
                    st.warning(f"### {status_icon} STATUS: {status_text}")
                    st.write(
                        "Berdasarkan model klasifikasi, tingkat stres mahasiswa tergolong **Sedang**. Perhatikan keseimbangan jadwal kuliah dan kesehatan mental."
                    )
                else:
                    st.error(f"### {status_icon} STATUS: {status_text}")
                    st.write(
                        "Berdasarkan model klasifikasi, tingkat stres mahasiswa tergolong **Tinggi**. Disarankan untuk mencari dukungan sosial atau konseling kampus."
                    )
        else:
            st.error("Model belum dimuat dengan benar. Pastikan folder 'model' ada.")

# Tab 2 untuk panduan parameter
with tab2:
    st.subheader("Panduan Parameter")
    st.write("Penjelasan singkat untuk fitur evaluasi kehidupan mahasiswa:")

    with st.expander("🧠 Faktor Psikologis"):
        st.markdown("""
        - **Anxiety Level (Tingkat Kecemasan)**: Mengukur skala kecemasan yang dialami mahasiswa sehari-hari.
        - **Self Esteem (Harga Diri)**: Tingkat kepercayaan diri dan bagaimana mahasiswa menilai kemampuan dirinya sendiri.
        - **Mental Health History (Riwayat Kesehatan Mental)**: Status apakah mahasiswa memiliki riwayat isu kesehatan mental sebelumnya.
        - **Depression (Depresi)**: Skala intensitas gejala depresi atau rasa sedih mendalam yang dialami mahasiswa.
        - **Headache (Sakit Kepala)**: Frekuensi atau tingkat keluhan sakit kepala fisik yang dirasakan oleh mahasiswa.
        - **Blood Pressure (Tekanan Darah)**: Skala indikasi tekanan darah mahasiswa.
        - **Sleep Quality (Kualitas Tidur)**: Tingkat kenyamanan, durasi, dan seberapa nyenyak tidur mahasiswa setiap malamnya.
        - **Breathing Problem (Masalah Pernapasan)**: Adanya gangguan pernapasan seperti sesak napas yang dapat dipicu oleh kepanikan.
        """)

    with st.expander("🌆 Faktor Lingkungan"):
        st.markdown("""
        - **Noise Level (Tingkat Kebisingan)**: Seberapa bising atau mengganggunya lingkungan sekitar tempat tinggal dan tempat belajar mahasiswa.
        - **Living Conditions (Kondisi Tempat Tinggal)**: Kelayakan, kebersihan, dan kenyamanan fasilitas tempat tinggal mahasiswa.
        - **Safety (Keamanan)**: Rasa aman psikologis dan fisik yang dirasakan mahasiswa baik di lingkungan tempat tinggal maupun sekitar kampus.
        - **Basic Needs (Kebutuhan Dasar)**: Tingkat pemenuhan kebutuhan pokok primer sehari-hari.
        """)

    with st.expander("🎓 Faktor Akademik"):
        st.markdown("""
        - **Academic Performance (Performa Akademik)**: Nilai IPK atau tingkat keberhasilan akademik mahasiswa di perkuliahan.
        - **Study Load (Beban Belajar)**: Volume materi perkuliahan, banyaknya SKS, praktikum, dan jam belajar.
        - **Teacher-Student Relationship (Hubungan Dosen-Mahasiswa)**: Kualitas interaksi, keterbukaan, dan dukungan dari dosen/pembimbing akademik kepada mahasiswa.
        - **Future Career Concerns (Kekhawatiran Karir Masa Depan)**: Tingkat kecemasan mahasiswa mengenai kelulusan, persaingan kerja, atau kepastian karir.
        """)

    with st.expander("🤝 Faktor Sosial"):
        st.markdown("""
        - **Social Support (Dukungan Sosial)**: Kemudahan mahasiswa dalam mendapatkan bantuan emosional dari keluarga, teman kos, atau sahabat terdekat.
        - **Peer Pressure (Tekanan Teman Sebaya)**: Tingkat tekanan sosial dari lingkungan pergaulan kampus untuk mengikuti gaya hidup atau standar perilaku tertentu.
        - **Extracurricular Activities (Aktivitas Ekstrakurikuler/UKM)**: Tingkat keaktifan serta beban waktu pada kegiatan non-akademik seperti organisasi kampus atau UKM.
        - **Bullying (Perundungan)**: Frekuensi pengalaman intimidasi fisik, verbal, maupun siber yang dialami oleh mahasiswa di lingkungan sekitarnya.
        """)


# Tab 3 untuk riwayat prediksi
with tab3:
    st.subheader("Riwayat Prediksi")
    total_items = len(st.session_state.history)

    if total_items == 0:
        st.info(
            "Belum ada riwayat prediksi. Silakan lakukan analisis terlebih dahulu di tab 'Prediksi Stres'."
        )
    else:
        st.write(f"Total pengujian pada sesi ini: **{total_items} data**")

        # Pagination untuk riwayat prediksi
        ITEMS_PER_PAGE = 5
        total_pages = math.ceil(total_items / ITEMS_PER_PAGE)

        # Kontrol untuk memilih halaman
        if total_pages > 1:
            current_page = st.radio(
                "Pilih Halaman:", options=range(1, total_pages + 1), horizontal=True
            )
        else:
            current_page = 1

        # Menghitung indeks data yang akan ditampilkan berdasarkan halaman saat ini
        start_idx = (current_page - 1) * ITEMS_PER_PAGE
        end_idx = start_idx + ITEMS_PER_PAGE

        # Menampilkan data sesuai halaman
        for i in range(start_idx, min(end_idx, total_items)):
            record = st.session_state.history[i]

            with st.container(border=True):
                col_text, col_btn = st.columns([5, 1])

                # Menampilkan informasi waktu, model, dan hasil prediksi
                with col_text:
                    st.write(f"**{record['time']}** | Model: `{record['model']}`")

                    if record["alert"] == "success":
                        st.success(f"{record['icon']} **{record['status']}**")
                    elif record["alert"] == "warning":
                        st.warning(f"{record['icon']} **{record['status']}**")
                    else:
                        st.error(f"{record['icon']} **{record['status']}**")

                    # Menampilkan detail parameter input
                    if "params" in record:
                        with st.expander("Lihat Detail Parameter Input"):
                            p = record["params"]
                            c1, c2, c3, c4 = st.columns(4)

                            with c1:
                                st.caption(f"Anxiety Level: {p['Anxiety Level']}")
                                st.caption(f"Self Esteem: {p['Self Esteem']}")
                                st.caption(
                                    f"Mental Health History: {p['Mental Health History']}"
                                )
                                st.caption(f"Depression: {p['Depression']}")
                                st.caption(f"Headache: {p['Headache']}")

                            with c2:
                                st.caption(f"Blood Pressure: {p['Blood Pressure']}")
                                st.caption(f"Sleep Quality: {p['Sleep Quality']}")
                                st.caption(
                                    f"Breathing Problem: {p['Breathing Problem']}"
                                )
                                st.caption(f"Noise Level: {p['Noise Level']}")
                                st.caption(
                                    f"Living Conditions: {p['Living Conditions']}"
                                )

                            with c3:
                                st.caption(f"Safety: {p['Safety']}")
                                st.caption(f"Basic Needs: {p['Basic Needs']}")
                                st.caption(
                                    f"Academic Performance: {p['Academic Performance']}"
                                )
                                st.caption(f"Study Load: {p['Study Load']}")
                                st.caption(
                                    f"Teacher-Student Relationship: {p['Teacher-Student Relationship']}"
                                )

                            with c4:
                                st.caption(
                                    f"Future Career Concerns: {p['Future Career Concerns']}"
                                )
                                st.caption(f"Social Support: {p['Social Support']}")
                                st.caption(f"Peer Pressure: {p['Peer Pressure']}")
                                st.caption(
                                    f"Extracurricular Activities: {p['Extracurricular Activities']}"
                                )
                                st.caption(f"Bullying: {p['Bullying']}")

                # Tombol untuk menghapus riwayat prediksi
                with col_btn:
                    st.button(
                        "🗑️ Hapus",
                        key=f"delete_btn_{i}_{record['time']}",
                        on_click=delete_history,
                        args=(i,),
                        use_container_width=True,
                    )

# Footer
st.markdown("---")
st.caption("© 2026 Muhammad Fikri Rouzan Ash Shidik")

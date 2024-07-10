# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Jaya Jaya Institut adalah salah satu lembaga pendidikan tinggi yang telah beroperasi sejak tahun 2000 dan telah menghasilkan banyak lulusan dengan reputasi yang sangat baik. Meskipun demikian, lembaga ini juga menghadapi tantangan besar dalam hal tingkat siswa yang tidak menyelesaikan pendidikannya, atau yang dikenal sebagai dropout.

Tingginya tingkat dropout menjadi perhatian serius bagi lembaga pendidikan ini. Oleh karena itu, Jaya Jaya Institut bertekad untuk mengidentifikasi siswa yang berpotensi melakukan dropout sejak dini, sehingga mereka dapat diberikan bimbingan khusus untuk mencegah hal tersebut terjadi.

### Permasalahan Bisnis

Jaya Jaya Institut menghadapi sejumlah tantangan dan risiko yang signifikan terkait tingkat dropout siswa mereka. Tantangan utamanya termasuk mempertahankan tingkat kelulusan yang tinggi serta menjaga reputasi sebagai lembaga pendidikan yang berkualitas. Tingginya tingkat siswa yang tidak menyelesaikan pendidikan dapat mengakibatkan penurunan pendapatan lembaga, karena berkurangnya jumlah mahasiswa yang membayar biaya kuliah. Selain itu, lembaga ini juga berisiko kehilangan kepercayaan dari masyarakat dan calon siswa jika masalah ini tidak ditangani secara efektif.

Dampak jangka pendek dari masalah ini mencakup penurunan kualitas layanan pendidikan akibat kebutuhan mendesak untuk mengalokasikan sumber daya tambahan untuk mengurangi tingkat dropout. Hal ini dapat mempengaruhi kondisi keuangan lembaga dan kesejahteraan staf akademik yang terlibat dalam upaya pencegahan. Di sisi lain, dampak jangka panjang mencakup kemungkinan penurunan pendapatan jangka panjang dan reputasi yang tergerus, yang dapat menghambat pertumbuhan institusi dalam menarik siswa dan mendapatkan dukungan dari stakeholder. Selain itu, lembaga ini juga berisiko kehilangan kemampuan untuk memberikan kontribusi positif terhadap masyarakat dan perekonomian secara keseluruhan jika tidak ada tindakan preventif yang dilakukan dengan segera.

### Cakupan Proyek

- Melakukan data analysis terhadap faktor yang mempengaruhi dropout
- Membuat dan mengevaluasi model machine learning untuk memperdiksi status student
- Membuat prototipe app prediksi status student dengan Streamlit
- Membuat dashboard monitoring student

### Persiapan

Sumber data: [students' performance](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)

Setup environment:

```
conda create --name main-ds python=3.11.3
conda activate main-ds
pip install -r requirements.txt

```

## Business Dashboard

Jelaskan tentang business dashboard yang telah dibuat. Jika ada, sertakan juga link untuk mengakses dashboard tersebut.

## Menjalankan Sistem Machine Learning

Jelaskan cara menjalankan protoype sistem machine learning yang telah dibuat. Selain itu, sertakan juga link untuk mengakses prototype tersebut.

```
streamlit run app.py

```

Link Streamlit:

## Conclusion

Jelaskan konklusi dari proyek yang dikerjakan.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.

- Faktor yang paling berpengaruh dalam dropout diantaranya nilai semester dan jumlah kredit semester dapat diantisipasi lebih dini oleh institusi melalui pemantauan progres akademik. Implementasikan pula program bimbingan dan monitoring yang intensif untuk siswa sehingga siswa dapat menyelesaikan pendidikan.
- Tuition fee dan scholarship juga memberi pengaruh pada droupout siswa. Insitut dapat melakukan evaluasi kebijakan keuangan seperti penawaran beasiswa tambahan, program bantuan keuangan, atau pengaturan pembayaran yang lebih fleksibel.

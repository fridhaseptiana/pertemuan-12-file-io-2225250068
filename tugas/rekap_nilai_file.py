
def baca_data(nama_file):
    data = []

    try:
        with open(nama_file, "r", encoding="utf-8") as file:
            for nomor, baris in enumerate(file, start=1):
                baris = baris.strip()

                if not baris:
                    continue

                try:
                    nim, teks_nilai = baris.split(",")
                    nilai = float(teks_nilai)
                    data.append((nim, nilai))
                except ValueError:
                    print(f"Baris {nomor} invalid: {baris}")

    except FileNotFoundError:
        print(f"File tidak ditemukan: {nama_file}")
        return None

    return data


def tulis_rekap(nama_file, data):
    with open(nama_file, "w", encoding="utf-8") as file:
        if not data:
            file.write("Tidak ada data valid.\n")
            return

        nilai = [record[1] for record in data]
        jumlah = len(data)
        rata_rata = sum(nilai) / jumlah
        minimum = min(nilai)
        maksimum = max(nilai)
        lulus = sum(1 for n in nilai if n >= 60)

        file.write("REKAP NILAI MAHASISWA\n")
        file.write(f"Jumlah data valid: {jumlah}\n")
        file.write(f"Rata-rata: {rata_rata:.2f}\n")
        file.write(f"Nilai minimum: {minimum:.2f}\n")
        file.write(f"Nilai maksimum: {maksimum:.2f}\n")
        file.write(f"Jumlah lulus (nilai >= 60): {lulus}\n")


input_file = "data/nilai.txt"
output_file = "data/hasil_rekap.txt"

data = baca_data(input_file)

if data is not None:
    try:
        tulis_rekap(output_file, data)
        print(f"Rekap berhasil disimpan ke {output_file}")
    except OSError as error:
        print(f"Gagal menulis file: {error}")

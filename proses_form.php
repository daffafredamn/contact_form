<?php
include 'terima_kasih.php';
if (isset($_SERVER["REQUEST_METHOD"]) && $_SERVER["REQUEST_METHOD"] == "POST") {
// Ganti dengan kredensial database Anda yang benar
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "formulir_kontak";

$conn = new mysqli($servername, $username, $password, $dbname);

// Periksa koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error); 

} else {
    echo "Koneksi berhasil";  

}
// Ambil data dari formulir
$nama = $_POST['nama'];
$nim = $_POST['nim'];
$kelas = $_POST['kelas'];
$gender = $_POST['gender'];
$email = $_POST['email'];
$pesan = $_POST['pesan'];

// Siapkan dan jalankan pernyataan INSERT
$sql = "INSERT INTO kontak (nama, nim, kelas, gender, email, pesan) VALUES (?, ?, ?, ?, ?, ?)";
$stmt = $conn->prepare($sql);
$stmt->bind_param("ssssss", $nama, $nim, $kelas, $gender, $email, $pesan);

if ($stmt->execute()) {
    header("Location: terima_kasih.php");
    exit();
} else {
    // Jika terjadi kesalahan, tampilkan pesan kesalahan
    echo "Terjadi kesalahan: " . $stmt->error;
}

$stmt->close();
$conn->close();
}
?>
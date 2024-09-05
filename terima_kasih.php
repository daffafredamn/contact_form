<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "formulir_kontak";

$conn = new mysqli($servername, $username, $password, $dbname);

// Periksa koneksi
if ($conn->connect_error) {
    die("Koneksi gagal: " . $conn->connect_error);
}
?> 
<!DOCTYPE html>
<html>
<head>
    <title>Terima Kasih</title>
    <link rel="stylesheet" href="style.css"> </head>
</head>
<body>
    <h1>Terima kasih!</h1>
    <p>Data Anda telah berhasil kami terima.</p>
</body>
</html>
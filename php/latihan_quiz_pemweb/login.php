<?php
session_start();

if (isset($_POST["login"])) {
    $servername = "localhost";
    $usernamedb = "root";
    $passworddb = "";
    $dbname = "dblatihan";
    $nama = $_POST["username"];
    $password = $_POST["password"];
    $conn = new mysqli($servername, $usernamedb, $passworddb, $dbname);
    if ($conn->connect_error) {
        die("Koneksi gagal : " . $conn->connect_error);
    }

    $result = $conn->query("select nama, katakunci from pengguna");
    foreach ($result as $a) {
        if ($a["nama"] == $nama && $a["katakunci"] == $password) {
            $_SESSION["logged in"] = true;
            header("Location: table.php");
        } else {
            unset($_SESSION["logged in"]);
            header("Location: index.php");
        }
    }
} else {
    header("Location: index.php");
}
?>

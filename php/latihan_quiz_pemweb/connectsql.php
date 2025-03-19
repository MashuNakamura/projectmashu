<?php
        session_start();
        if(isset($_SESSION["logged in"])){
            $servername = "localhost";
            $usernamedb = "root";
            $passworddb = "";
            $dbname = "dblatihan";
            $conn = new mysqli($servername, $usernamedb, $passworddb, $dbname);

            if(isset($_POST["add-this"])) {
                $nim = $_POST["nim"];
                $nama = $_POST["name"];
                $tanggal_lahir = $_POST["tanggal_lahir"];
                $alamat = $_POST["alamat"];
                $conn->query("insert into mhs (nim, nama, tgl_lahir, alamat) values ('$nim', '$nama', '$tanggal_lahir', '$alamat')");
                header("Location: table.php");
            }
        }
?>

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
                $alamat = $_POST["alamat"];
                $conn->query("insert into mhs (nim, nama, alamat) values ('$nim', '$nama', '$alamat')");
                header("Location: table.php");
            }
        }
?>

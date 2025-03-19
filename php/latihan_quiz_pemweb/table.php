<html>
    <head>
        <title>Table</title>
    </head>
    <body>
        <?php
        session_start();
        if(isset($_SESSION["logged in"])){
            $servername = "localhost";
            $usernamedb = "root";
            $passworddb = "";
            $dbname = "dblatihan";
            $conn = new mysqli($servername, $usernamedb, $passworddb, $dbname);


            if(isset($_POST["add"])){ 
                echo '<form method="post" action ="add-this.php">';
                echo '<label for="nim">NIM : </label>';
                echo '<input type="number" name="nim">';
                echo '<label for="name"> Nama : </label>';
                echo '<input type="text" name="name">';
                echo '<label for="tanggal_lahir"> Tanggal Lahir : </label>';
                echo '<input type="date" name="tanggal_lahir">';
                echo '<label for="alamat"> Alamat : </label>';
                echo '<input type="text" name="alamat">';
                echo '<input type="submit" name="add-this">';
                echo '<form>';
            }
            
            // Default query
            $str = "select * from mhs";

            if(isset($_GET["search"])){
            $q = $_GET["query"];
            $str = "select * from mhs where nim like '%$q%' or nama like '%$q%' or tgl_lahir like '%$q%' or alamat like '%$q%'";
            }

            $result = $conn->query($str);
            foreach ($result as $a) {
                $nim = $a["nim"];
                $nama = $a["nama"];
                $tanggal_lahir = $a["tgl_lahir"];
                $alamat = $a["alamat"];


                if(isset($_POST["delete-$nim"])){
                    $conn->query("delete from mhs where nim = '$nim'"); 
                }

                if(isset($_POST["edit-$nim"])) { 
                    echo "<form method='post' action ='table.php'>";
                    echo "<label for='nim'>NIM : </label>";
                    echo "<input type='number' name='nim' value='$nim'>";
                    echo "<label for='name'> Nama : </label>";
                    echo "<input type='text' name='name' value='$nama'>";
                    echo "<label for='tanggal_lahir'> Tanggal Lahir : </label>";
                    echo "<input type='date' name='tanggal_lahir' value='$tanggal_lahir'>";
                    echo "<label for='alamat'> Alamat : </label>";
                    echo "<input type='text' name='alamat' value='$alamat'>";
                    echo "<input type='submit' name='edit-this-$nim'>";
                    echo '<form>';
                    }

                if(isset($_POST["edit-this-$nim"])) {
                    $new_nim = $_POST["nim"];
                    $new_nama = $_POST["name"];
                    $new_tanggal_lahir = $_POST["tanggal_lahir"];
                    $new_alamat = $_POST["alamat"];
                    $conn->query("update mhs set nama = '$new_nama', tgl_lahir = '$new_tanggal_lahir', alamat = '$new_alamat' where nim = '$new_nim'");                    
                    }
                }

            echo '<table border="1">';
            echo '<tr>';
            echo '<td>NIM</td>';
            echo '<td>Nama</td>';
            echo '<td>Tanggal Lahir</td>';
            echo '<td>Alamat</td>';
            echo '<td>';
            echo '<center>';
            echo '<form method="post" action="table.php">';
            echo '<input type="submit" value="add" name="add">';
            echo '</center>';
            echo '</form>';
            echo '</td>';
            echo '</tr>';
            $result = $conn->query($str); 
            foreach ($result as $a) {
                $nim = $a['nim'];
                echo '<tr>';
                echo '<td>' . $a["nim"] . '</td>'; 
                echo '<td>' . $a["nama"] . '</td>'; 
                echo '<td>' . $a["tgl_lahir"] . '</td>'; 
                echo '<td>' . $a["alamat"] . '</td>'; 
                echo '<td>';
                echo '<form method="post" action="table.php">';
                echo "<input type='submit' value='edit' name='edit-$nim'>";
                echo "<input type='submit' value='delete' name='delete-$nim'>";
                echo '</form>';
                echo '</td>';
                echo '</tr>';
            }
            echo '</table>';
            echo "<br>";
            echo '<form method="GET" action="table.php">';
            echo '<textarea name="query" id="searchbox"></textarea>';
            echo '<input type="submit" value="Search" name="search">';
            echo "<br>";
            echo "<br>";
            echo '<input type="submit" value="Logout" name="logout">';
            echo '</center>';
            echo '</form>';

        } else {
        session_destroy();
        header("Location: index.php");
        }

        if(isset($_POST["logout"])){
            session_destroy();
            header("Location: index.php");
        }
        ?>
    </body>
</html>

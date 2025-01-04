<?php
// reg.php
if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if (
        isset($_POST['u1'], $_POST['u2'], $_POST['u3'], $_POST['u4'], $_POST['user_type']) &&
        !empty($_POST['u1']) && !empty($_POST['u2']) &&
        !empty($_POST['u3']) && !empty($_POST['u4']) && !empty($_POST['user_type'])
    ) {
        // Collect form data
        $name = $_POST['u1'];
        $email = $_POST['u2'];
        $contact = $_POST['u3'];
        $password = $_POST['u4'];
        $role = $_POST['user_type'];

        // Encrypt the password
        $enc_pass = md5($password);

        // Map roles to database columns
        $is_farmer = 0;
        $is_rent_owner = 0;
        $is_agronomist = 0;
        $is_storage_owner = 0;

        switch ($role) {
            case 'farmer':
                $is_farmer = 1;
                break;
            case 'equipment_renter':
                $is_rent_owner = 1;
                break;
            case 'agronomist':
                $is_agronomist = 1;
                break;
            case 'storage_owner':
                $is_storage_owner = 1;
                break;
            default:
                echo "<script>alert('Invalid role selected.'); location.assign('signup.php');</script>";
                exit();
        }

        try {
            // Connect to the database
            $con = new PDO('mysql:host=localhost:3306;dbname=hm;', 'root', '');
            $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Begin transaction
            $con->beginTransaction();

            // Insert into UserInfo table
            $query = "INSERT INTO UserInfo (user_name, password, user_id, is_farmer, is_storage_owner, is_rent_owner, is_agronomist, role_count) 
                      VALUES (:name, :password, :email, :is_farmer, :is_storage_owner, :is_rent_owner, :is_agronomist, :role_count)";
            $stmt = $con->prepare($query);

            $stmt->execute([
                ':name' => $name,
                ':password' => $enc_pass,
                ':email' => $email,
                ':is_farmer' => $is_farmer,
                ':is_storage_owner' => $is_storage_owner,
                ':is_rent_owner' => $is_rent_owner,
                ':is_agronomist' => $is_agronomist,
                ':role_count' => 1
            ]);

            // Set user_id in session
            session_start();
            $_SESSION['user_id'] = $email;

            // If the user is a farmer, insert into the Farmer table
            if ($is_farmer) {
                $queryFarmer = "INSERT INTO Farmer (user_id) VALUES (:user_id)";
                $stmtFarmer = $con->prepare($queryFarmer);
                $stmtFarmer->execute([
                    ':user_id' => $email
                ]);
            }

            // Commit transaction
            $con->commit();

            // Redirect to the appropriate page based on the role
            if ($is_farmer) {
                header("Location: farmerSignUp.php");
                exit();
            } else {
                header("Location: login.php");
                exit();
            }
        } catch (PDOException $e) {
            // Rollback transaction on error
            $con->rollBack();
            echo "<script>alert('Database error: " . $e->getMessage() . "'); location.assign('signup.php');</script>";
        }
    } else {
        echo "<script>alert('Please fill out all fields.'); location.assign('signup.php');</script>";
    }
} else {
    header("Location: signup.php");
    exit();
}
?>

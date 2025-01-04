<?php
session_start();

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if (
        isset($_POST['u2']) && 
        isset($_POST['u4']) &&
        !empty($_POST['u2']) &&
        !empty($_POST['u4'])
    ) {
        $user_id = $_POST['u2'];
        $password = $_POST['u4'];
        $encrypted_password = md5($password); // Assuming passwords are stored as MD5 hashes

        try {
            // Establish database connection
            $con = new PDO('mysql:host=localhost;dbname=hm', 'root', '');
            $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Prepare and execute query
            $query = "SELECT * FROM UserInfo WHERE user_id = :user_id AND password = :password";
            $stmt = $con->prepare($query);
            $stmt->execute([
                ':user_id' => $user_id,
                ':password' => $encrypted_password
            ]);

            // Check if the user exists
            if ($stmt->rowCount() == 1) {
                $user = $stmt->fetch(PDO::FETCH_ASSOC);

                $_SESSION['user_info_id'] = $user['user_info_id'];
                $_SESSION['user_name'] = $user['user_name'];
                $_SESSION['user_id'] = $user['user_id'];
                $_SESSION['is_admin'] = $user['is_admin'];
                $_SESSION['is_farmer'] = $user['is_farmer'];
                $_SESSION['is_storage_owner'] = $user['is_storage_owner'];
                $_SESSION['is_rent_owner'] = $user['is_rent_owner'];
                $_SESSION['is_agronomist'] = $user['is_agronomist'];

                // Redirect to a dashboard or home page
                header("Location: home.php");
                exit;
            } else {
                // Invalid credentials
                $_SESSION['error'] = "Invalid user ID or password. Please try again.";
                header("Location: login.php");
                exit;
            }
        } catch (PDOException $e) {
            // Handle database connection or query errors
            $_SESSION['error'] = "Database error: " . $e->getMessage();
            header("Location: login.php");
            exit;
        }
    } else {
        // Missing credentials
        $_SESSION['error'] = "Please provide both user ID and password.";
        header("Location: login.php");
        exit;
    }
} else {
    // Invalid request method
    header("Location: login.php");
    exit;
}
?>

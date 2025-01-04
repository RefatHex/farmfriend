<?php
// farmerReg.php
session_start(); // Start the session

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    if (
        isset($_POST['name'], $_POST['dob'], $_POST['address'], $_POST['field_size']) &&
        !empty($_POST['name']) && !empty($_POST['dob']) &&
        !empty($_POST['address']) && !empty($_POST['field_size'])
    ) {
        $name = $_POST['name'];
        $dob = $_POST['dob'];
        $address = $_POST['address'];
        $field_size = $_POST['field_size'];

        // Handle file upload (optional)
        $upload_file = null;
        if (isset($_FILES['picture']) && $_FILES['picture']['error'] == UPLOAD_ERR_OK) {
            $picture = $_FILES['picture'];
            $picture_name = uniqid() . '_' . basename($picture['name']);
            $upload_dir = 'uploads/';
            $upload_file = $upload_dir . $picture_name;

            if (!is_dir($upload_dir)) {
                mkdir($upload_dir, 0777, true); // Create the uploads directory if it doesn't exist
            }

            if (!move_uploaded_file($picture['tmp_name'], $upload_file)) {
                $upload_file = null; // Reset if upload fails
            }
        }

        try {
            // Database connection
            $con = new PDO('mysql:host=localhost;dbname=hm', 'root', '');
            $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Retrieve user_id from session
            if (isset($_SESSION['user_id'])) {
                $user_id = $_SESSION['user_id'];
            } else {
                echo "User is not logged in.";
                exit();
            }

            // Update the Farmer table
            $query = "UPDATE Farmer 
                      SET name = :name, dob = :dob, address = :address, field_size = :field_size" . 
                      ($upload_file ? ", profile_picture = :profile_picture" : "") . " 
                      WHERE user_id = :user_id";

            $stmt = $con->prepare($query);
            $params = [
                ':user_id' => $user_id,
                ':name' => $name,
                ':dob' => $dob,
                ':address' => $address,
                ':field_size' => $field_size,
            ];
            if ($upload_file) {
                $params[':profile_picture'] = $upload_file;
            }

            $stmt->execute($params);

            // Redirect to login page
            header("Location: login.php");
            exit();
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill all fields.";
    }
} else {
    header("Location: farmerSignup.php");
    exit();
}
?>

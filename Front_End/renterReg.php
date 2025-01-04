<?php
// renterReg.php
session_start(); // Start the session

if ($_SERVER['REQUEST_METHOD'] == "POST") {
    // Check if all required fields are present
    if (
        isset($_POST['name'], $_POST['dob'], $_POST['u3'], $_POST['address'], $_POST['equipment_details']) &&
        !empty($_POST['name']) && !empty($_POST['dob']) &&
        !empty($_POST['u3']) && !empty($_POST['address']) &&
        !empty($_POST['equipment_details'])
    ) {
        // Sanitize input
        $name = htmlspecialchars($_POST['name']);
        $dob = $_POST['dob'];
        $contact = htmlspecialchars($_POST['u3']);
        $address = htmlspecialchars($_POST['address']);
        $equipment_details = htmlspecialchars($_POST['equipment_details']);

        try {
            // Database connection
            $con = new PDO('mysql:host=localhost;dbname=hm', 'root', '');
            $con->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);

            // Retrieve user_id from session
            if (isset($_SESSION['user_id'])) {
                $user_id = $_SESSION['user_id'];

                // Insert into RentOwner table
                $query = "INSERT INTO RentOwner (name, dob, contact, address, rental_product, user_id, no_of_deals)
                          VALUES (:name, :dob, :contact, :address, :equipment_details, :user_id, :no_of_deals)";
                $stmt = $con->prepare($query);
                $stmt->execute([
                    ':name' => $name,
                    ':dob' => $dob,
                    ':contact' => $contact,
                    ':address' => $address,
                    ':equipment_details' => $equipment_details,
                    ':user_id' => $user_id,
                    ':no_of_deals' => 0 // Initialize no_of_deals to 0
                ]);

                // Redirect to login page with a success message
                $_SESSION['message'] = "Registration successful. Please log in.";
                header("Location: login.php");
                exit();
            } else {
                echo "Error: User is not logged in.";
                exit();
            }
        } catch (PDOException $e) {
            echo "Error: " . $e->getMessage();
        }
    } else {
        echo "Please fill all fields.";
    }
} else {
    header("Location: renterSignup.php");
    exit();
}

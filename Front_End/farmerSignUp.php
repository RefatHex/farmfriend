<!DOCTYPE HTML>
<html>

<head>
    <meta charset="utf-8">
    <title>Farmer Sign Up</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <style>
        /* Reusing the same styles from the previous page */
        body {
            background-color: #1c1c1e;
            background-image: url('images/farmerSignup.jpg');
            background-size: cover;
            background-position: center;
            color: white;
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            height: 100vh;
            position: relative;
        }

        body::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: inherit;
            filter: blur(8px);
            z-index: -1;
        }

        .full-container {
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .content {
            flex: 1;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: -80px;
        }

        .form_ {
            width: 400px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
            position: relative;
        }

        .form_ h4 {
            text-align: center;
            margin-bottom: 20px;
            font-weight: bold;
            font-size: 24px;
        }

        .form-control {
            background-color: #2e2e2e;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px;
        }

        .form-control:focus {
            border-color: #007bff;
            box-shadow: 0 0 8px rgba(0, 123, 255, 0.5);
            background-color: #1c1c1e;
        }

        .form-control:hover {
            background-color: #333;
        }

        .btn-submit {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 5px;
            width: 100%;
            margin-top: 20px;
        }

        .btn-submit:hover {
            background-color: #0056b3;
            cursor: pointer;
            box-shadow: 0 4px 10px rgba(0, 91, 179, 0.5);
            transition: all 0.3s ease;
        }

        nav.navbar {
            background: linear-gradient(to right, #3b6e3d, #2f4f2f);
            border: none;
            border-radius: 0;
            margin-bottom: 0;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        nav.navbar a {
            color: #fff !important;
            font-weight: bold;
            font-size: 16px;
        }

        nav.navbar a:hover {
            background-color: rgba(255, 255, 255, 0.2) !important;
            color: #fff !important;
            transition: all 0.3s ease;
            border-radius: 5px;
            padding: 5px 10px;
        }

        .form-group {
            margin-bottom: 20px;
        }
    </style>
</head>

<body>

    <div class="full-container">
        <nav class="navbar navbar-inverse">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" href="http://localhost/hm/home.php">FARM FRIEND</a>
                </div>
                <ul class="nav navbar-nav">
                    <li><a href="http://localhost/hm/login.php">Login</a></li>
                    <li><a href="http://localhost/hm/signup.php">Sign Up</a></li>
                    <li class="active"><a href="#">Farmer Sign Up</a></li>
                </ul>
            </div>
        </nav>

        <div class="content">
            <div class="form_">
                <h4>Farmer Additional Details</h4>

                <form action="farmerReg.php" method="POST">
                    <div class="form-group">
                        <label for="name">Name: </label>
                        <input type="text" class="form-control" id="name" name="name" placeholder="Enter Your Name" required>
                    </div>

                    <div class="form-group">
                        <label for="dob">Date of Birth: </label>
                        <input type="date" class="form-control" id="dob" name="dob" required>
                    </div>

                    <div class="form-group">
                        <label for="address">Address: </label>
                        <textarea class="form-control" id="address" name="address" placeholder="Enter Your Address" rows="3" required></textarea>
                    </div>

                    <div class="form-group">
                        <label for="field_size">Field Size (in hectares): </label>
                        <input type="number" class="form-control" id="field_size" name="field_size" placeholder="Enter Field Size" step="0.01" required>
                    </div>

                    <div class="form-group">
                        <label for="picture">Profile Picture: </label>
                        <input type="file" class="form-control" id="picture" name="picture" accept="image/*">
                    </div>

                    <button type="submit" class="btn-submit">Submit</button>
                </form>
            </div>
        </div>
    </div>

    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>

</body>

</html>

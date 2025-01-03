<!DOCTYPE html>
<html lang="en">

<head>
    <title>Home</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            background-color: #f3f4f6;
            font-family: 'Arial', sans-serif;
            color: #333;
            overflow-x: hidden;
        }

        nav.navbar {
            background: linear-gradient(to right, #3b6e3d, #2f4f2f); /* Dark green gradient */
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

        .background {
            background-image: url('images/hf.png'); /* Update with your image path */
            background-size: cover;
            background-position: center;
            width: 100%;
            height: calc(100vh - 50px); /* Fill the viewport, minus the navbar height */
            position: relative;
        }

        .title-container {
            position: absolute;
            top: -5%; /* Positioned dynamically */
            left: 50%;
            transform: translateX(-50%);
            text-align: center;
            color: white;
        }

        .title-container h2 {
            font-size: 3rem;
            font-weight: 700;
            background: rgba(0, 0, 0, 0.6);
            color: #fff;
            display: inline-block;
            padding: 15px 30px;
            border-radius: 15px;
            box-shadow: 0 6px 15px rgba(0, 0, 0, 0.3);
        }

        .title-container hr {
            width: 80px;
            height: 4px;
            background: white;
            margin: 10px auto;
            border: none;
            border-radius: 2px;
        }
    </style>
</head>

<body>
    <nav class="navbar navbar-inverse">
        <div class="container-fluid">
            <div class="navbar-header">
                <a class="navbar-brand" href="http://localhost/hm/home.php">FARM FRIEND</a>
            </div>
            <ul class="nav navbar-nav">
                <li><a href="http://localhost/hm/login.php">Login</a></li>
                <li><a href="http://localhost/hm/signup.php">Sign Up</a></li>
            </ul>
        </div>
    </nav>

    <div class="background">
        <div class="title-container">
            <hr />
            <h2>FARM FRIEND</h2>
            <hr />
        </div>
    </div>
</body>

</html>

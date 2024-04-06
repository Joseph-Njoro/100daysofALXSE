<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tic Tac Toe</title>
    <link rel="stylesheet" href="style.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-image: url('background.jpg'); /* Replace 'background.jpg' with the path to your own background image */
            background-size: cover;
            background-position: center;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            padding: 0;
        }

        .container {
            display: grid;
            grid-template-columns: repeat(3, 150px); /* Increased size of grid columns */
            grid-template-rows: repeat(3, 150px); /* Increased size of grid rows */
            gap: 2px;
            border: 4px solid #333; /* Added border around the grid */
            padding: 10px; /* Added padding to the container */
        }

        .cell {
            display: flex;
            justify-content: center;
            align-items: center;
            border: 2px solid #333; /* Made borders thicker */
            cursor: pointer;
            font-size: 36px; /* Increased font size */
            background-color: rgba(255, 255, 255, 0.7); /* Added a semi-transparent white background */
            transition: background-color 0.3s ease; /* Added transition for smoother hover effect */
        }

        .cell:hover {
            background-color: rgba(255, 255, 255, 0.9); /* Lighten the background color on hover */
        }

        .player-text {
            text-align: center;
            font-size: 24px;
            margin-bottom: 20px;
            color: #333;
        }

        .player1 {
            color: blue;
        }

        .player2 {
            color: red;
        }
    </style>
</head>
<body>
    <h2 class="player-text">Player X's Turn</h2>
    <div class="container">
        <div class="cell" id="cell00"></div>
        <div class="cell" id="cell01"></div>
        <div class="cell" id="cell02"></div>
        <div class="cell" id="cell10"></div>
        <div class="cell" id="cell11"></div>
        <div class="cell" id="cell12"></div>
        <div class="cell" id="cell20"></div>
        <div class="cell" id="cell21"></div>
        <div class="cell" id="cell22"></div>
    </div>

    <script src="feedback.js"></script>
</body>
</html>
import express from 'express';
import cookieParser from 'cookie-parser';
import path from 'path';
import mysql from 'mysql';

import authRoutes from "./routes/auth.routes.js";
import messageRouter from "./routes/message.routes.js"

import protectRoute from './middleware/protectRoute.js';


// Connecting with MySQL
const con = mysql.createConnection({
	host: "localhost",
	user: "root",
	password: "",
	database: "CyberPulse_DB"
});

// Connect
con.connect((err) => {
	if (err) throw err;
	console.log("MySQL Connected!");
});


// App
const app = express();
const PORT = 8080;

// View Engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "../frontend/views"));


// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());


// Routes
app.get('/', async (req, res) => {
    try { // User is Loggin
        const loggedInUserId = req.user._id; // Machine Learning


    } catch (err) { // Means User in NOT Logged In
        let sql = "SELECT * FROM Incidents"

        con.query(sql, (err, result) => {
            if (err) throw err
            res.render("home", { "allIncidents": result })
        })
    }
});

app.use("/auth", authRoutes);

app.get("/incident/:id", (req, res) => {
	
})


server.listen(PORT, () => {
    console.log(`Server running on port ${PORT}!`)
    connectToMongoDB();
});
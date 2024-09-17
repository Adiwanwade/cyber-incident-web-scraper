export const signup = async (req, res) => {
    try {
        const { fullName, password, conformPassword } = req.body;

        if (password !== conformPassword) {
            return res.status(400).json({ error: "Password did not match" });
        }

        let sql = `INSERT INTO Users (username, password) VALUES ('${req.body.username}', '${req.body.password}')`

        con.query(sql, (err, result) => {
            if (err) throw err
        })

        req.user = { "username": req.body.username, "password": req.body.password}

        return res.redirect("/");
    }
    catch (err) {
        console.log("Error in signup Controller: ", err.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
}

export const login = async (req, res) => {
    try {
        const { fullName, password } = req.body;

        let sql = `SELECT * FROM Users WHERE username = '${req.body.username}' AND password = '${req.body.password}'`

        con.query(sql, (err, result) => {   // Result is an Array of JSON Objects
            if (err) throw err

            if (result.length == 0) {
                res.render("login", { "msg": "Login Falied" })
            }

            req.user = { "username": req.body.username, "password": req.body.password}
        })

        res.status(200).redirect("/");

    } catch (err) {
        console.log("Error in login Controller: ", err.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
}

export const logout = (req, res) => { // Problem
    try {
        res.redirect("/auth/login");

    } catch (err) {
        console.log("Error in logout Controller: ", err.message);
        res.status(500).json({ error: "Internal Server Error" });
    }
}
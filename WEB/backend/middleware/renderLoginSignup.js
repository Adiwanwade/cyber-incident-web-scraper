const renderLoginSignup = async (req, res, next) => {
    try {
        const token = req.user.password;
        if(!token){
            return next();
        }

        sql = `select * from incidents where password = ${token}`

        con.query(sql, (err, result) => {   // Result is an Array of JSON Objects
            if (err) throw err
    
            if(!result){
                return next();
            }
    
            req.user = result;
        })

        return res.redirect("/");
        
    } catch (err) {
        console.log("Error in renderLoginSignup Middleware: ", err.message);
        res.status(500).json({error: "Internal Server Error"})
    }
}

export default renderLoginSignup;
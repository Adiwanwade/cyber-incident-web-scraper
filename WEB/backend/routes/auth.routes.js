import express from 'express';
import {signup, login, logout} from "../controllers/auth.controller.js"
import renderLoginSignup from "../middleware/renderLoginSignup.js"

const router = express.Router();

router.get("/signup", renderLoginSignup, (req, res) => {
    res.render("signup");
})

router.get("/login", renderLoginSignup, (req, res) => {
    res.render("login");
})

router.post("/signup", signup)

router.post("/login", login)

router.get("/logout", logout)


export default router;
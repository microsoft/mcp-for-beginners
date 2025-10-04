import { config } from "dotenv";
import { verifyToken } from "./util.js";
import { decode } from "punycode";

config();

let decodedToken = verifyToken(process.env.token || "");
console.log("Decoded Token:", decodedToken);
console.log("User exist", ["User usersson", "user1"].includes(decodedToken?.name || ""));

console.log("Token from .env:", process.env.token);
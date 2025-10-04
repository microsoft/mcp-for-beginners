import jwt from 'jsonwebtoken';
import fs from 'fs';
import path from 'path';

const secretKey = 'your-secret-key'; // Use env vars in production

export function createToken() {
    // Define the payload
    const payload = {
        sub: '1234567890',
        name: 'User usersson',
        admin: true,
        iat: Math.floor(Date.now() / 1000), // Issued at
        exp: Math.floor(Date.now() / 1000) + 60 * 60, // Expires in 1 hour
        scopes: ["Admin.Write", "User.Read"]
    };

    // Define the header (optional, jsonwebtoken sets defaults)
    const header = {
        alg: 'HS256',
        typ: 'JWT'
    };

    // Create the token
    const token = jwt.sign(payload, secretKey, {
        algorithm: 'HS256',
        header: header
    });

    console.log('JWT:', token);
    fs.writeFileSync(path.join(process.cwd(), '.env'), `token=${token}\n`);
    // store to file .env as token=generated token
    console.log('Token stored to .env file');
}

export function verifyToken(token: string) {
    try {
        const decoded = jwt.verify(token, secretKey);
        return decoded;
    } catch (err) {
        console.error('Token verification failed:', err);
        return null;
    }
}

// if run as script, create a token
if (import.meta.url === `file://${process.argv[1]}`) {
    createToken();
}
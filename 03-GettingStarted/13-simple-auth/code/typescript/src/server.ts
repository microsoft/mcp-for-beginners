import express from 'express';

const app = express();

function isValid(secret) {
    return secret === "secret123";
}

app.use((req, res, next) => {
    console.log('Request received:', req.method, req.url, req.headers);
    console.log('Headers:', req.headers["authorization"]);
    if(!req.headers["authorization"]) {
        res.status(401).send('Unauthorized');
        return;
    }
    
    let token = req.headers["authorization"];

    if(!isValid(token)) {
        res.status(403).send('Forbidden');
        return;
    }  

    console.log('Middleware executed');
    next();
});

app.post('/mcp', (req, res) => {
    res.send('MCP endpoint reached');
});

app.listen(8000, () => {
    console.log('Server is running on http://localhost:8000');
});

import express from 'express';

const app = express();

// Toy credential for the lesson, not production authentication.
function isValid(authorization: string | undefined): boolean {
    return authorization === "Bearer secret123";
}

app.use((req, res, next) => {
    // Do not log request headers: Authorization may contain a credential.
    console.log('Request received:', req.method, req.url);
    const authorization = req.headers.authorization;
    if (!isValid(authorization)) {
        res.status(401).send('Unauthorized');
        return;
    }

    next();
});

app.post('/mcp', (req, res) => {
    res.send('MCP endpoint reached');
});

app.listen(8000, () => {
    console.log('Server is running on http://localhost:8000');
});

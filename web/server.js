const express = require('express');
const bodyParser = require('body-parser');
const { exec } = require('child_process');
const app = express();

app.use(bodyParser.urlencoded({ extended: true }));

app.post('/search', (req, res) => {
    const { type, query } = req.body;
    const url = `https://matchmytaste.onrender.com/search_${type}`;
    const data = JSON.stringify({ query });

    exec(`curl -X POST ${url} -H "Content-Type: application/json" -d '${data}'`, (error, stdout, stderr) => {
        if (error) {
            console.error(`Error: ${error.message}`);
            res.send('Error fetching data');
            return;
        }
        if (stderr) {
            console.error(`Stderr: ${stderr}`);
            res.send('Error fetching data');
            return;
        }
        console.log(`Response: ${stdout}`);
        res.send(stdout);
    });
});

app.listen(3000, () => {
    console.log('Server running on port 3000');
});

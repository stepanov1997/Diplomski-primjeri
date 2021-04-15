const pagesFolder = './pages';
import express from 'express';
import http from 'http';
import fs from 'fs';
const app = express();

const champs = JSON.parse(fs.readFileSync("champions.json"))

app.get('/', (req, res) => {
    if(req.query.page){
        let page = req.query.page;
        if(page.endsWith("css"))
            res.writeHead(200, {'Content-Type': 'text/css'});
        else if(page.endsWith("html"))
            res.writeHead(200, {'Content-Type': 'text/html', 'Accept-Charset':'UTF-8'});
        let content = fs.readFileSync(`${pagesFolder}/${page}`, "utf-8")
        res.end(content)
    }else{
        let content = "<h1>Primjeri:</h1>";
        let i = 0;
        content += "<div>"
        for (const file of fs.readdirSync(pagesFolder, "utf-8")) {
            i++;
            content += `<a href=${req.url+"?page="+encodeURI(file)}>${i+".  "+file}</a><br>`
        }
        content += "</div>"
        res.writeHead(200, {'Content-Type': 'text/html', 'Accept-Charset':'UTF-8'});
        res.end(content);
    }
});

app.get('/randomChampion', (req, res) => {
    res.header("Content-Type", "application/json")
    res.end(JSON.stringify(champs[Math.floor(Math.random()*champs.length)]))
})


process.env.PORT="80"
app.listen(process.env.PORT, () =>
    console.log(`Example app listening on port ${process.env.PORT}!`),
);

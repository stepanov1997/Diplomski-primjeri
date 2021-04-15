function rasporediPredmete(predmeti) {
    const predmetiCopy = JSON.parse(JSON.stringify(predmeti))
    let brojCasova = predmeti.reduce((acc, b) => acc + b.brojCasovaSedmicno, 0)
    const raspored = []
    const n = Math.floor(brojCasova * 1.0 / 5) + 1
    for (let i = 0; i < 5; i++) {
        const rasporedZaDan = []
        for (let j = 0; j < n; j++) {
            if (brojCasova === 0)
                break;

            let predmet = undefined
            while (!predmet || predmet.brojCasovaSedmicno === 0) {
                predmet = predmetiCopy[Math.floor(predmetiCopy.length * Math.random())]
            }
            predmet.brojCasovaSedmicno--;
            rasporedZaDan.push(predmet.naziv);
            brojCasova--;
        }
        raspored.push(rasporedZaDan);
    }
    return raspored;
}

function prikaziRasporedCasova() {

    const result = document.getElementById("result")

    const dani = ["Ponedjeljak", "Utorak", "Srijeda", "Četvrtak", "Petak"]
    const predmeti = [
        {naziv: "Frontend programiranje", brojCasovaSedmicno: 4},
        {naziv: "Backend programiranje", brojCasovaSedmicno: 6},
        {naziv: "Baze podataka", brojCasovaSedmicno: 7},
        {naziv: "Osnove veb dizajna", brojCasovaSedmicno: 3},
        {naziv: "Devops pristup: Upravljanje razvojem i operacijama softvera", brojCasovaSedmicno: 4}
    ]

    let casovi = {raspored: rasporediPredmete(predmeti)}

    const naslov = document.createElement("h1")
    naslov.innerText = "Raspored nastave:"
    naslov.className = "text-center"

    const table = document.createElement("table")
    table.className = "table"
    const thead = table.createTHead()
    thead.className = "thead"
    const row = thead.insertRow()
    for (const dan of dani) {
        const headerCell = document.createElement("th")
        headerCell.scope = "col"
        headerCell.innerText = dan
        row.appendChild(headerCell)
    }
    const tbody = table.createTBody()
    for (const rasporedDan of casovi.raspored) {
        const row = tbody.insertRow()
        for (const rasporedCas of rasporedDan) {
            const cell = row.insertCell()
            cell.innerText = rasporedCas
        }
    }

    result.innerHTML = ""
    result.append(naslov, table)
}

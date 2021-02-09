var dataContainer = document.getElementById("networkData");

function readTextFile(file, alertUser) {
    var allText = "";
    var rawFile = new XMLHttpRequest();
    rawFile.open("GET", file, false);
    rawFile.onreadystatechange = function () {
        if(rawFile.readyState === 4) {
            if(rawFile.status === 200 || rawFile.status == 0) {
                allText = rawFile.responseText;
                if (alertUser === 1) {
                    alert(allText);
                }
                
            }
        }
    }
    rawFile.send(null);
    return allText;
}

function parseMassJSON(fileName) {
    console.log(readTextFile(fileName, 0))
}

parseMassJSON("/network_log.json");